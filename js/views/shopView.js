/**
 * 商店视图 — 灵宠放置传 (Phase 6)
 * 金币商品 + 灵石商品 + 每日限购
 */
const V = require('./env')
const { SHOP_ITEMS_DAILY, SHOP_ITEMS_GEM } = require('../data/items')

let _tab = 'daily'  // 'daily' | 'gem'
let _scrollY = 0
let _purchaseResult = null  // { success, msg }

function rShopView(g) {
  const { ctx, R, TH, W, H, S, safeTop } = V

  ctx.fillStyle = '#0d0d1a'; ctx.fillRect(0, 0, W, H)

  const topY = safeTop
  const topH = 42*S
  ctx.fillStyle = 'rgba(0,0,0,0.7)'; ctx.fillRect(0, topY, W, topH)

  // 返回
  g._shopBackBtn = [8*S, topY+6*S, 56*S, 30*S]
  ctx.fillStyle = 'rgba(255,255,255,0.15)'
  R.roundRect(...g._shopBackBtn, 6*S); ctx.fill()
  ctx.fillStyle = '#fff'; ctx.font = `${12*S}px "PingFang SC",sans-serif`
  ctx.textAlign = 'center'
  ctx.fillText('← 返回', g._shopBackBtn[0]+g._shopBackBtn[2]/2, topY+25*S)

  ctx.fillStyle = '#f5d76e'; ctx.font = `bold ${16*S}px "PingFang SC",sans-serif`
  ctx.fillText('商店', W/2, topY+28*S)

  // 货币显示
  ctx.textAlign = 'right'; ctx.fillStyle = '#ffd700'; ctx.font = `${11*S}px "PingFang SC",sans-serif`
  ctx.fillText(`💰${g.storage.gold}  💎${g.storage.gem}`, W-16*S, topY+28*S)

  // 标签栏
  const tabY = topY + topH + 2*S
  const tabH = 30*S
  const tabs = [{id:'daily',label:'金币商店'},{id:'gem',label:'灵石商店'}]
  g._shopTabs = []
  for (let i = 0; i < tabs.length; i++) {
    const tx = i * (W/2)
    const active = _tab === tabs[i].id
    const btnR = [tx, tabY, W/2, tabH]
    g._shopTabs.push({ rect: btnR, id: tabs[i].id })
    ctx.fillStyle = active ? 'rgba(245,215,110,0.15)' : 'transparent'
    ctx.fillRect(tx, tabY, W/2, tabH)
    ctx.fillStyle = active ? '#f5d76e' : 'rgba(255,255,255,0.5)'
    ctx.font = `${12*S}px "PingFang SC",sans-serif`
    ctx.textAlign = 'center'
    ctx.fillText(tabs[i].label, tx+W/4, tabY+tabH*0.68)
  }

  // 商品列表
  const listY = tabY + tabH + 8*S
  const items = _tab === 'daily' ? SHOP_ITEMS_DAILY : SHOP_ITEMS_GEM
  const itemH = 60*S, itemGap = 8*S

  g._shopItemBtns = []
  for (let i = 0; i < items.length; i++) {
    const item = items[i]
    const iy = listY + i*(itemH+itemGap) - _scrollY

    const btnRect = [16*S, iy, W-32*S, itemH]
    g._shopItemBtns.push({ rect: btnRect, item, index: i })

    ctx.fillStyle = 'rgba(30,30,50,0.7)'
    R.roundRect(...btnRect, 8*S); ctx.fill()

    // 名称
    ctx.fillStyle = '#fff'; ctx.font = `bold ${13*S}px "PingFang SC",sans-serif`
    ctx.textAlign = 'left'
    ctx.fillText(item.name, btnRect[0]+14*S, iy+22*S)

    // 描述
    ctx.fillStyle = 'rgba(255,255,255,0.5)'; ctx.font = `${10*S}px "PingFang SC",sans-serif`
    ctx.fillText(item.desc, btnRect[0]+14*S, iy+40*S)

    // 价格按钮
    const priceW = 80*S, priceH = 32*S
    const priceX = btnRect[0]+btnRect[2]-priceW-10*S
    const priceY = iy + (itemH-priceH)/2
    const costKey = item.cost.gold !== undefined ? 'gold' : 'gem'
    const costVal = item.cost[costKey]
    const canAfford = costKey === 'gold' ? g.storage.gold >= costVal : g.storage.gem >= costVal

    ctx.fillStyle = canAfford ? (costKey === 'gold' ? '#f5d76e' : '#b388ff') : 'rgba(255,255,255,0.1)'
    R.roundRect(priceX, priceY, priceW, priceH, 6*S); ctx.fill()
    ctx.fillStyle = canAfford ? '#1a1a2e' : 'rgba(255,255,255,0.3)'
    ctx.font = `bold ${12*S}px "PingFang SC",sans-serif`
    ctx.textAlign = 'center'
    const icon = costKey === 'gold' ? '💰' : '💎'
    ctx.fillText(`${icon}${costVal}`, priceX+priceW/2, priceY+priceH*0.65)

    // 每日限购
    if (item.dailyLimit) {
      const bought = g.storage.daily[`shop_${item.id}`] || 0
      ctx.fillStyle = 'rgba(255,255,255,0.3)'; ctx.font = `${9*S}px "PingFang SC",sans-serif`
      ctx.textAlign = 'left'
      ctx.fillText(`限购 ${bought}/${item.dailyLimit}`, btnRect[0]+14*S, iy+52*S)
    }
  }

  // 购买结果提示
  if (_purchaseResult) {
    _renderPurchaseResult(g)
  }
}

function _renderPurchaseResult(g) {
  const { ctx, R, W, H, S } = V
  const pr = _purchaseResult

  ctx.save()
  ctx.fillStyle = 'rgba(0,0,0,0.4)'; ctx.fillRect(0, 0, W, H)
  const pw = 200*S, ph = 80*S
  const px = (W-pw)/2, py = (H-ph)/2
  ctx.fillStyle = 'rgba(20,20,40,0.95)'
  R.roundRect(px, py, pw, ph, 10*S); ctx.fill()
  ctx.fillStyle = pr.success ? '#4dcc4d' : '#ff5040'
  ctx.font = `bold ${14*S}px "PingFang SC",sans-serif`
  ctx.textAlign = 'center'
  ctx.fillText(pr.msg, px+pw/2, py+34*S)

  g._shopResultBtn = [px+pw/2-30*S, py+ph-30*S, 60*S, 24*S]
  ctx.fillStyle = 'rgba(255,255,255,0.15)'
  R.roundRect(...g._shopResultBtn, 4*S); ctx.fill()
  ctx.fillStyle = '#fff'; ctx.font = `${11*S}px "PingFang SC",sans-serif`
  ctx.fillText('确定', px+pw/2, py+ph-14*S)
  ctx.restore()
}

// ===== 触摸 =====
function tShopView(g, type, x, y) {
  if (type === 'move') {
    // 暂不滚动
    return
  }
  if (type !== 'end') return

  if (_purchaseResult) {
    if (g._shopResultBtn && _hit(x,y,g._shopResultBtn)) { _purchaseResult = null }
    return
  }

  if (g._shopBackBtn && _hit(x,y,g._shopBackBtn)) {
    g.scene = 'home'; _scrollY = 0; return
  }

  if (g._shopTabs) {
    for (const t of g._shopTabs) {
      if (_hit(x,y,t.rect)) { _tab = t.id; _scrollY = 0; return }
    }
  }

  if (g._shopItemBtns) {
    for (const btn of g._shopItemBtns) {
      if (_hit(x,y,btn.rect)) {
        _purchaseItem(g, btn.item)
        return
      }
    }
  }
}

function _purchaseItem(g, item) {
  // 每日限购检查
  if (item.dailyLimit) {
    const key = `shop_${item.id}`
    const bought = g.storage.daily[key] || 0
    if (bought >= item.dailyLimit) {
      _purchaseResult = { success: false, msg: '今日已售罄' }
      return
    }
  }

  // 扣费
  const costKey = item.cost.gold !== undefined ? 'gold' : 'gem'
  const costVal = item.cost[costKey]
  const ok = costKey === 'gold' ? g.storage.spendGold(costVal) : g.storage.spendGem(costVal)
  if (!ok) {
    _purchaseResult = { success: false, msg: `${costKey === 'gold' ? '金币' : '灵石'}不足` }
    return
  }

  // 发放
  const give = item.give
  if (give.normalBall) g.storage.addItem('normalBall', give.normalBall)
  if (give.superBall)  g.storage.addItem('superBall', give.superBall)
  if (give.masterBall) g.storage.addItem('masterBall', give.masterBall)
  if (give.expOrb_s)   g.storage.addItem('expOrb_s', give.expOrb_s)
  if (give.expOrb_m)   g.storage.addItem('expOrb_m', give.expOrb_m)
  if (give.expOrb_l)   g.storage.addItem('expOrb_l', give.expOrb_l)
  if (give.stamina)    g.storage.addStamina(give.stamina)
  if (give.staminaFull) {
    g.storage.addStamina(g.storage.staminaMax)
  }

  // 每日限购记录
  if (item.dailyLimit) {
    const key = `shop_${item.id}`
    if (!g.storage.daily[key]) g.storage.daily[key] = 0
    g.storage.daily[key]++
  }

  _purchaseResult = { success: true, msg: '购买成功！' }
}

function _hit(x,y,r) { return x>=r[0]&&x<=r[0]+r[2]&&y>=r[1]&&y<=r[1]+r[3] }

module.exports = { rShopView, tShopView }
