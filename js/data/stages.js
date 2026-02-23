/**
 * 关卡系统 — 灵宠放置传
 * 5大区域 × 20关 = 100关
 * 复用原版 tower.js 的怪物生成、五行系统和事件数据
 */

const {
  ATTRS, ATTR_NAME,
  MONSTER_NAMES, ELITE_NAMES,
  BOSS_POOL_10, BOSS_POOL_20, BOSS_POOL_30,
  BOSS_SKILL_SETS,
  ENEMY_SKILLS,
} = require('./tower')

// ===== 区域定义 =====
const AREAS = {
  metal: {
    id: 'metal', name: '金风峡谷', desc: '西域荒原尽头的金色峡谷，金属性妖兽的聚居地',
    attr: 'metal', difficulty: 2,
    bgPath: 'assets/battle/battle_metal.jpg',
    mapBgPath: 'assets/backgrounds/home_bg.jpg',
    stageCount: 20,
    staminaCost: 5,
    unlockCondition: null,  // 初始解锁
  },
  wood: {
    id: 'wood', name: '翠木森林', desc: '万木丛生的灵木古林，木属性妖兽的乐园',
    attr: 'wood', difficulty: 2,
    bgPath: 'assets/battle/battle_wood.jpg',
    mapBgPath: 'assets/backgrounds/home_bg.jpg',
    stageCount: 20,
    staminaCost: 5,
    unlockCondition: { area: 'metal', stage: 5 },  // 金风峡谷通关5关解锁
  },
  earth: {
    id: 'earth', name: '厚土高原', desc: '大地脉络汇聚的神秘高原，土属性妖兽的领地',
    attr: 'earth', difficulty: 3,
    bgPath: 'assets/battle/battle_earth.jpg',
    mapBgPath: 'assets/backgrounds/home_bg.jpg',
    stageCount: 20,
    staminaCost: 6,
    unlockCondition: { area: 'wood', stage: 5 },
  },
  water: {
    id: 'water', name: '深水龙宫', desc: '海底深处的上古龙宫遗迹，水属性妖兽的圣地',
    attr: 'water', difficulty: 4,
    bgPath: 'assets/battle/battle_water.jpg',
    mapBgPath: 'assets/backgrounds/home_bg.jpg',
    stageCount: 20,
    staminaCost: 7,
    unlockCondition: { area: 'earth', stage: 5 },
  },
  fire: {
    id: 'fire', name: '烈火火山', desc: '永恒燃烧的火山群，火属性妖兽的终极修炼场',
    attr: 'fire', difficulty: 5,
    bgPath: 'assets/battle/battle_fire.jpg',
    mapBgPath: 'assets/backgrounds/home_bg.jpg',
    stageCount: 20,
    staminaCost: 8,
    unlockCondition: { area: 'water', stage: 5 },
  },
}

// 区域解锁顺序
const AREA_ORDER = ['metal', 'wood', 'earth', 'water', 'fire']

// ===== 怪物数值层级表（20关制，每区域独立） =====
// 每区域内 1~20 关，数值独立缩放
const STAGE_TIERS = {
  metal: [
    { minStage:1,  maxStage:5,  hpMin:120,  hpMax:240,   atkMin:6,   atkMax:10  },
    { minStage:6,  maxStage:10, hpMin:250,  hpMax:420,   atkMin:10,  atkMax:16  },
    { minStage:11, maxStage:15, hpMin:440,  hpMax:700,   atkMin:15,  atkMax:24  },
    { minStage:16, maxStage:20, hpMin:720,  hpMax:1100,  atkMin:22,  atkMax:34  },
  ],
  wood: [
    { minStage:1,  maxStage:5,  hpMin:150,  hpMax:280,   atkMin:7,   atkMax:12  },
    { minStage:6,  maxStage:10, hpMin:300,  hpMax:500,   atkMin:12,  atkMax:18  },
    { minStage:11, maxStage:15, hpMin:520,  hpMax:850,   atkMin:17,  atkMax:28  },
    { minStage:16, maxStage:20, hpMin:870,  hpMax:1350,  atkMin:26,  atkMax:40  },
  ],
  earth: [
    { minStage:1,  maxStage:5,  hpMin:200,  hpMax:360,   atkMin:8,   atkMax:14  },
    { minStage:6,  maxStage:10, hpMin:380,  hpMax:650,   atkMin:14,  atkMax:22  },
    { minStage:11, maxStage:15, hpMin:680,  hpMax:1100,  atkMin:20,  atkMax:32  },
    { minStage:16, maxStage:20, hpMin:1120, hpMax:1700,  atkMin:30,  atkMax:46  },
  ],
  water: [
    { minStage:1,  maxStage:5,  hpMin:260,  hpMax:460,   atkMin:10,  atkMax:16  },
    { minStage:6,  maxStage:10, hpMin:480,  hpMax:800,   atkMin:16,  atkMax:26  },
    { minStage:11, maxStage:15, hpMin:820,  hpMax:1400,  atkMin:24,  atkMax:38  },
    { minStage:16, maxStage:20, hpMin:1420, hpMax:2200,  atkMin:36,  atkMax:52  },
  ],
  fire: [
    { minStage:1,  maxStage:5,  hpMin:320,  hpMax:560,   atkMin:12,  atkMax:20  },
    { minStage:6,  maxStage:10, hpMin:580,  hpMax:1000,  atkMin:20,  atkMax:30  },
    { minStage:11, maxStage:15, hpMin:1020, hpMax:1700,  atkMin:28,  atkMax:44  },
    { minStage:16, maxStage:20, hpMin:1720, hpMax:2800,  atkMin:42,  atkMax:62  },
  ],
}

// ===== 工具函数 =====
function _lerp(a, b, t) { return a + (b - a) * t }
function _rand(min, max) { return Math.floor(Math.random() * (max - min + 1)) + min }
function _pick(arr) { return arr[Math.floor(Math.random() * arr.length)] }

// ===== 关卡数据生成 =====

/**
 * 生成指定关卡的怪物波次
 * @param {string} area - 区域ID
 * @param {number} stageNum - 关卡号 1-20
 * @returns {object} { waves: [{enemies:[...]}, ...], isBoss, staminaCost, rewards }
 */
function generateStageData(area, stageNum) {
  const areaData = AREAS[area]
  if (!areaData) throw new Error('Invalid area: ' + area)

  const isBoss = (stageNum === 10 || stageNum === 20)
  const isElite = (stageNum === 5 || stageNum === 15)

  // 波次数：普通1-2波，精英1波，BOSS1波
  let waveCount = 1
  if (!isBoss && !isElite) {
    if (stageNum <= 5) waveCount = 1
    else if (stageNum <= 10) waveCount = _rand(1, 2)
    else if (stageNum <= 15) waveCount = _rand(1, 2)
    else waveCount = _rand(2, 3)
  }

  const waves = []
  for (let w = 0; w < waveCount; w++) {
    if (isBoss && w === waveCount - 1) {
      waves.push({ enemies: [_generateBoss(area, stageNum)] })
    } else if (isElite && w === waveCount - 1) {
      waves.push({ enemies: [_generateElite(area, stageNum)] })
    } else {
      // 普通波: 1只怪
      waves.push({ enemies: [_generateMonster(area, stageNum)] })
    }
  }

  // 首通奖励
  const firstClearRewards = _calcFirstClearRewards(area, stageNum, isBoss, isElite)

  // 重复通关奖励（经验 + 金币 + 掉落概率）
  const repeatRewards = {
    exp: 20 + stageNum * 5 + AREA_ORDER.indexOf(area) * 15,
    gold: 10 + stageNum * 3 + AREA_ORDER.indexOf(area) * 8,
    petDropRate: isBoss ? 0.50 : isElite ? 0.25 : 0.15,
  }

  // 星级目标
  const star3Turns = isBoss ? (8 + stageNum) : (5 + Math.floor(stageNum / 3))
  const starTargets = {
    star1: '通关',
    star2: '无人阵亡通关',
    star3: `${star3Turns}回合内通关`,
    star3Turns,
  }

  return {
    area,
    stageNum,
    waves,
    isBoss,
    isElite,
    staminaCost: areaData.staminaCost,
    firstClearRewards,
    repeatRewards,
    starTargets,
    bgPath: areaData.bgPath,
  }
}

// 生成普通怪物
function _generateMonster(area, stageNum) {
  const attr = AREAS[area].attr
  const tiers = STAGE_TIERS[area]
  let tier = tiers[tiers.length - 1]
  for (const t of tiers) {
    if (stageNum >= t.minStage && stageNum <= t.maxStage) { tier = t; break }
  }

  const progress = Math.min(1, (stageNum - tier.minStage) / Math.max(1, tier.maxStage - tier.minStage))
  const rand = () => 0.85 + Math.random() * 0.30
  let hp  = Math.round(_lerp(tier.hpMin, tier.hpMax, progress) * rand())
  let atk = Math.round(_lerp(tier.atkMin, tier.atkMax, progress) * rand())

  const names = MONSTER_NAMES[attr]
  const nameIdx = Math.min(Math.floor((stageNum - 1) / 3), names.length - 1)
  const name = names[nameIdx]

  // 技能
  const skills = []
  const skillPool1 = ['poison','seal','convert']
  const skillPool2 = ['atkBuff','defDown','healBlock']
  if (stageNum <= 5) {
    skills.push(_pick(['convert','aoe']))
  } else if (stageNum <= 10) {
    skills.push(_pick(skillPool1))
  } else {
    skills.push(_pick(skillPool1))
    if (stageNum >= 15) skills.push(_pick(skillPool2))
  }

  const attrKeyMap = { metal:'m', wood:'w', earth:'e', water:'s', fire:'f' }
  const monKey = attrKeyMap[attr]
  const monIdx = nameIdx + 1
  const avatar = `enemies/mon_${monKey}_${monIdx}`

  // 捕捉掉落的宠物ID映射（怪物名→同名宠物）
  const petId = `${attrKeyMap[attr]}${monIdx}`

  return { name, attr, hp, maxHp: hp, atk, def: Math.round(atk * 0.35), skills, avatar, petId }
}

// 生成精英怪
function _generateElite(area, stageNum) {
  const base = _generateMonster(area, stageNum)
  const attr = base.attr

  base.hp    = Math.round(base.hp * (2.2 + Math.random() * 0.6))
  base.maxHp = base.hp
  base.atk   = Math.round(base.atk * (1.6 + Math.random() * 0.4))
  base.def   = Math.round(base.def * 1.5)
  base.name  = _pick(ELITE_NAMES[attr])
  base.isElite = true

  const skillPool = ['stun','defDown','selfHeal','breakBead','atkBuff','poison','seal','eliteSealRow','eliteSealAttr']
  const s1 = _pick(skillPool)
  let s2 = _pick(skillPool); while (s2 === s1) s2 = _pick(skillPool)
  base.skills = [s1, s2]

  const eliteAttrMap = { metal:'m', wood:'w', water:'s', fire:'f', earth:'e' }
  const eliteKey = eliteAttrMap[attr]
  const eliteNames = ELITE_NAMES[attr]
  const eliteIdx = eliteNames.indexOf(base.name) + 1 || _rand(1, 3)
  base.avatar = `enemies/elite_${eliteKey}_${eliteIdx}`
  base.battleBg = `enemies/bg_elite_${eliteKey}_${_rand(1, 3)}`

  return base
}

// 生成BOSS
function _generateBoss(area, stageNum) {
  const base = _generateMonster(area, stageNum)
  const attr = AREAS[area].attr
  const bossLevel = stageNum <= 10 ? 1 : 2

  base.hp    = Math.round(base.hp * (2.5 + (bossLevel - 1) * 0.8))
  base.maxHp = base.hp
  base.atk   = Math.round(base.atk * (1.5 + (bossLevel - 1) * 0.3))
  base.def   = Math.round(base.def * (1.2 + (bossLevel - 1) * 0.2))
  base.isBoss = true
  base.attr  = attr

  // 每区域用不同BOSS池
  const areaIdx = AREA_ORDER.indexOf(area)
  let pool
  if (stageNum <= 10) pool = BOSS_POOL_10
  else pool = BOSS_POOL_20

  const chosen = pool[areaIdx % pool.length]
  base.name = chosen.name
  base.avatar = `enemies/boss_${chosen.bossNum}`
  base.battleBg = `enemies/bg_boss_${chosen.bossNum}`

  base.skills = BOSS_SKILL_SETS[chosen.name]
    ? [...BOSS_SKILL_SETS[chosen.name]]
    : (BOSS_SKILL_SETS[chosen.bossNum] ? [...BOSS_SKILL_SETS[chosen.bossNum]] : ['bossRage', 'bossBlitz'])

  return base
}

// 计算首通奖励
function _calcFirstClearRewards(area, stageNum, isBoss, isElite) {
  const areaIdx = AREA_ORDER.indexOf(area)
  const rewards = {
    gold: 50 + stageNum * 10 + areaIdx * 30,
    gem: 0,
    normalBall: 0,
    superBall: 0,
    exp: 30 + stageNum * 8 + areaIdx * 20,
  }

  if (isBoss) {
    rewards.gold += 200
    rewards.gem += 5
    rewards.superBall += 1
  } else if (isElite) {
    rewards.gold += 100
    rewards.gem += 2
    rewards.normalBall += 2
  } else if (stageNum % 3 === 0) {
    rewards.normalBall += 1
  }

  // 星级奖励
  rewards.starRewards = {
    1: { gold: 20 },
    2: { normalBall: 1 },
    3: { gem: 1 },
  }

  return rewards
}

// ===== 检查区域是否解锁 =====
function isAreaUnlocked(area, stageProgress) {
  const areaData = AREAS[area]
  if (!areaData) return false
  if (!areaData.unlockCondition) return true  // 无条件即解锁
  const cond = areaData.unlockCondition
  const progress = stageProgress[cond.area]
  if (!progress) return false
  return progress.cleared >= cond.stage
}

// ===== 获取所有可用区域 =====
function getAvailableAreas(stageProgress) {
  return AREA_ORDER.filter(a => isAreaUnlocked(a, stageProgress))
}

// ===== 每日副本定义 =====
const DAILY_DUNGEONS = {
  gold: {
    id: 'gold', name: '金币洞窟', desc: '大量金币产出',
    maxDaily: 3, staminaCost: 10,
    available: 'daily',  // 每日开放
    generateRewards: (level) => ({ gold: 200 + level * 50 }),
  },
  exp: {
    id: 'exp', name: '经验秘境', desc: '获取经验珠',
    maxDaily: 3, staminaCost: 10,
    available: 'daily',
    generateRewards: (level) => ({
      expOrb_s: 3 + Math.floor(level / 5),
      expOrb_m: level >= 5 ? 1 : 0,
    }),
  },
  ball: {
    id: 'ball', name: '灵珠试炼', desc: '获取各级灵珠',
    maxDaily: 3, staminaCost: 12,
    available: [2, 4, 6],  // 周二/四/六
    generateRewards: (level) => ({
      normalBall: 2 + Math.floor(level / 3),
      superBall: level >= 10 ? 1 : 0,
    }),
  },
}

module.exports = {
  AREAS,
  AREA_ORDER,
  STAGE_TIERS,
  DAILY_DUNGEONS,
  generateStageData,
  isAreaUnlocked,
  getAvailableAreas,
}
