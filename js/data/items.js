/**
 * 道具系统 — 灵宠放置传
 * 灵珠、经验珠、素材等道具定义
 */

// ===== 灵珠（捕捉道具） =====
const CAPTURE_BALLS = {
  normalBall: {
    id: 'normalBall', name: '普通灵珠', desc: '基础捕捉道具',
    baseRate: 0.20,   // 基础捕捉率 20%
    rarity: 'normal',
    icon: 'assets/ui/ball_normal.png',
    shopPrice: 100,   // 金币购买价格
  },
  superBall: {
    id: 'superBall', name: '高级灵珠', desc: '较高成功率的捕捉道具',
    baseRate: 0.45,
    rarity: 'rare',
    icon: 'assets/ui/ball_super.png',
    shopPrice: 500,
  },
  masterBall: {
    id: 'masterBall', name: '大师灵珠', desc: '极高成功率的捕捉道具',
    baseRate: 0.75,
    rarity: 'epic',
    icon: 'assets/ui/ball_master.png',
    shopPrice: null,   // 不可金币购买，只能通过灵石或特殊途径
    gemPrice: 10,
  },
  ultraBall: {
    id: 'ultraBall', name: '五行灵珠', desc: '必定捕捉成功',
    baseRate: 1.0,
    rarity: 'legendary',
    icon: 'assets/ui/ball_ultra.png',
    shopPrice: null,
    gemPrice: null,     // 成就/活动专属
  },
}

// ===== 经验道具 =====
const EXP_ITEMS = {
  expOrb_s: {
    id: 'expOrb_s', name: '小经验珠', desc: '提供100点宠物经验',
    expValue: 100,
    rarity: 'normal',
  },
  expOrb_m: {
    id: 'expOrb_m', name: '中经验珠', desc: '提供500点宠物经验',
    expValue: 500,
    rarity: 'rare',
  },
  expOrb_l: {
    id: 'expOrb_l', name: '大经验珠', desc: '提供2000点宠物经验',
    expValue: 2000,
    rarity: 'epic',
  },
}

// ===== 捕捉率计算 =====
/**
 * 计算实际捕捉率
 * 基于灵珠 + stages.js 中的稀有度/星级基础概率
 * @param {string} ballType - 灵珠类型 key
 * @param {object} enemy - 敌方数据 { hp, maxHp, attr, rarity, star, isBoss, isElite }
 * @param {string} teamAttr - 队伍主属性（用于克制加成）
 * @returns {number} 0~1 的捕捉率
 */
function calcCaptureRate(ballType, enemy, teamAttr) {
  const ball = CAPTURE_BALLS[ballType]
  if (!ball) return 0

  // 基础概率：来自 stages.js 的稀有度/星级配置
  const { getBaseCaptureRate } = require('./stages')
  let rate = getBaseCaptureRate(enemy.rarity || 'R', enemy.star || 1)

  // 灵珠倍率
  rate *= (ball.baseRate / 0.20)  // 以普通灵珠0.20为基准倍率

  // 血量越低捕捉率越高：(1 + (1 - 剩余血量比) × 0.5)
  const hpRatio = enemy.hp / enemy.maxHp
  rate *= (1 + (1 - hpRatio) * 0.5)

  // 属性克制加成 +20%
  const { getCounterMap } = require('./tower')
  if (teamAttr && getCounterMap(enemy.attr)[teamAttr] === enemy.attr) {
    rate *= 1.2
  }

  // BOSS/精英惩罚（已在基础概率中体现，此处不再额外惩罚）

  return Math.min(1, Math.max(0, rate))
}

// ===== 商店定义 =====
const SHOP_ITEMS_DAILY = [
  { id: 'shop_ball1',  name: '普通灵珠×3', desc: '购买3个普通灵珠', cost: { gold: 250 },  give: { normalBall: 3 } },
  { id: 'shop_ball2',  name: '高级灵珠×1', desc: '购买1个高级灵珠', cost: { gold: 800 },  give: { superBall: 1 } },
  { id: 'shop_exp1',   name: '小经验珠×5', desc: '购买5个小经验珠', cost: { gold: 400 },  give: { expOrb_s: 5 } },
  { id: 'shop_exp2',   name: '中经验珠×2', desc: '购买2个中经验珠', cost: { gold: 600 },  give: { expOrb_m: 2 } },
  { id: 'shop_stam',   name: '体力药剂',   desc: '回复30点体力',   cost: { gold: 300 },  give: { stamina: 30 }, dailyLimit: 3 },
]

const SHOP_ITEMS_GEM = [
  { id: 'gem_ball1',   name: '大师灵珠×1', desc: '极高捕捉率灵珠', cost: { gem: 10 },   give: { masterBall: 1 } },
  { id: 'gem_ball2',   name: '高级灵珠×5', desc: '一组高级灵珠',   cost: { gem: 15 },   give: { superBall: 5 } },
  { id: 'gem_exp1',    name: '大经验珠×1', desc: '海量宠物经验',   cost: { gem: 8 },    give: { expOrb_l: 1 } },
  { id: 'gem_stam',    name: '体力恢复满', desc: '体力恢复至上限', cost: { gem: 5 },    give: { staminaFull: true } },
]

module.exports = {
  CAPTURE_BALLS,
  EXP_ITEMS,
  SHOP_ITEMS_DAILY,
  SHOP_ITEMS_GEM,
  calcCaptureRate,
}
