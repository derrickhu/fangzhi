/**
 * 背包视图 — 灵宠放置传 (Phase 6)
 * 展示所有道具：灵珠、经验珠、素材等
 */
const V = require('./env')
const { CAPTURE_BALLS, EXP_ITEMS } = require('../data/items')

// 道具定义汇总（用于展示）
const ALL_ITEMS = [
  { key: 'normalBall', ...CAPTURE_BALLS.normalBall, category: '灵珠' },
  { key: 'superBall',  ...CAPTURE_BALLS.superBall,  category: '灵珠' },
  { key: 'masterBall', ...CAPTURE_BALLS.masterBall, category: '灵珠' },
  { key: 'ultraBall',  ...CAPTURE_BALLS.ultraBall,  category: '灵珠' },
  { key: 'expOrb_s',   ...EXP_ITEMS.expOrb_s,       category: '经验' },
  { key: 'expOrb_m',   ...EXP_ITEMS.expOrb_m,       category: '经验' },
  { key: 'expOrb_l',   ...EXP_ITEMS.expOrb_l,       category: '经验' },
]

const RARITY_COLORS = {
  normal: '#8bc34a',
  rare: '#4dabff',
  epic: '#b388ff',
  legendary: '#ffd700',
}

function rInventory(g) {
  const { ctx, R, TH, W, H, S, safeTop } = V

  ctx.fillStyle = '#0d0d1a'; ctx.fillRect(0, 0, W, H)

  const topY = safeTop
  const topH = 42*S
  ctx.fillStyle = 'rgba(0,0,0,0.7)'; ctx.fillRect(0, topY, W, topH)

  // 返回
  g._invBackBtn = [8*S, topY+6*S, 56*S, 30*S]
  ctx.fillStyle = 'rgba(255,255,255,0.15)'
  R.roundRect(...g._invBackBtn, 6*S); ctx.fill()
  ctx.fillStyle = '#fff'; ctx.font = `${12*S}px "PingFang SC",sans-serif`
  ctx.textAlign = 'center'
  ctx.fillText('← 返回', g._invBackBtn[0]+g._invBackBtn[2]/2, topY+25*S)

  ctx.fillStyle = '#f5d76e'; ctx.font = `bold ${16*S}px "PingFang SC",sans-serif`
  ctx.fillText('背包', W/2, topY+28*S)

  // 货币
  ctx.textAlign = 'right'; ctx.fillStyle = '#ffd700'; ctx.font = `${11*S}px "PingFang SC",sans-serif`
  ctx.fillText(`💰${g.storage.gold}  💎${g.storage.gem}`, W-16*S, topY+28*S)

  // 道具网格
  const gridY = topY + topH + 12*S
  const cols = 3
  const cellPad = 8*S
  const cellW = (W - cellPad * (cols + 1)) / cols
  const cellH = 80*S

  const items = ALL_ITEMS.filter(i => g.storage.getItemCount(i.key) > 0)

  g._invCells = []
  for (let i = 0; i < items.length; i++) {
    const col = i % cols, row = Math.floor(i / cols)
    const cx = cellPad + col * (cellW + cellPad)
    const cy = gridY + row * (cellH + cellPad)

    const item = items[i]
    const count = g.storage.getItemCount(item.key)
    const rarColor = RARITY_COLORS[item.rarity] || '#999'

    g._invCells.push({ rect: [cx, cy, cellW, cellH], item })

    ctx.fillStyle = 'rgba(30,30,50,0.7)'
    R.roundRect(cx, cy, cellW, cellH, 8*S); ctx.fill()

    ctx.strokeStyle = rarColor + '80'; ctx.lineWidth = 1*S
    R.roundRect(cx, cy, cellW, cellH, 8*S); ctx.stroke()

    // 类别
    ctx.fillStyle = rarColor; ctx.font = `${9*S}px "PingFang SC",sans-serif`
    ctx.textAlign = 'left'
    ctx.fillText(item.category, cx+8*S, cy+14*S)

    // 名称
    ctx.fillStyle = '#fff'; ctx.font = `bold ${11*S}px "PingFang SC",sans-serif`
    ctx.textAlign = 'center'
    ctx.fillText(item.name, cx+cellW/2, cy+36*S)

    // 数量
    ctx.fillStyle = '#f5d76e'; ctx.font = `bold ${16*S}px "PingFang SC",sans-serif`
    ctx.fillText(`×${count}`, cx+cellW/2, cy+60*S)

    // 描述
    ctx.fillStyle = 'rgba(255,255,255,0.4)'; ctx.font = `${8*S}px "PingFang SC",sans-serif`
    ctx.fillText(item.desc.substr(0, 10), cx+cellW/2, cy+74*S)
  }

  if (items.length === 0) {
    ctx.fillStyle = 'rgba(255,255,255,0.3)'; ctx.font = `${14*S}px "PingFang SC",sans-serif`
    ctx.textAlign = 'center'
    ctx.fillText('背包空空如也', W/2, H*0.4)
  }
}

// ===== 触摸 =====
function tInventory(g, type, x, y) {
  if (type !== 'end') return
  if (g._invBackBtn && _hit(x,y,g._invBackBtn)) {
    g.scene = 'home'; return
  }
}

function _hit(x,y,r) { return x>=r[0]&&x<=r[0]+r[2]&&y>=r[1]&&y<=r[1]+r[3] }

module.exports = { rInventory, tInventory }
