/**
 * 关卡系统 — 灵宠放置传（v3 重制版）
 * 7大区域 × 15关 = 105关
 * 每个区域对应一个种族，敌人均为该种族的基础捕捉宠
 * 敌人有等级和星级概念，由易到难
 * 捕捉的宠物等级和星级与怪物一致
 * 击杀掉落为1星1级宠
 */

const {
  ATTRS, ATTR_NAME,
  ENEMY_SKILLS,
} = require('./tower')

// ===== 103只基础捕捉宠数据（按种族分组） =====
// 每只宠物: { petId, name, rarity, attr, race }
// rarity: 'R'(幼兽) / 'SR'(灵兽) / 'SSR'(神兽)

const BASE_PETS = {
  // === 兽灵族（16只） ===
  beast: [
    { petId: 'flame_fox',         name: '炎狐',     rarity: 'R',   attr: 'fire',    race: 'beast' },
    { petId: 'brook_otter',       name: '溪獭',     rarity: 'R',   attr: 'water',   race: 'beast' },
    { petId: 'leaf_deer',         name: '叶鹿',     rarity: 'R',   attr: 'grass',   race: 'beast' },
    { petId: 'rock_badger',       name: '岩獾',     rarity: 'R',   attr: 'earth',   race: 'beast' },
    { petId: 'gale_weasel',       name: '风鼬',     rarity: 'R',   attr: 'wind',    race: 'beast' },
    { petId: 'thunder_marten',    name: '雷貂',     rarity: 'R',   attr: 'thunder', race: 'beast' },
    { petId: 'thorn_hedgehog',    name: '刺猬',     rarity: 'R',   attr: 'grass',   race: 'beast' },
    { petId: 'crimson_wolf',      name: '赤狼',     rarity: 'R',   attr: 'fire',    race: 'beast' },
    { petId: 'iron_armadillo',    name: '铁甲犰狳', rarity: 'R',   attr: 'earth',   race: 'beast' },
    { petId: 'cloud_leopard',     name: '云豹',     rarity: 'R',   attr: 'wind',    race: 'beast' },
    { petId: 'blaze_lion',        name: '焰狮',     rarity: 'SR',  attr: 'fire',    race: 'beast' },
    { petId: 'frost_raccoon',     name: '冰貉',     rarity: 'SR',  attr: 'water',   race: 'beast' },
    { petId: 'jade_lizard',       name: '翠蜥',     rarity: 'SR',  attr: 'grass',   race: 'beast' },
    { petId: 'boulder_ox',        name: '磐牛',     rarity: 'SR',  attr: 'earth',   race: 'beast' },
    { petId: 'storm_tiger',       name: '雷虎',     rarity: 'SR',  attr: 'thunder', race: 'beast' },
    { petId: 'spirit_qilin',      name: '灵麒',     rarity: 'SSR', attr: 'heart',   race: 'beast' },
  ],
  // === 羽翼族（15只） ===
  wing: [
    { petId: 'vermilion_chick',   name: '朱雀雏',   rarity: 'R',   attr: 'fire',    race: 'wing' },
    { petId: 'wind_falcon',       name: '风隼',     rarity: 'R',   attr: 'wind',    race: 'wing' },
    { petId: 'storm_petrel',      name: '海燕',     rarity: 'R',   attr: 'water',   race: 'wing' },
    { petId: 'blossom_butterfly', name: '花蝶',     rarity: 'R',   attr: 'grass',   race: 'wing' },
    { petId: 'bolt_eagle',        name: '雷鹰',     rarity: 'R',   attr: 'thunder', race: 'wing' },
    { petId: 'dusk_bat',          name: '暮蝠',     rarity: 'R',   attr: 'shadow',  race: 'wing' },
    { petId: 'glow_moth',         name: '萤蛾',     rarity: 'R',   attr: 'light',   race: 'wing' },
    { petId: 'bamboo_sparrow',    name: '竹雀',     rarity: 'R',   attr: 'grass',   race: 'wing' },
    { petId: 'sand_owl',          name: '砂鸮',     rarity: 'R',   attr: 'earth',   race: 'wing' },
    { petId: 'ice_gull',          name: '冰鸥',     rarity: 'R',   attr: 'water',   race: 'wing' },
    { petId: 'ember_crane',       name: '焰鹤',     rarity: 'SR',  attr: 'fire',    race: 'wing' },
    { petId: 'shadow_raven',      name: '影鸦',     rarity: 'SR',  attr: 'shadow',  race: 'wing' },
    { petId: 'breeze_phoenix',    name: '风凤雏',   rarity: 'SR',  attr: 'wind',    race: 'wing' },
    { petId: 'thunder_roc',       name: '雷翎鹏',   rarity: 'SR',  attr: 'thunder', race: 'wing' },
    { petId: 'aurora_wing',       name: '极光翼',   rarity: 'SSR', attr: 'light',   race: 'wing' },
  ],
  // === 水族（15只） ===
  aqua: [
    { petId: 'bubble_fish',       name: '泡泡鱼',   rarity: 'R',   attr: 'water',   race: 'aqua' },
    { petId: 'stone_turtle',      name: '岩龟',     rarity: 'R',   attr: 'earth',   race: 'aqua' },
    { petId: 'flame_shrimp',      name: '火虾',     rarity: 'R',   attr: 'fire',    race: 'aqua' },
    { petId: 'ink_octopus',       name: '墨章',     rarity: 'R',   attr: 'shadow',  race: 'aqua' },
    { petId: 'jelly_spirit',      name: '水母灵',   rarity: 'R',   attr: 'water',   race: 'aqua' },
    { petId: 'spark_frog',        name: '雷蛙',     rarity: 'R',   attr: 'thunder', race: 'aqua' },
    { petId: 'coral_crab',        name: '珊瑚蟹',   rarity: 'R',   attr: 'grass',   race: 'aqua' },
    { petId: 'lantern_fish',      name: '灯笼鱼',   rarity: 'R',   attr: 'fire',    race: 'aqua' },
    { petId: 'frost_clam',        name: '寒蛤',     rarity: 'R',   attr: 'water',   race: 'aqua' },
    { petId: 'surf_seahorse',     name: '浪花海马', rarity: 'R',   attr: 'wind',    race: 'aqua' },
    { petId: 'tide_whale',        name: '碧潮鲸',   rarity: 'SR',  attr: 'water',   race: 'aqua' },
    { petId: 'obsidian_turtle',   name: '玄甲龟',   rarity: 'SR',  attr: 'earth',   race: 'aqua' },
    { petId: 'abyss_eel',         name: '深渊鳗',   rarity: 'SR',  attr: 'shadow',  race: 'aqua' },
    { petId: 'thunder_frog',      name: '雷纹蛙',   rarity: 'SR',  attr: 'thunder', race: 'aqua' },
    { petId: 'stardragon_fish',   name: '星海龙鱼', rarity: 'SSR', attr: 'light',   race: 'aqua' },
  ],
  // === 植灵族（15只） ===
  flora: [
    { petId: 'little_mushroom',   name: '小蘑菇',   rarity: 'R',   attr: 'grass',   race: 'flora' },
    { petId: 'dandelion_spirit',  name: '蒲公英',   rarity: 'R',   attr: 'wind',    race: 'flora' },
    { petId: 'fire_lotus',        name: '火莲',     rarity: 'R',   attr: 'fire',    race: 'flora' },
    { petId: 'vine_child',        name: '藤蔓童',   rarity: 'R',   attr: 'grass',   race: 'flora' },
    { petId: 'cactus_ball',       name: '仙人球',   rarity: 'R',   attr: 'earth',   race: 'flora' },
    { petId: 'bamboo_spirit',     name: '竹灵',     rarity: 'R',   attr: 'wind',    race: 'flora' },
    { petId: 'crystal_bloom',     name: '晶花',     rarity: 'R',   attr: 'earth',   race: 'flora' },
    { petId: 'maple_sprite',      name: '枫叶精',   rarity: 'R',   attr: 'fire',    race: 'flora' },
    { petId: 'moss_orb',          name: '苔球',     rarity: 'R',   attr: 'grass',   race: 'flora' },
    { petId: 'night_orchid',      name: '夜兰',     rarity: 'R',   attr: 'shadow',  race: 'flora' },
    { petId: 'banyan_elder',      name: '古榕精',   rarity: 'SR',  attr: 'grass',   race: 'flora' },
    { petId: 'blaze_crystal_lotus', name: '焰晶莲', rarity: 'SR',  attr: 'fire',    race: 'flora' },
    { petId: 'thunder_bamboo',    name: '雷竹翁',   rarity: 'SR',  attr: 'thunder', race: 'flora' },
    { petId: 'stone_mushroom_king', name: '岩菇王', rarity: 'SR',  attr: 'earth',   race: 'flora' },
    { petId: 'heart_blossom',     name: '心蕊花',   rarity: 'SSR', attr: 'heart',   race: 'flora' },
  ],
  // === 元素族（15只） ===
  element: [
    { petId: 'fire_wisp',         name: '火灵',     rarity: 'R',   attr: 'fire',    race: 'element' },
    { petId: 'water_wisp',        name: '水灵',     rarity: 'R',   attr: 'water',   race: 'element' },
    { petId: 'grass_wisp',        name: '草灵',     rarity: 'R',   attr: 'grass',   race: 'element' },
    { petId: 'thunder_wisp',      name: '雷灵',     rarity: 'R',   attr: 'thunder', race: 'element' },
    { petId: 'earth_wisp',        name: '土灵',     rarity: 'R',   attr: 'earth',   race: 'element' },
    { petId: 'wind_wisp',         name: '风灵',     rarity: 'R',   attr: 'wind',    race: 'element' },
    { petId: 'fire_elemental',    name: '火精灵',   rarity: 'SR',  attr: 'fire',    race: 'element' },
    { petId: 'water_elemental',   name: '水精灵',   rarity: 'SR',  attr: 'water',   race: 'element' },
    { petId: 'grass_elemental',   name: '草精灵',   rarity: 'SR',  attr: 'grass',   race: 'element' },
    { petId: 'thunder_elemental', name: '雷精灵',   rarity: 'SR',  attr: 'thunder', race: 'element' },
    { petId: 'light_elemental',   name: '光精灵',   rarity: 'SR',  attr: 'light',   race: 'element' },
    { petId: 'shadow_elemental',  name: '影精灵',   rarity: 'SR',  attr: 'shadow',  race: 'element' },
    { petId: 'rock_elemental',    name: '岩精灵',   rarity: 'SR',  attr: 'earth',   race: 'element' },
    { petId: 'wind_elemental',    name: '风精灵',   rarity: 'SR',  attr: 'wind',    race: 'element' },
    { petId: 'chaos_spirit',      name: '混沌灵',   rarity: 'SSR', attr: 'light',   race: 'element' },
  ],
  // === 幻灵族（13只） ===
  phantom: [
    { petId: 'stardust_wisp',     name: '星尘灵',   rarity: 'R',   attr: 'light',   race: 'phantom' },
    { petId: 'dark_wraith',       name: '暗魂灵',   rarity: 'R',   attr: 'shadow',  race: 'phantom' },
    { petId: 'dream_tapir',       name: '睡梦貘',   rarity: 'R',   attr: 'heart',   race: 'phantom' },
    { petId: 'moonbeam_spirit',   name: '月光灵',   rarity: 'R',   attr: 'light',   race: 'phantom' },
    { petId: 'shade_devourer',    name: '噬影魔',   rarity: 'R',   attr: 'shadow',  race: 'phantom' },
    { petId: 'emotion_sprite',    name: '心绪灵',   rarity: 'R',   attr: 'heart',   race: 'phantom' },
    { petId: 'mirror_spirit',     name: '镜像灵',   rarity: 'R',   attr: 'light',   race: 'phantom' },
    { petId: 'galaxy_spirit',     name: '星河灵',   rarity: 'SR',  attr: 'light',   race: 'phantom' },
    { petId: 'nether_spirit',     name: '幽冥灵',   rarity: 'SR',  attr: 'shadow',  race: 'phantom' },
    { petId: 'psyche_spirit',     name: '心络灵',   rarity: 'SR',  attr: 'heart',   race: 'phantom' },
    { petId: 'divine_illusion',   name: '圣幻灵',   rarity: 'SSR', attr: 'light',   race: 'phantom' },
    { petId: 'myriad_spirit',     name: '万象灵',   rarity: 'SSR', attr: 'heart',   race: 'phantom' },
    { petId: 'realm_master',      name: '幻界主',   rarity: 'SSR', attr: 'light',   race: 'phantom' },
  ],
  // === 龙族（14只） ===
  dragon: [
    { petId: 'fire_dragonling',   name: '火龙崽',   rarity: 'R',   attr: 'fire',    race: 'dragon' },
    { petId: 'water_serpent',     name: '水蛟',     rarity: 'R',   attr: 'water',   race: 'dragon' },
    { petId: 'rock_drake',        name: '岩蜥龙',   rarity: 'R',   attr: 'earth',   race: 'dragon' },
    { petId: 'wind_wyvern',       name: '翼龙崽',   rarity: 'R',   attr: 'wind',    race: 'dragon' },
    { petId: 'spark_ceratops',    name: '雷角龙',   rarity: 'R',   attr: 'thunder', race: 'dragon' },
    { petId: 'flora_lindworm',    name: '花蛇龙',   rarity: 'R',   attr: 'grass',   race: 'dragon' },
    { petId: 'gale_pteranodon',   name: '风翼龙',   rarity: 'R',   attr: 'wind',    race: 'dragon' },
    { petId: 'shadow_dragon',     name: '影龙',     rarity: 'SR',  attr: 'shadow',  race: 'dragon' },
    { petId: 'radiant_dragon',    name: '光龙',     rarity: 'SR',  attr: 'light',   race: 'dragon' },
    { petId: 'ocean_dragon',      name: '海龙',     rarity: 'SR',  attr: 'water',   race: 'dragon' },
    { petId: 'ironscale_dragon',  name: '岩甲龙',   rarity: 'SR',  attr: 'earth',   race: 'dragon' },
    { petId: 'heart_dragon',      name: '心纹龙',   rarity: 'SSR', attr: 'heart',   race: 'dragon' },
    { petId: 'inferno_ancient',   name: '炽焰古龙', rarity: 'SSR', attr: 'fire',    race: 'dragon' },
    { petId: 'cosmos_dragon',     name: '万象龙神', rarity: 'SSR', attr: 'light',   race: 'dragon' },
  ],
}

// ===== 区域定义（7大区域，对应7大种族） =====
const AREAS = {
  beast: {
    id: 'beast', name: '灵兽荒原', desc: '广袤荒原上灵兽奔走的原始大地',
    race: 'beast', difficulty: 1,
    bgPath: 'assets/battle/battle_earth.jpg',
    mapBgPath: 'assets/backgrounds/home_bg.jpg',
    stageCount: 16,   // 兽灵族16只基础宠 = 16关
    staminaCost: 5,
    unlockCondition: null,  // 初始解锁
  },
  wing: {
    id: 'wing', name: '苍穹群岛', desc: '浮于云端的空岛群落，羽翼族的栖息地',
    race: 'wing', difficulty: 2,
    bgPath: 'assets/battle/battle_metal.jpg',
    mapBgPath: 'assets/backgrounds/home_bg.jpg',
    stageCount: 15,
    staminaCost: 5,
    unlockCondition: { area: 'beast', stage: 8 },
  },
  aqua: {
    id: 'aqua', name: '深海龙宫', desc: '海底幽深处的水族古国',
    race: 'aqua', difficulty: 3,
    bgPath: 'assets/battle/battle_water.jpg',
    mapBgPath: 'assets/backgrounds/home_bg.jpg',
    stageCount: 15,
    staminaCost: 6,
    unlockCondition: { area: 'wing', stage: 8 },
  },
  flora: {
    id: 'flora', name: '万灵古林', desc: '千年古木参天的灵植秘境',
    race: 'flora', difficulty: 3,
    bgPath: 'assets/battle/battle_wood.jpg',
    mapBgPath: 'assets/backgrounds/home_bg.jpg',
    stageCount: 15,
    staminaCost: 6,
    unlockCondition: { area: 'aqua', stage: 8 },
  },
  element: {
    id: 'element', name: '元素熔炉', desc: '九种元素交汇碰撞的混沌之地',
    race: 'element', difficulty: 4,
    bgPath: 'assets/battle/battle_fire.jpg',
    mapBgPath: 'assets/backgrounds/home_bg.jpg',
    stageCount: 15,
    staminaCost: 7,
    unlockCondition: { area: 'flora', stage: 8 },
  },
  phantom: {
    id: 'phantom', name: '幻梦深渊', desc: '现实与幻境交错的迷幻空间',
    race: 'phantom', difficulty: 5,
    bgPath: 'assets/battle/battle_metal.jpg',
    mapBgPath: 'assets/backgrounds/home_bg.jpg',
    stageCount: 13,  // 幻灵族13只
    staminaCost: 8,
    unlockCondition: { area: 'element', stage: 8 },
  },
  dragon: {
    id: 'dragon', name: '龙脊山脉', desc: '传说中龙族沉睡的神山禁地',
    race: 'dragon', difficulty: 6,
    bgPath: 'assets/battle/battle_fire.jpg',
    mapBgPath: 'assets/backgrounds/home_bg.jpg',
    stageCount: 14,  // 龙族14只
    staminaCost: 10,
    unlockCondition: { area: 'phantom', stage: 8 },
  },
}

// 区域解锁顺序
const AREA_ORDER = ['beast', 'wing', 'aqua', 'flora', 'element', 'phantom', 'dragon']

// ===== 敌人等级 & 星级配置 =====
// 每个区域内，关卡号 → 敌人等级和星级
// 规则：R级宠 ★1-★2，SR级宠 ★1-★3，SSR级宠 ★2-★4
// 同区域内难度递增

/**
 * 根据区域和关卡号计算敌人等级和星级
 * @param {string} area - 区域ID
 * @param {number} stageNum - 关卡号（1-based）
 * @param {string} rarity - 宠物稀有度 'R'/'SR'/'SSR'
 * @returns {{ level: number, star: number }}
 */
function getEnemyLevelAndStar(area, stageNum, rarity) {
  const areaIdx = AREA_ORDER.indexOf(area)
  const areaData = AREAS[area]
  const totalStages = areaData.stageCount

  // 区域基础等级偏移（后面区域基础等级更高）
  const areaBaseLv = [1, 8, 18, 28, 40, 55, 70][areaIdx] || 1

  // 关卡内等级递增
  const stageProgress = (stageNum - 1) / Math.max(1, totalStages - 1)
  const areaLvRange = [12, 15, 18, 20, 22, 20, 30][areaIdx] || 15
  const level = Math.floor(areaBaseLv + stageProgress * areaLvRange)

  // 星级：取决于稀有度和关卡位置
  let star = 1
  if (rarity === 'R') {
    // R级宠：前60%为★1，后40%为★2
    if (stageProgress > 0.6) star = 2
  } else if (rarity === 'SR') {
    // SR级宠：通常出现在中后段，★1-★3
    if (stageProgress > 0.85) star = 3
    else if (stageProgress > 0.5) star = 2
  } else if (rarity === 'SSR') {
    // SSR级宠：出现在最后，★2-★4
    if (areaIdx >= 5) star = 3  // 幻灵/龙族SSR起步★3
    else star = 2
    // 最终区域最后boss级SSR
    if (areaIdx >= 6 && stageProgress > 0.9) star = 4
  }

  return { level: Math.max(1, Math.min(100, level)), star }
}

// ===== 基础属性公式（与宠物系统一致） =====
// baseAtk 由稀有度决定，star和level影响最终值
const RARITY_BASE_ATK = { R: 8, SR: 12, SSR: 16 }
const STAR_ATK_MUL = 1.3  // 每升1星ATK倍率

function calcEnemyStats(rarity, level, star) {
  const baseAtk = RARITY_BASE_ATK[rarity] || 8
  const starMul = Math.pow(STAR_ATK_MUL, star - 1)
  const levelMul = 1 + (level - 1) * 0.03
  const atk = Math.floor(baseAtk * starMul * levelMul)
  const hp = atk * 12
  const def = Math.floor(atk * 0.35)
  return { hp, maxHp: hp, atk, def }
}

// ===== 敌人技能分配 =====
// 根据稀有度和星级决定技能数量和类型
function getEnemySkills(rarity, star, stageNum) {
  const skills = []
  const lightPool = ['convert', 'aoe']
  const pool1 = ['poison', 'seal', 'convert']
  const pool2 = ['atkBuff', 'defDown', 'healBlock']
  const elitePool = ['stun', 'selfHeal', 'breakBead', 'eliteSealRow']

  if (rarity === 'R') {
    if (star <= 1) {
      skills.push(_pick(lightPool))
    } else {
      skills.push(_pick(pool1))
    }
  } else if (rarity === 'SR') {
    skills.push(_pick(pool1))
    if (star >= 2) skills.push(_pick(pool2))
    if (star >= 3) skills.push(_pick(elitePool))
  } else if (rarity === 'SSR') {
    // SSR视为BOSS级，技能更丰富
    skills.push(_pick(pool1))
    skills.push(_pick(pool2))
    if (star >= 3) skills.push(_pick(elitePool))
    if (star >= 4) skills.push(_pick(['stun', 'eliteSealRow', 'eliteSealAttr']))
  }

  return skills
}

// ===== 捕捉概率 =====
// 基于稀有度和星级的捕捉基础概率（使用灵珠前的基础值）
const CAPTURE_BASE_RATE = {
  R:   { 1: 0.30, 2: 0.20, 3: 0.12, 4: 0.08 },
  SR:  { 1: 0.18, 2: 0.12, 3: 0.08, 4: 0.05 },
  SSR: { 1: 0.10, 2: 0.06, 3: 0.03, 4: 0.01 },
}

function getBaseCaptureRate(rarity, star) {
  const rates = CAPTURE_BASE_RATE[rarity] || CAPTURE_BASE_RATE.R
  return rates[star] || rates[1]
}

// ===== 击杀掉落概率 =====
// 击杀怪物有几率掉落同种宠物（1星1级）
const DROP_RATE = {
  R:   0.15,   // R级怪15%掉落
  SR:  0.08,   // SR级怪8%掉落
  SSR: 0.03,   // SSR级怪3%掉落
}

// ===== 工具函数 =====
function _lerp(a, b, t) { return a + (b - a) * t }
function _rand(min, max) { return Math.floor(Math.random() * (max - min + 1)) + min }
function _pick(arr) { return arr[Math.floor(Math.random() * arr.length)] }

// ===== 关卡数据生成 =====

/**
 * 生成指定关卡的怪物波次
 * @param {string} area - 区域ID
 * @param {number} stageNum - 关卡号 1-N
 * @returns {object} { waves, staminaCost, rewards, ... }
 */
function generateStageData(area, stageNum) {
  const areaData = AREAS[area]
  if (!areaData) throw new Error('Invalid area: ' + area)

  const race = areaData.race
  const petList = BASE_PETS[race]
  if (!petList || stageNum < 1 || stageNum > petList.length) {
    throw new Error('Invalid stage: ' + area + ' #' + stageNum)
  }

  // 本关的目标宠物（固定，每关对应该种族的第N只基础宠）
  const targetPet = petList[stageNum - 1]
  const { level, star } = getEnemyLevelAndStar(area, stageNum, targetPet.rarity)
  const stats = calcEnemyStats(targetPet.rarity, level, star)
  const skills = getEnemySkills(targetPet.rarity, star, stageNum)

  // 判断BOSS/精英
  const isBoss = targetPet.rarity === 'SSR'
  const isElite = targetPet.rarity === 'SR'

  // BOSS/精英的血量和攻击加成
  let hpMul = 1, atkMul = 1
  if (isBoss) {
    hpMul = 2.5 + (star - 1) * 0.5
    atkMul = 1.5 + (star - 1) * 0.2
  } else if (isElite) {
    hpMul = 1.8 + (star - 1) * 0.3
    atkMul = 1.3 + (star - 1) * 0.15
  }

  const finalHp = Math.round(stats.hp * hpMul)
  const finalAtk = Math.round(stats.atk * atkMul)
  const finalDef = Math.round(stats.def * (isBoss ? 1.5 : isElite ? 1.2 : 1))

  // 构建敌人数据
  const enemy = {
    name: targetPet.name,
    attr: targetPet.attr,
    hp: finalHp,
    maxHp: finalHp,
    atk: finalAtk,
    def: finalDef,
    skills,
    petId: targetPet.petId,
    rarity: targetPet.rarity,
    level,
    star,
    isBoss,
    isElite,
    avatar: `pets/pet_${targetPet.petId}`,   // 头像 pet_{id}.jpg
    fullImg: `pets/pet_${targetPet.petId}_full`,  // 全身图 pet_{id}_full.png
  }

  // 波次：R级1波，SR级1-2波（可能有小怪前置），SSR级2-3波
  const waves = []
  if (isBoss) {
    // SSR BOSS关：先出1-2波同区域R级小怪，最后一波出BOSS
    const preWaveCount = _rand(1, 2)
    for (let w = 0; w < preWaveCount; w++) {
      const rPets = petList.filter(p => p.rarity === 'R')
      const minion = _pick(rPets)
      const mLvStar = getEnemyLevelAndStar(area, Math.max(1, stageNum - 3), minion.rarity)
      const mStats = calcEnemyStats(minion.rarity, mLvStar.level, mLvStar.star)
      waves.push({
        enemies: [{
          name: minion.name,
          attr: minion.attr,
          hp: mStats.hp, maxHp: mStats.hp,
          atk: mStats.atk, def: mStats.def,
          skills: getEnemySkills(minion.rarity, mLvStar.star, stageNum - 3),
          petId: minion.petId,
          rarity: minion.rarity,
          level: mLvStar.level,
          star: mLvStar.star,
          avatar: `pets/pet_${minion.petId}`,
          fullImg: `pets/pet_${minion.petId}_full`,
        }]
      })
    }
    waves.push({ enemies: [enemy] })
  } else if (isElite) {
    // SR精英关：可能有1波R级前置
    if (Math.random() < 0.5) {
      const rPets = petList.filter(p => p.rarity === 'R')
      if (rPets.length > 0) {
        const minion = _pick(rPets)
        const mLvStar = getEnemyLevelAndStar(area, Math.max(1, stageNum - 2), minion.rarity)
        const mStats = calcEnemyStats(minion.rarity, mLvStar.level, mLvStar.star)
        waves.push({
          enemies: [{
            name: minion.name,
            attr: minion.attr,
            hp: mStats.hp, maxHp: mStats.hp,
            atk: mStats.atk, def: mStats.def,
            skills: getEnemySkills(minion.rarity, mLvStar.star, stageNum - 2),
            petId: minion.petId,
            rarity: minion.rarity,
            level: mLvStar.level,
            star: mLvStar.star,
            avatar: `pets/pet_${minion.petId}`,
            fullImg: `pets/pet_${minion.petId}_full`,
          }]
        })
      }
    }
    waves.push({ enemies: [enemy] })
  } else {
    // 普通R级关：1波
    waves.push({ enemies: [enemy] })
  }

  // 首通奖励
  const firstClearRewards = _calcFirstClearRewards(area, stageNum, isBoss, isElite)

  // 重复通关奖励
  const areaIdx = AREA_ORDER.indexOf(area)
  const repeatRewards = {
    exp: 20 + stageNum * 5 + areaIdx * 15,
    gold: 10 + stageNum * 3 + areaIdx * 8,
    petDropRate: DROP_RATE[targetPet.rarity] || 0.15,
  }

  // 星级目标
  const star3Turns = isBoss ? (10 + stageNum) : isElite ? (8 + stageNum) : (5 + Math.floor(stageNum / 2))
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
    targetPet,   // 本关目标宠物信息（用于UI展示）
  }
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
    rewards.gold += 300
    rewards.gem += 8
    rewards.superBall += 2
  } else if (isElite) {
    rewards.gold += 150
    rewards.gem += 3
    rewards.normalBall += 3
    rewards.superBall += 1
  } else if (stageNum % 3 === 0) {
    rewards.normalBall += 2
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
  if (!areaData.unlockCondition) return true
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
    available: 'daily',
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
    available: [2, 4, 6],
    generateRewards: (level) => ({
      normalBall: 2 + Math.floor(level / 3),
      superBall: level >= 10 ? 1 : 0,
    }),
  },
}

module.exports = {
  AREAS,
  AREA_ORDER,
  BASE_PETS,
  RARITY_BASE_ATK,
  DAILY_DUNGEONS,
  CAPTURE_BASE_RATE,
  DROP_RATE,
  generateStageData,
  getEnemyLevelAndStar,
  calcEnemyStats,
  getBaseCaptureRate,
  isAreaUnlocked,
  getAvailableAreas,
}
