/**
 * 关卡管理器 — 灵宠放置传
 * 管理关卡战斗流程：进入关卡 → 多波次战斗 → 结算奖励 → 捕捉
 * 与 battleEngine 配合，复用转珠战斗核心
 */
const { generateStageData, AREAS, isAreaUnlocked } = require('../data/stages')
const { getPetById, getPetInstanceStats } = require('../data/pets')
const { calcCaptureRate, CAPTURE_BALLS } = require('../data/items')
const battleEngine = require('./battle')

/**
 * 进入关卡战斗
 * @param {Main} g - 游戏主实例
 * @param {string} area - 区域ID (metal/wood/earth/water/fire)
 * @param {number} stageNum - 关卡编号 (1-20)
 */
function enterStageBattle(g, area, stageNum) {
  // 检查区域解锁
  if (!isAreaUnlocked(area, g.storage.stageProgress)) {
    console.warn('[StageMgr] 区域未解锁:', area)
    return false
  }

  // 检查体力
  const areaData = AREAS[area]
  if (!areaData) return false
  if (!g.storage.spendStamina(areaData.staminaCost)) {
    console.warn('[StageMgr] 体力不足')
    g._staminaShortage = true
    return false
  }

  // 生成关卡数据
  const stageData = generateStageData(area, stageNum)
  if (!stageData) return false

  g.stageBattleData = stageData
  g.stageBattleWaves = stageData.waves
  g.stageBattleWave = 0
  g.selectedArea = area
  g.selectedStage = stageNum
  g.stageResult = null
  g._stageNoDeaths = true        // 追踪"无人阵亡"星级条件
  g._stageTurnCount = 0          // 追踪"回合限制"星级条件
  g._stageMode = true            // 标记当前为关卡模式（非通天塔）
  g._capturePhase = null         // 捕获阶段数据
  g._waveTransition = null       // 波次过渡动画

  // 从存储中获取战斗队伍的宠物实例
  const battleTeamUids = g.storage.teams.battle
  if (!battleTeamUids || battleTeamUids.length === 0) {
    console.warn('[StageMgr] 战斗队伍为空')
    g.storage.addStamina(areaData.staminaCost) // 退还体力
    return false
  }

  // 构建上场宠物列表（兼容原战斗系统格式）
  g.pets = []
  for (const uid of battleTeamUids) {
    const inst = g.storage.getPetByUid(uid)
    if (!inst) continue
    const template = getPetById(inst.id)
    if (!template) continue
    const stats = getPetInstanceStats(inst)
    g.pets.push({
      ...template,
      uid: inst.uid,
      star: inst.star,
      level: inst.level,
      currentCd: 0,
      // 战斗属性（基于等级和星级）
      atk: stats.atk,
      _baseHp: stats.hp,
      _baseRec: stats.rec,
    })
  }

  // 计算队伍总HP和REC
  const totalHp = g.pets.reduce((sum, p) => sum + (p._baseHp || 0), 0)
  const totalRec = g.pets.reduce((sum, p) => sum + (p._baseRec || 0), 0)
  g.heroMaxHp = totalHp
  g.heroHp = totalHp
  g.heroShield = 0
  g.heroBuffs = []
  g.enemyBuffs = []
  g._teamRec = totalRec

  // 法宝 / 队长技
  // 优先使用队长技（★4宠物在编队第一位时），否则使用装备法宝
  const { getCaptainSkill } = require('../data/pets')
  const captainWeapon = getCaptainSkill(g.pets)
  if (captainWeapon) {
    g.weapon = captainWeapon
  } else {
    const equippedWpn = g.storage.getEquippedWeapon()
    if (equippedWpn) {
      const { WEAPONS } = require('../data/weapons')
      g.weapon = WEAPONS.find(w => w.id === equippedWpn.id) || null
    } else {
      g.weapon = null
    }
  }

  // runBuffs 在关卡模式下重置
  const runMgr = require('./runManager')
  g.runBuffs = runMgr.makeDefaultRunBuffs()
  g.runBuffLog = []
  g.combo = 0
  g.turnCount = 0

  // 进入第一波战斗
  _startWave(g, 0)
  return true
}

/**
 * 开始指定波次
 */
function _startWave(g, waveIndex) {
  if (waveIndex >= g.stageBattleWaves.length) {
    // 所有波次完成 → 胜利结算
    _onAllWavesCleared(g)
    return
  }

  g.stageBattleWave = waveIndex
  const wave = g.stageBattleWaves[waveIndex]

  // 波次过渡动画（非首波时展示）
  if (waveIndex > 0) {
    g._waveTransition = { wave: waveIndex + 1, timer: 40 }
  }

  // 选取本波次敌人（可能多只，目前逐只打）
  g._waveEnemies = [...wave.enemies]
  g._waveEnemyIndex = 0

  // 进入与第一只敌人的战斗（有过渡动画时延迟）
  if (waveIndex > 0) {
    g._waveStartPending = true
  } else {
    _fightNextEnemy(g)
  }
}

/**
 * 与波次中下一只敌人战斗
 */
function _fightNextEnemy(g) {
  if (g._waveEnemyIndex >= g._waveEnemies.length) {
    // 本波次所有敌人打完 → 下一波
    _startWave(g, g.stageBattleWave + 1)
    return
  }

  const enemyData = g._waveEnemies[g._waveEnemyIndex]
  // 使用原战斗引擎进入战斗
  battleEngine.enterBattle(g, enemyData)
  g.scene = 'battle'
}

/**
 * 关卡模式下的胜利处理（单只敌人被击败后）
 */
function onStageBattleVictory(g) {
  g._stageTurnCount += g.turnCount

  // 记录本次击败的敌人（用于捕捉判定）
  const enemy = g.enemy
  g._lastDefeatedEnemy = enemy

  // 检查是否可以捕获（敌人有 petId 且不是已拥有满星）
  if (enemy && enemy.petId && !enemy.isBoss) {
    // 进入捕获阶段
    g._capturePhase = {
      enemy: { ...enemy },
      petId: enemy.petId,
      canCapture: true,
      selectedBall: null,
      captureResult: null,
      animTimer: 0,
    }
    // 不立即推进，等待玩家选择捕获或跳过
    return
  }

  // 无捕获机会，正常推进
  _advanceAfterVictory(g)
}

/**
 * 胜利后推进到下一只/下一波
 */
function _advanceAfterVictory(g) {
  g._capturePhase = null

  // 下一只敌人
  g._waveEnemyIndex++
  if (g._waveEnemyIndex < g._waveEnemies.length) {
    // 还有敌人，继续战斗（保留HP/盾/Buff状态）
    _fightNextEnemy(g)
  } else if (g.stageBattleWave + 1 < g.stageBattleWaves.length) {
    // 还有下一波
    _startWave(g, g.stageBattleWave + 1)
  } else {
    // 全部波次通过
    _onAllWavesCleared(g)
  }
}

/**
 * 尝试捕获
 */
function attemptCapture(g, ballType) {
  const cp = g._capturePhase
  if (!cp || !cp.canCapture) return

  // 检查球数量
  if (!g.storage.useItem(ballType, 1)) {
    console.warn('[StageMgr] 灵珠不足:', ballType)
    return
  }

  // 计算主属性（队伍中数量最多的属性）
  const attrCount = {}
  g.pets.forEach(p => { attrCount[p.attr] = (attrCount[p.attr] || 0) + 1 })
  let teamAttr = null, maxCount = 0
  for (const [a, c] of Object.entries(attrCount)) {
    if (c > maxCount) { maxCount = c; teamAttr = a }
  }

  const rate = calcCaptureRate(ballType, cp.enemy, teamAttr)
  const roll = Math.random()
  const success = roll < rate

  cp.captureResult = { success, rate, ballType }
  cp.animTimer = 60  // 动画帧数

  if (success) {
    // 捕获成功：添加宠物到库
    const template = getPetById(cp.petId)
    if (template) {
      const newPet = g.storage.addPet({ id: template.id, attr: template.attr, star: 1 })
      cp.capturedPet = newPet
    }
  }
}

/**
 * 跳过捕获
 */
function skipCapture(g) {
  _advanceAfterVictory(g)
}

/**
 * 捕获动画结束后确认
 */
function confirmCapture(g) {
  _advanceAfterVictory(g)
}

/**
 * 所有波次通关 → 结算
 */
function _onAllWavesCleared(g) {
  const data = g.stageBattleData
  const area = g.selectedArea
  const stageNum = g.selectedStage
  const isFirstClear = g.storage.getStageClearedCount(area) < stageNum

  // 计算星级
  let stars = 1   // star1: 通关
  if (g._stageNoDeaths) stars = 2  // star2: 无人阵亡
  if (data.starTargets && g._stageTurnCount <= data.starTargets.star3Turns) {
    stars = 3     // star3: 回合限制内通关
  }

  // 选择奖励
  const rewards = isFirstClear ? { ...data.firstClearRewards } : { ...data.repeatRewards }
  rewards.isFirstClear = isFirstClear
  rewards.stars = stars

  // 星级额外奖励（首次通关时）
  if (isFirstClear) {
    if (stars >= 2) {
      rewards.gold = (rewards.gold || 0) + 50
      rewards.bonusStar2 = true
    }
    if (stars >= 3) {
      rewards.gem = (rewards.gem || 0) + 2
      rewards.bonusStar3 = true
    }
  }

  // 发放奖励
  if (rewards.gold) g.storage.addGold(rewards.gold)
  if (rewards.gem) g.storage.addGem(rewards.gem)
  if (rewards.exp) {
    // 经验分配给战斗队伍
    const teamUids = g.storage.teams.battle
    if (teamUids.length > 0) {
      const expEach = Math.floor(rewards.exp / teamUids.length)
      teamUids.forEach(uid => g.storage.addPetExp(uid, expEach))
    }
    g.storage.addPlayerExp(Math.floor(rewards.exp * 0.1))
  }

  // 发放道具奖励（首通奖励中的灵珠等直接放在奖励对象中）
  if (rewards.normalBall) g.storage.addItem('normalBall', rewards.normalBall)
  if (rewards.superBall)  g.storage.addItem('superBall', rewards.superBall)
  if (rewards.masterBall) g.storage.addItem('masterBall', rewards.masterBall)
  if (rewards.items) {
    for (const [itemKey, amount] of Object.entries(rewards.items)) {
      g.storage.addItem(itemKey, amount)
    }
  }

  // 更新关卡进度
  g.storage.updateStageProgress(area, stageNum, stars)
  g.storage.recordBattle(g.combo)

  // 宠物掉落判定
  rewards.petDrops = []
  if (data.repeatRewards && data.repeatRewards.petDropRate) {
    if (Math.random() < data.repeatRewards.petDropRate) {
      // 从本关怪物中随机一只对应宠物
      const allEnemies = []
      for (const wave of g.stageBattleWaves) {
        for (const e of wave.enemies) {
          if (e.petId) allEnemies.push(e)
        }
      }
      if (allEnemies.length > 0) {
        const picked = allEnemies[Math.floor(Math.random() * allEnemies.length)]
        const template = getPetById(picked.petId)
        if (template) {
          const newPet = g.storage.addPet({ id: template.id, attr: template.attr, star: 1 })
          rewards.petDrops.push(newPet)
        }
      }
    }
  }

  g.stageResult = rewards
  g._stageMode = false
  g.scene = 'stageResult'
}

/**
 * 关卡战斗失败
 */
function onStageBattleDefeat(g) {
  g.stageResult = {
    defeat: true,
    stars: 0,
    area: g.selectedArea,
    stageNum: g.selectedStage,
  }
  g._stageMode = false
  g._capturePhase = null
  g.scene = 'stageResult'
}

module.exports = {
  enterStageBattle,
  onStageBattleVictory,
  onStageBattleDefeat,
  attemptCapture,
  skipCapture,
  confirmCapture,
}
