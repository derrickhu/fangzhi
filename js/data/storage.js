/**
 * 存储管理 — 灵宠放置传
 * 永久养成存档：宠物库、法宝库、关卡进度、货币、背包、放置、通天塔
 * 本地缓存 + 云数据库双重存储
 */

const LOCAL_KEY = 'lingpet_idle_v1'
const LEGACY_KEY = 'wxtower_v1'   // 旧版存档key，用于迁移
const CLOUD_ENV = 'cloud1-2gkio0pq80e2bc3b'

// ===== 默认持久化数据结构 =====
function defaultPersist() {
  return {
    // === 版本号 ===
    version: 2,

    // === 玩家基础 ===
    playerLevel: 1,               // 探险等级
    playerExp: 0,                 // 探险经验
    gold: 500,                    // 金币（初始赠送500）
    gem: 10,                      // 灵石（初始赠送10）
    stamina: 100,                 // 当前体力
    staminaMax: 100,              // 体力上限
    lastStaminaTime: 0,           // 上次体力回复时间戳

    // === 宠物库（所有已拥有宠物实例） ===
    ownedPets: [],
    // 每只宠物: { uid, id, attr, star, level, exp, locked }

    // === 编队 ===
    teams: {
      battle: [],                 // 战斗队伍 uid 数组（最多5）
      idle: [],                   // 挂机队伍 uid 数组（最多5）
    },

    // === 法宝库 ===
    ownedWeapons: [],
    // 每件: { id, level }
    equippedWeaponId: null,       // 当前装备的法宝ID

    // === 背包 ===
    inventory: {
      normalBall: 5,              // 普通灵珠
      superBall: 2,               // 高级灵珠
      masterBall: 0,              // 大师灵珠
      ultraBall: 0,               // 五行灵珠
      expOrb_s: 3,                // 小经验珠
      expOrb_m: 0,                // 中经验珠
      expOrb_l: 0,                // 大经验珠
    },

    // === 关卡进度 ===
    stageProgress: {
      metal: { cleared: 0, stars: {} },   // stars: { 1: 3, 2: 2, ... }
      wood:  { cleared: 0, stars: {} },
      earth: { cleared: 0, stars: {} },
      water: { cleared: 0, stars: {} },
      fire:  { cleared: 0, stars: {} },
    },

    // === 放置挂机 ===
    idle: {
      area: null,                 // 挂机区域 'metal'|'wood'|...
      startTime: 0,               // 开始时间戳
      teamUids: [],               // 挂机队伍
      maxHours: 8,                // 最大累积小时数
    },

    // === 每日数据 ===
    daily: {
      date: '',
      dungeonCount: { gold: 0, exp: 0, ball: 0, attr: 0 },
      shopPurchases: {},
      adWatchCount: 0,
      staminaAdCount: 0,
    },

    // === 通天塔（保留原版Roguelike作为周常挑战） ===
    tower: {
      bestFloor: 0,
      weeklyBestFloor: 0,
      lastResetWeek: '',
    },

    // === 图鉴 & 统计 ===
    petDex: [],                   // 历史收集到3星的宠物ID列表
    petDexSeen: [],               // 已查看过详情的宠物ID列表
    stats: {
      totalBattles: 0,
      totalCombos: 0,
      maxCombo: 0,
      bestFloorPets: [],
      bestFloorWeapon: null,
      bestTotalTurns: 0,
    },

    // === 设置 ===
    settings: {
      bgmOn: true,
      sfxOn: true,
    },

    // === 成就进度 ===
    achievements: {},

    // === 旧版兼容（迁移后标记） ===
    _migratedFromV1: false,
  }
}

// ===== 体力配置 =====
const STAMINA_REGEN_INTERVAL = 5 * 60 * 1000  // 5分钟回复1点
const STAMINA_AD_RESTORE = 20                   // 看广告回复20点

// ===== 宠物UID生成 =====
let _uidCounter = 0
function generatePetUid() {
  _uidCounter++
  return `pet_${Date.now()}_${_uidCounter}_${Math.random().toString(36).substr(2, 4)}`
}

class Storage {
  constructor() {
    this._d = null
    this._cloudReady = false
    this._openid = ''
    this._cloudSyncTimer = null
    this._cloudInitDone = false
    this._pendingSync = false
    // 用户信息
    this.userInfo = null
    this.userAuthorized = false
    // 排行榜缓存
    this.rankAllList = []
    this.rankDexList = []
    this.rankComboList = []
    this.rankPowerList = []
    this.rankAllMyRank = -1
    this.rankDexMyRank = -1
    this.rankComboMyRank = -1
    this.rankPowerMyRank = -1
    this.rankLoading = false
    this.rankLastFetch = 0
    this.rankLastFetchTab = ''
    this._load()
    this._loadUserInfo()
    this._initCloud()
    // 启动时结算体力
    this._recoverStamina()
  }

  // ===== 便捷访问器 =====
  get playerLevel()  { return this._d.playerLevel }
  get playerExp()    { return this._d.playerExp }
  get gold()         { return this._d.gold }
  get gem()          { return this._d.gem }
  get stamina()      { return this._d.stamina }
  get staminaMax()   { return this._d.staminaMax }
  get ownedPets()    { return this._d.ownedPets }
  get teams()        { return this._d.teams }
  get ownedWeapons() { return this._d.ownedWeapons }
  get equippedWeaponId() { return this._d.equippedWeaponId }
  get inventory()    { return this._d.inventory }
  get stageProgress(){ return this._d.stageProgress }
  get idle()         { return this._d.idle }
  get daily()        { return this._d.daily }
  get tower()        { return this._d.tower }
  get petDex()       { return this._d.petDex || [] }
  get petDexSeen()   { return this._d.petDexSeen || [] }
  get stats()        { return this._d.stats }
  get settings()     { return this._d.settings }
  // 兼容旧代码
  get bestFloor()    { return this._d.tower.bestFloor }
  get totalRuns()    { return this._d.stats.totalBattles }

  // ===== 货币操作 =====
  addGold(amount) {
    this._d.gold = Math.max(0, this._d.gold + amount)
    this._save()
  }

  addGem(amount) {
    this._d.gem = Math.max(0, this._d.gem + amount)
    this._save()
  }

  spendGold(amount) {
    if (this._d.gold < amount) return false
    this._d.gold -= amount
    this._save()
    return true
  }

  spendGem(amount) {
    if (this._d.gem < amount) return false
    this._d.gem -= amount
    this._save()
    return true
  }

  // ===== 体力系统 =====
  _recoverStamina() {
    if (!this._d.lastStaminaTime) {
      this._d.lastStaminaTime = Date.now()
      return
    }
    const now = Date.now()
    const elapsed = now - this._d.lastStaminaTime
    const recovered = Math.floor(elapsed / STAMINA_REGEN_INTERVAL)
    if (recovered > 0 && this._d.stamina < this._d.staminaMax) {
      this._d.stamina = Math.min(this._d.staminaMax, this._d.stamina + recovered)
      this._d.lastStaminaTime = now
      this._save()
    }
  }

  updateStamina() {
    this._recoverStamina()
    return this._d.stamina
  }

  spendStamina(amount) {
    this._recoverStamina()
    if (this._d.stamina < amount) return false
    this._d.stamina -= amount
    this._d.lastStaminaTime = Date.now()
    this._save()
    return true
  }

  addStamina(amount) {
    this._d.stamina = Math.min(this._d.staminaMax, this._d.stamina + amount)
    this._save()
  }

  // ===== 宠物库操作 =====
  addPet(petData) {
    // petData: { id, attr, star } — 从模板数据创建实例
    const uid = generatePetUid()
    const instance = {
      uid,
      id: petData.id,
      attr: petData.attr,
      star: petData.star || 1,
      level: 1,
      exp: 0,
      locked: false,
    }
    this._d.ownedPets.push(instance)
    this._save()
    return instance
  }

  removePet(uid) {
    const idx = this._d.ownedPets.findIndex(p => p.uid === uid)
    if (idx < 0) return null
    // 不能删除编队中的宠物
    if (this._d.teams.battle.includes(uid) || this._d.teams.idle.includes(uid)) return null
    if (this._d.ownedPets[idx].locked) return null
    const removed = this._d.ownedPets.splice(idx, 1)[0]
    this._save()
    return removed
  }

  getPetByUid(uid) {
    return this._d.ownedPets.find(p => p.uid === uid) || null
  }

  // 宠物升级（增加经验）
  addPetExp(uid, expAmount) {
    const pet = this.getPetByUid(uid)
    if (!pet) return null
    const { getMaxLevel, getExpToLevel } = require('./pets')
    const maxLv = getMaxLevel(pet.star)
    if (pet.level >= maxLv) return pet
    pet.exp += expAmount
    // 连续升级
    while (pet.level < maxLv) {
      const needed = getExpToLevel(pet.level + 1)
      if (pet.exp >= needed) {
        pet.exp -= needed
        pet.level++
      } else break
    }
    if (pet.level >= maxLv) pet.exp = 0
    this._save()
    return pet
  }

  // 宠物升星
  starUpPet(uid) {
    const pet = this.getPetByUid(uid)
    if (!pet || pet.star >= 3) return false
    pet.star++
    this._save()
    return true
  }

  // ===== 编队操作 =====
  setBattleTeam(uidArray) {
    this._d.teams.battle = uidArray.slice(0, 5)
    this._save()
  }

  setIdleTeam(uidArray) {
    this._d.teams.idle = uidArray.slice(0, 5)
    this._save()
  }

  // ===== 法宝操作 =====
  addWeapon(weaponId) {
    const existing = this._d.ownedWeapons.find(w => w.id === weaponId)
    if (existing) {
      // 已有则升级
      existing.level = (existing.level || 1) + 1
    } else {
      this._d.ownedWeapons.push({ id: weaponId, level: 1 })
    }
    this._save()
  }

  equipWeapon(weaponId) {
    this._d.equippedWeaponId = weaponId
    this._save()
  }

  getEquippedWeapon() {
    if (!this._d.equippedWeaponId) return null
    return this._d.ownedWeapons.find(w => w.id === this._d.equippedWeaponId) || null
  }

  // ===== 背包操作 =====
  addItem(itemKey, amount) {
    if (this._d.inventory[itemKey] === undefined) this._d.inventory[itemKey] = 0
    this._d.inventory[itemKey] += amount
    this._save()
  }

  useItem(itemKey, amount) {
    if (!this._d.inventory[itemKey] || this._d.inventory[itemKey] < amount) return false
    this._d.inventory[itemKey] -= amount
    this._save()
    return true
  }

  getItemCount(itemKey) {
    return this._d.inventory[itemKey] || 0
  }

  // ===== 关卡进度 =====
  updateStageProgress(area, stageNum, starCount) {
    const prog = this._d.stageProgress[area]
    if (!prog) return
    if (stageNum > prog.cleared) prog.cleared = stageNum
    const prev = prog.stars[stageNum] || 0
    if (starCount > prev) prog.stars[stageNum] = starCount
    this._save()
  }

  getStageClearedCount(area) {
    return this._d.stageProgress[area]?.cleared || 0
  }

  getStageStars(area, stageNum) {
    return this._d.stageProgress[area]?.stars[stageNum] || 0
  }

  getTotalStars() {
    let total = 0
    for (const area of ['metal','wood','earth','water','fire']) {
      const prog = this._d.stageProgress[area]
      if (prog && prog.stars) {
        for (const s of Object.values(prog.stars)) total += s
      }
    }
    return total
  }

  // ===== 放置挂机 =====
  startIdle(area, teamUids) {
    this._d.idle = {
      area,
      startTime: Date.now(),
      teamUids: teamUids.slice(0, 5),
      maxHours: this._d.idle.maxHours || 8,
    }
    this._save()
  }

  // 结算挂机收益
  collectIdleRewards() {
    const idle = this._d.idle
    if (!idle.area || !idle.startTime) return null

    const now = Date.now()
    const elapsedMs = now - idle.startTime
    const maxMs = (idle.maxHours || 8) * 3600 * 1000
    const effectiveMs = Math.min(elapsedMs, maxMs)
    const hours = effectiveMs / 3600000

    // 基于已通关关卡数计算收益
    const clearedCount = this.getStageClearedCount(idle.area)
    if (clearedCount <= 0) return null

    const baseExpPerHour = 50 + clearedCount * 15
    const baseGoldPerHour = 30 + clearedCount * 10

    const rewards = {
      exp: Math.floor(baseExpPerHour * hours),
      gold: Math.floor(baseGoldPerHour * hours),
      hours: Math.round(hours * 10) / 10,
      petDrops: [],   // 极低概率掉落宠物
    }

    // 宠物掉落概率：每小时5%基础
    const dropChancePerHour = 0.05 + clearedCount * 0.005
    if (Math.random() < dropChancePerHour * hours) {
      rewards.petDrops.push({ area: idle.area, count: 1 })
    }

    // 发放奖励
    this.addGold(rewards.gold)
    // 经验分配给挂机队伍宠物
    if (idle.teamUids.length > 0) {
      const expEach = Math.floor(rewards.exp / idle.teamUids.length)
      idle.teamUids.forEach(uid => this.addPetExp(uid, expEach))
    }

    // 重置挂机计时
    this._d.idle.startTime = now
    this._save()
    return rewards
  }

  stopIdle() {
    const rewards = this.collectIdleRewards()
    this._d.idle.area = null
    this._d.idle.startTime = 0
    this._d.idle.teamUids = []
    this._save()
    return rewards
  }

  // ===== 每日重置检查 =====
  checkDailyReset() {
    const today = new Date().toISOString().slice(0, 10)
    if (this._d.daily.date !== today) {
      this._d.daily = {
        date: today,
        dungeonCount: { gold: 0, exp: 0, ball: 0, attr: 0 },
        shopPurchases: {},
        adWatchCount: 0,
        staminaAdCount: 0,
      }
      this._save()
    }
    // 通天塔周重置（每周一重置周最佳）
    this._checkTowerWeeklyReset()
  }

  _checkTowerWeeklyReset() {
    const now = new Date()
    // 计算本周一的日期字符串 (ISO week)
    const day = now.getDay() || 7  // 周日=7
    const monday = new Date(now)
    monday.setDate(now.getDate() - day + 1)
    const weekKey = monday.toISOString().slice(0, 10)
    if (this._d.tower.lastResetWeek !== weekKey) {
      this._d.tower.weeklyBestFloor = 0
      this._d.tower.lastResetWeek = weekKey
      this._save()
      console.log('[Tower] 周重置完成, weekKey:', weekKey)
    }
  }

  // ===== 每日副本次数 =====
  getDungeonCount(dungeonId) {
    return (this._d.daily.dungeonCount && this._d.daily.dungeonCount[dungeonId]) || 0
  }

  addDungeonCount(dungeonId) {
    if (!this._d.daily.dungeonCount) this._d.daily.dungeonCount = {}
    this._d.daily.dungeonCount[dungeonId] = (this._d.daily.dungeonCount[dungeonId] || 0) + 1
    this._save()
  }

  // ===== 每日商店购买记录 =====
  getDailyShopPurchase(itemKey) {
    return (this._d.daily.shopPurchases && this._d.daily.shopPurchases[itemKey]) || 0
  }

  addDailyShopPurchase(itemKey) {
    if (!this._d.daily.shopPurchases) this._d.daily.shopPurchases = {}
    this._d.daily.shopPurchases[itemKey] = (this._d.daily.shopPurchases[itemKey] || 0) + 1
    this._save()
  }

  // ===== 通天塔（保留原版兼容） =====
  updateTowerBestFloor(floor, pets, weapon, totalTurns) {
    if (floor > this._d.tower.bestFloor) {
      this._d.tower.bestFloor = floor
      this._d.stats.bestFloorPets = (pets || []).map(p => ({ name: p.name, attr: p.attr, atk: p.atk }))
      this._d.stats.bestFloorWeapon = weapon ? { name: weapon.name } : null
    }
    if (totalTurns > 0 && (!this._d.stats.bestTotalTurns || totalTurns < this._d.stats.bestTotalTurns)) {
      this._d.stats.bestTotalTurns = totalTurns
    }
    this._save()
  }

  // 兼容旧方法名
  updateBestFloor(floor, pets, weapon, totalTurns) {
    return this.updateTowerBestFloor(floor, pets, weapon, totalTurns)
  }

  // ===== 战斗统计 =====
  recordBattle(combo) {
    this._d.stats.totalBattles++
    this._d.stats.totalCombos += combo
    this._d.stats.maxCombo = Math.max(this._d.stats.maxCombo, combo)
    this._save()
  }

  // ===== 探险等级 =====
  addPlayerExp(amount) {
    this._d.playerExp += amount
    const expTable = [0, 100, 250, 500, 800, 1200, 1700, 2300, 3000, 4000, 5000]
    while (this._d.playerLevel < 99) {
      const needed = expTable[Math.min(this._d.playerLevel, expTable.length - 1)]
        + Math.max(0, this._d.playerLevel - expTable.length + 1) * 1000
      if (this._d.playerExp >= needed) {
        this._d.playerExp -= needed
        this._d.playerLevel++
        // 等级奖励
        this._d.staminaMax = 100 + (this._d.playerLevel - 1) * 2
      } else break
    }
    this._save()
  }

  // ===== 战斗力计算 =====
  calcTeamPower(teamUids) {
    const { getPetById, getPetStarAtk } = require('./pets')
    let power = 0
    for (const uid of (teamUids || [])) {
      const inst = this.getPetByUid(uid)
      if (!inst) continue
      const template = getPetById(inst.id)
      if (!template) continue
      const starAtk = getPetStarAtk({ ...template, star: inst.star })
      const levelBonus = 1 + (inst.level - 1) * 0.03
      power += Math.floor(starAtk * levelBonus * 100)
    }
    return power
  }

  // ===== 设置 =====
  toggleBgm() {
    this._d.settings.bgmOn = !this._d.settings.bgmOn
    this._save()
    return this._d.settings.bgmOn
  }
  toggleSfx() {
    this._d.settings.sfxOn = !this._d.settings.sfxOn
    this._save()
    return this._d.settings.sfxOn
  }

  // ===== 图鉴 =====
  addPetDex(petId) {
    if (!this._d.petDex) this._d.petDex = []
    if (!this._d.petDex.includes(petId)) {
      this._d.petDex.push(petId)
      this._save()
    }
  }
  markDexSeen(petId) {
    if (!this._d.petDexSeen) this._d.petDexSeen = []
    if (!this._d.petDexSeen.includes(petId)) {
      this._d.petDexSeen.push(petId)
      this._save()
    }
  }

  // ===== 通天塔局内暂存（保留用于通天塔模式） =====
  saveRunState(runState) {
    this._d.savedRun = runState
    this._save()
  }
  loadRunState() { return this._d.savedRun || null }
  clearRunState() { delete this._d.savedRun; this._save() }
  hasSavedRun() { return !!this._d.savedRun }

  // ===== 彻底重置 =====
  async resetAll() {
    this._d = defaultPersist()
    try { wx.removeStorageSync(LOCAL_KEY) } catch(e) {}
    try { wx.removeStorageSync(LEGACY_KEY) } catch(e) {}
    this._save()
    if (this._cloudReady && this._openid) {
      try {
        const db = wx.cloud.database()
        const res = await db.collection('playerData').where({ _openid: this._openid }).get()
        if (res.data && res.data.length > 0) {
          await db.collection('playerData').doc(res.data[0]._id).remove()
        }
      } catch(e) { console.warn('[Storage] 云端重置失败:', e) }
    }
    return true
  }

  // ===== 本地存储 =====
  _load() {
    try {
      // 先尝试加载新版存档
      let raw = wx.getStorageSync(LOCAL_KEY)
      if (raw) {
        this._d = JSON.parse(raw)
        this._ensureFields()
        return
      }
      // 尝试迁移旧版存档
      const legacy = wx.getStorageSync(LEGACY_KEY)
      if (legacy) {
        console.log('[Storage] 检测到旧版存档，执行迁移...')
        this._d = defaultPersist()
        const old = JSON.parse(legacy)
        // 迁移数据
        this._d.tower.bestFloor = old.bestFloor || 0
        this._d.stats = { ...this._d.stats, ...(old.stats || {}) }
        this._d.settings = { ...this._d.settings, ...(old.settings || {}) }
        this._d.petDex = old.petDex || []
        this._d.petDexSeen = old.petDexSeen || []
        this._d._migratedFromV1 = true
        this._save()
        console.log('[Storage] 旧版存档迁移完成')
        return
      }
      // 全新存档
      this._d = defaultPersist()
    } catch(e) {
      console.warn('Storage load error:', e)
      this._d = defaultPersist()
    }
  }

  _ensureFields() {
    const def = defaultPersist()
    // 确保顶层字段存在
    for (const k of Object.keys(def)) {
      if (this._d[k] === undefined) this._d[k] = def[k]
    }
    // 确保嵌套对象字段
    if (!this._d.teams) this._d.teams = def.teams
    if (!this._d.stageProgress) this._d.stageProgress = def.stageProgress
    if (!this._d.idle) this._d.idle = def.idle
    if (!this._d.daily) this._d.daily = def.daily
    if (!this._d.tower) this._d.tower = def.tower
    if (!this._d.inventory) this._d.inventory = def.inventory
    // 确保 daily 子字段
    if (!this._d.daily.shopPurchases) this._d.daily.shopPurchases = {}
    if (!this._d.daily.dungeonCount) this._d.daily.dungeonCount = {}
    // 确保 stageProgress 所有区域存在
    for (const area of ['metal','wood','earth','water','fire']) {
      if (!this._d.stageProgress[area]) {
        this._d.stageProgress[area] = { cleared: 0, stars: {} }
      }
    }
    // 确保 inventory 所有字段
    for (const k of Object.keys(def.inventory)) {
      if (this._d.inventory[k] === undefined) this._d.inventory[k] = def.inventory[k]
    }
  }

  _save() {
    try {
      wx.setStorageSync(LOCAL_KEY, JSON.stringify(this._d))
      this._debounceSyncToCloud()
    } catch(e) {
      console.warn('Storage save error:', e)
    }
  }

  _loadUserInfo() {
    try {
      const raw = wx.getStorageSync('wxtower_userinfo')
      if (raw) {
        const info = JSON.parse(raw)
        if (info && info.nickName && info.nickName !== '微信用户' && info.avatarUrl && info.avatarUrl.length > 10) {
          this.userInfo = info
          this.userAuthorized = true
        } else {
          wx.removeStorageSync('wxtower_userinfo')
          this.userInfo = null
          this.userAuthorized = false
        }
      }
    } catch(e) {}
  }

  _saveUserInfo(info) {
    this.userInfo = info
    this.userAuthorized = true
    try { wx.setStorageSync('wxtower_userinfo', JSON.stringify(info)) } catch(e) {}
  }

  // ===== 微信授权（沿用原版） =====
  showUserInfoBtn(rect, callback) {
    this.destroyUserInfoBtn()
    try {
      const btn = wx.createUserInfoButton({
        type: 'text', text: '',
        style: {
          left: rect.left, top: rect.top,
          width: rect.width, height: rect.height,
          backgroundColor: 'rgba(0,0,0,0)',
          borderColor: 'rgba(0,0,0,0)',
          borderWidth: 0, borderRadius: 0,
          color: 'rgba(0,0,0,0)',
          fontSize: 1, textAlign: 'center',
          lineHeight: rect.height,
        },
        withCredentials: false,
      })
      this._userInfoBtn = btn
      this._userInfoBtnCallback = callback
      btn.onTap((res) => {
        btn.destroy()
        this._userInfoBtn = null
        const cb = this._userInfoBtnCallback
        this._userInfoBtnCallback = null
        const errMsg = res.errMsg || ''
        if (errMsg.indexOf('no privacy api permission') !== -1 || res.err_code === -12034) {
          if (cb) cb(false, null)
          return
        }
        if (res.userInfo && res.userInfo.nickName && res.userInfo.nickName !== '微信用户') {
          const info = { nickName: res.userInfo.nickName, avatarUrl: res.userInfo.avatarUrl }
          this._saveUserInfo(info)
          if (cb) cb(true, info)
        } else if (res.errMsg && res.errMsg.indexOf('fail') !== -1) {
          this._tryOpenSetting(cb)
        } else {
          if (cb) cb(false, null)
        }
      })
    } catch(e) {
      if (callback) callback(false, null)
    }
  }

  _tryOpenSetting(callback) {
    wx.getSetting({
      success: (settingRes) => {
        if (settingRes.authSetting['scope.userInfo'] === false) {
          wx.showModal({
            title: '授权提示',
            content: '需要获取您的昵称和头像用于排行榜展示，请在设置中开启',
            confirmText: '去设置', cancelText: '暂不',
            success: (modalRes) => {
              if (modalRes.confirm) {
                wx.openSetting({
                  success: (openRes) => {
                    if (openRes.authSetting['scope.userInfo']) {
                      wx.getUserInfo({
                        success: (infoRes) => {
                          if (infoRes.userInfo && infoRes.userInfo.nickName !== '微信用户') {
                            const info = { nickName: infoRes.userInfo.nickName, avatarUrl: infoRes.userInfo.avatarUrl }
                            this._saveUserInfo(info)
                            if (callback) callback(true, info)
                          } else { if (callback) callback(false, null) }
                        },
                        fail: () => { if (callback) callback(false, null) }
                      })
                    } else { if (callback) callback(false, null) }
                  },
                  fail: () => { if (callback) callback(false, null) }
                })
              } else { if (callback) callback(false, null) }
            },
            fail: () => { if (callback) callback(false, null) }
          })
        } else {
          if (callback) callback(false, null)
        }
      },
      fail: () => { if (callback) callback(false, null) }
    })
  }

  updateUserInfoBtnPos(rect) {
    if (!this._userInfoBtn) return
    try {
      this._userInfoBtn.style.left = rect.left
      this._userInfoBtn.style.top = rect.top
      this._userInfoBtn.style.width = rect.width
      this._userInfoBtn.style.height = rect.height
    } catch(e) {}
  }

  destroyUserInfoBtn() {
    if (this._userInfoBtn) {
      try { this._userInfoBtn.destroy() } catch(e) {}
      this._userInfoBtn = null
      this._userInfoBtnCallback = null
    }
  }

  // ===== 排行榜 =====
  async submitScore(floor, pets, weapon, totalTurns) {
    if (!this._cloudReady || !this.userAuthorized) return
    try {
      await wx.cloud.callFunction({
        name: 'ranking',
        data: {
          action: 'submit',
          nickName: this.userInfo.nickName,
          avatarUrl: this.userInfo.avatarUrl,
          floor,
          pets: (pets || []).map(p => ({ name: p.name, attr: p.attr })),
          weapon: weapon ? { name: weapon.name } : null,
          totalTurns: totalTurns || 0,
          petDexCount: (this._d.petDex || []).length,
          maxCombo: this._d.stats.maxCombo || 0,
          teamPower: this.calcTeamPower(this._d.teams.battle),
        }
      })
    } catch(e) { console.warn('[Ranking] 提交失败:', e) }
  }

  async submitDexAndCombo() {
    if (!this._cloudReady || !this.userAuthorized) return
    try {
      await wx.cloud.callFunction({
        name: 'ranking',
        data: {
          action: 'submitDexCombo',
          nickName: this.userInfo.nickName,
          avatarUrl: this.userInfo.avatarUrl,
          petDexCount: (this._d.petDex || []).length,
          maxCombo: this._d.stats.maxCombo || 0,
        }
      })
    } catch(e) {}
  }

  async fetchRanking(tab, force) {
    const now = Date.now()
    const listMap = { all: 'rankAllList', dex: 'rankDexList', combo: 'rankComboList', power: 'rankPowerList' }
    const listKey = listMap[tab] || 'rankAllList'
    if (!force && now - this.rankLastFetch < 30000 && this.rankLastFetchTab === tab && this[listKey].length > 0) return
    if (this.rankLoading) return
    this.rankLoading = true
    try {
      const actionMap = { all: 'getAll', dex: 'getDex', combo: 'getCombo', power: 'getPower' }
      const action = actionMap[tab] || 'getAll'
      const r = await wx.cloud.callFunction({ name: 'ranking', data: { action } })
      if (r.result && r.result.code === 0) {
        this[listKey] = r.result.list || []
        const rankKey = listKey.replace('List', 'MyRank')
        this[rankKey] = r.result.myRank || -1
        this.rankLastFetch = now
        this.rankLastFetchTab = tab
      }
    } catch(e) { console.warn('[Ranking] 拉取失败:', e) }
    this.rankLoading = false
  }

  // ===== 云同步 =====
  _debounceSyncToCloud() {
    if (!this._cloudInitDone) { this._pendingSync = true; return }
    if (this._cloudSyncTimer) clearTimeout(this._cloudSyncTimer)
    this._cloudSyncTimer = setTimeout(() => {
      this._cloudSyncTimer = null
      this._syncToCloud()
    }, 2000)
  }

  async _initCloud() {
    try {
      wx.cloud.init({ env: CLOUD_ENV, traceUser: true })
      this._cloudReady = true
    } catch(e) { console.warn('Cloud init failed:', e); return }
    try { await this._ensureCollections() } catch(e) {}
    try { await this._getOpenid() } catch(e) { console.warn('Get openid failed:', e) }
    if (this._openid) await this._syncFromCloud()
    this._cloudInitDone = true
    if (this._pendingSync) { this._pendingSync = false; this._syncToCloud() }
  }

  async _ensureCollections() {
    const r = await wx.cloud.callFunction({ name: 'initCollections' })
    if (r.result && r.result.errors && r.result.errors.length) {
      console.warn('创建集合异常:', r.result.errors)
    }
  }

  async _getOpenid() {
    const r = await wx.cloud.callFunction({ name: 'getOpenid' })
    this._openid = (r.result && r.result.openid) || ''
  }

  async _syncFromCloud() {
    if (!this._cloudReady || !this._openid) return
    try {
      const db = wx.cloud.database()
      const res = await db.collection('playerData').where({ _openid: this._openid }).get()
      if (res.data && res.data.length > 0) {
        const cloud = res.data[0]
        const cloudTime = cloud._updateTime || 0
        const localTime = this._d._updateTime || 0
        if (cloudTime > localTime) {
          delete cloud._id; delete cloud._openid
          Object.assign(this._d, cloud)
          this._ensureFields()
          wx.setStorageSync(LOCAL_KEY, JSON.stringify(this._d))
        }
      }
    } catch(e) { console.warn('Sync from cloud error:', e) }
  }

  async _syncToCloud() {
    if (!this._cloudReady || !this._openid) return
    try {
      const db = wx.cloud.database()
      const col = db.collection('playerData')
      const res = await col.where({ _openid: this._openid }).get()
      const saveData = { ...this._d, _updateTime: Date.now() }
      delete saveData._id; delete saveData._openid
      if (res.data && res.data.length > 0) {
        await col.doc(res.data[0]._id).update({ data: saveData })
      } else {
        await col.add({ data: saveData })
      }
    } catch(e) { console.warn('[Storage] 云同步失败:', e.message || e) }
  }
}

module.exports = Storage
