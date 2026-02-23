/**
 * 关卡选择视图 + 关卡结算视图 — 灵宠放置传
 * 显示区域内20关列表、星级进度、关卡详情、开始战斗
 */
const V = require('./env')
const { AREAS, generateStageData } = require('../data/stages')

// ===== 区域配色 =====
const AREA_COLORS = {
  metal: { main: '#f5d76e', bg: '#3a3520', accent: '#ffe066' },
  wood:  { main: '#6dd400', bg: '#1a3a10', accent: '#90ff40' },
  earth: { main: '#d4a24e', bg: '#3a2a10', accent: '#e8c070' },
  water: { main: '#4dabff', bg: '#102a3a', accent: '#80c8ff' },
  fire:  { main: '#ff5040', bg: '#3a1010', accent: '#ff8070' },
}

const AREA_NAMES = {
  metal: '金灵域', wood: '木灵域', earth: '土灵域',
  water: '水灵域', fire: '火灵域',
}

// ===== 渲染关卡选择 =====
function rStageSelect(g) {
  const { ctx, R, TH, W, H, S, safeTop } = V
  const area = g.selectedArea
  const color = AREA_COLORS[area] || AREA_COLORS.metal
  const areaData = AREAS[area]
  const cleared = g.storage.getStageClearedCount(area)

  // 背景
  ctx.fillStyle = color.bg
  ctx.fillRect(0, 0, W, H)
  // 尝试绘制区域背景图
  if (areaData && areaData.bgPath) {
    try {
      const img = R.getImage(areaData.bgPath)
      if (img) {
        ctx.globalAlpha = 0.3
        ctx.drawImage(img, 0, 0, W, H)
        ctx.globalAlpha = 1
      }
    } catch(e) {}
  }

  // ── 顶部标题栏 ──
  const topH = 46 * S
  const topY = safeTop
  ctx.fillStyle = 'rgba(0,0,0,0.6)'
  ctx.fillRect(0, topY, W, topH)

  // 返回按钮
  g._stageBackBtn = [8 * S, topY + 6 * S, 60 * S, 34 * S]
  ctx.fillStyle = 'rgba(255,255,255,0.15)'
  R.roundRect(...g._stageBackBtn, 8 * S)
  ctx.fill()
  ctx.fillStyle = '#fff'
  ctx.font = `${13 * S}px "PingFang SC",sans-serif`
  ctx.textAlign = 'center'
  ctx.fillText('← 返回', g._stageBackBtn[0] + g._stageBackBtn[2] / 2, topY + 28 * S)

  // 区域名称
  ctx.fillStyle = color.main
  ctx.font = `bold ${18 * S}px "PingFang SC",sans-serif`
  ctx.textAlign = 'center'
  ctx.fillText(areaData ? areaData.name : area, W / 2, topY + 30 * S)

  // 进度
  ctx.fillStyle = 'rgba(255,255,255,0.6)'
  ctx.font = `${11 * S}px "PingFang SC",sans-serif`
  ctx.textAlign = 'right'
  const totalStars = _getAreaTotalStars(g, area)
  ctx.fillText(`⭐ ${totalStars}/60  ${cleared}/20`, W - 16 * S, topY + 30 * S)

  // ── 关卡列表 ──
  const listY = topY + topH + 8 * S
  const listH = H - listY - 10 * S
  const stageH = 64 * S
  const stageGap = 8 * S

  ctx.save()
  ctx.beginPath()
  ctx.rect(0, listY, W, listH)
  ctx.clip()

  g._stageBtns = []
  for (let i = 1; i <= 20; i++) {
    const sy = listY + (i - 1) * (stageH + stageGap) - g.stageScrollY
    if (sy + stageH < listY || sy > listY + listH) continue  // 裁剪

    const isUnlocked = i <= cleared + 1
    const stars = g.storage.getStageStars(area, i)
    const isBoss = (i === 10 || i === 20)
    const isElite = (i === 5 || i === 15)

    const btnRect = [16 * S, sy, W - 32 * S, stageH]
    g._stageBtns.push({ rect: btnRect, stageNum: i, unlocked: isUnlocked })

    // 卡片背景
    if (isBoss) {
      ctx.fillStyle = isUnlocked ? 'rgba(180,40,40,0.6)' : 'rgba(50,20,20,0.5)'
    } else if (isElite) {
      ctx.fillStyle = isUnlocked ? 'rgba(120,80,20,0.6)' : 'rgba(40,30,10,0.5)'
    } else {
      ctx.fillStyle = isUnlocked ? 'rgba(40,40,60,0.6)' : 'rgba(20,20,30,0.5)'
    }
    R.roundRect(...btnRect, 10 * S)
    ctx.fill()

    // 左侧关卡号
    ctx.fillStyle = isUnlocked ? color.main : '#555'
    ctx.font = `bold ${20 * S}px "PingFang SC",sans-serif`
    ctx.textAlign = 'left'
    ctx.fillText(`${i}`, btnRect[0] + 14 * S, sy + stageH * 0.55)

    // 类型标签
    let typeLabel = '普通'
    let typeLabelColor = 'rgba(255,255,255,0.5)'
    if (isBoss) { typeLabel = '👑 BOSS'; typeLabelColor = '#ff5040' }
    else if (isElite) { typeLabel = '⚡ 精英'; typeLabelColor = '#f5d76e' }

    ctx.fillStyle = isUnlocked ? typeLabelColor : '#444'
    ctx.font = `${11 * S}px "PingFang SC",sans-serif`
    ctx.textAlign = 'left'
    ctx.fillText(typeLabel, btnRect[0] + 44 * S, sy + 22 * S)

    // 体力消耗
    if (areaData) {
      ctx.fillStyle = isUnlocked ? 'rgba(255,255,255,0.4)' : '#333'
      ctx.font = `${10 * S}px "PingFang SC",sans-serif`
      ctx.fillText(`⚡${areaData.staminaCost}`, btnRect[0] + 44 * S, sy + 42 * S)
    }

    // 星级显示
    if (stars > 0) {
      ctx.fillStyle = '#ffd700'
      ctx.font = `${14 * S}px "PingFang SC",sans-serif`
      ctx.textAlign = 'right'
      let starStr = ''
      for (let s = 0; s < 3; s++) starStr += (s < stars) ? '★' : '☆'
      ctx.fillText(starStr, btnRect[0] + btnRect[2] - 14 * S, sy + 24 * S)
    }

    // 状态
    ctx.textAlign = 'right'
    if (!isUnlocked) {
      ctx.fillStyle = '#555'
      ctx.font = `${11 * S}px "PingFang SC",sans-serif`
      ctx.fillText('🔒', btnRect[0] + btnRect[2] - 14 * S, sy + 48 * S)
    } else if (stars > 0) {
      ctx.fillStyle = '#4dcc4d'
      ctx.font = `${10 * S}px "PingFang SC",sans-serif`
      ctx.fillText('已通关', btnRect[0] + btnRect[2] - 14 * S, sy + 48 * S)
    } else {
      ctx.fillStyle = color.accent
      ctx.font = `bold ${11 * S}px "PingFang SC",sans-serif`
      ctx.fillText('挑战 →', btnRect[0] + btnRect[2] - 14 * S, sy + 48 * S)
    }
  }

  ctx.restore()
}

// ===== 渲染关卡结算 =====
function rStageResult(g) {
  const { ctx, R, TH, W, H, S, safeTop } = V
  const result = g.stageResult
  if (!result) return

  const area = g.selectedArea
  const color = AREA_COLORS[area] || AREA_COLORS.metal

  // 背景
  ctx.fillStyle = result.defeat ? '#1a0808' : color.bg
  ctx.fillRect(0, 0, W, H)

  const centerX = W / 2
  let curY = safeTop + 40 * S

  // 标题
  ctx.textAlign = 'center'
  if (result.defeat) {
    ctx.fillStyle = '#ff5040'
    ctx.font = `bold ${28 * S}px "PingFang SC",sans-serif`
    ctx.fillText('战斗失败', centerX, curY)
  } else {
    ctx.fillStyle = '#ffd700'
    ctx.font = `bold ${28 * S}px "PingFang SC",sans-serif`
    ctx.fillText('关卡通过！', centerX, curY)
  }
  curY += 36 * S

  // 关卡信息
  const areaName = AREA_NAMES[area] || area
  ctx.fillStyle = 'rgba(255,255,255,0.6)'
  ctx.font = `${13 * S}px "PingFang SC",sans-serif`
  ctx.fillText(`${areaName} 第${g.selectedStage}关`, centerX, curY)
  curY += 30 * S

  if (!result.defeat) {
    // 星级展示
    const stars = result.stars || 0
    ctx.font = `${30 * S}px "PingFang SC",sans-serif`
    let starStr = ''
    for (let i = 0; i < 3; i++) starStr += (i < stars) ? '★' : '☆'
    ctx.fillStyle = '#ffd700'
    ctx.fillText(starStr, centerX, curY)
    curY += 36 * S

    // 首次通关标记
    if (result.isFirstClear) {
      ctx.fillStyle = '#4dcc4d'
      ctx.font = `bold ${14 * S}px "PingFang SC",sans-serif`
      ctx.fillText('🎉 首次通关！', centerX, curY)
      curY += 24 * S
    }

    // 奖励详情卡
    const cardW = 260 * S, cardH = 140 * S
    const cardX = (W - cardW) / 2
    const cardY = curY
    ctx.fillStyle = 'rgba(0,0,0,0.5)'
    R.roundRect(cardX, cardY, cardW, cardH, 10 * S)
    ctx.fill()

    ctx.fillStyle = color.main
    ctx.font = `bold ${14 * S}px "PingFang SC",sans-serif`
    ctx.fillText('— 奖励 —', centerX, cardY + 22 * S)

    ctx.fillStyle = '#fff'
    ctx.font = `${13 * S}px "PingFang SC",sans-serif`
    let ry = cardY + 44 * S
    if (result.gold) {
      ctx.fillText(`💰 金币 +${result.gold}`, centerX, ry)
      ry += 22 * S
    }
    if (result.gem) {
      ctx.fillText(`💎 灵石 +${result.gem}`, centerX, ry)
      ry += 22 * S
    }
    if (result.exp) {
      ctx.fillText(`📖 经验 +${result.exp}`, centerX, ry)
      ry += 22 * S
    }
    if (result.petDrops && result.petDrops.length > 0) {
      ctx.fillStyle = '#4dcc4d'
      ctx.fillText(`🐾 获得宠物 ×${result.petDrops.length}！`, centerX, ry)
      ry += 22 * S
    }

    if (result.bonusStar2) {
      ctx.fillStyle = '#f5d76e'
      ctx.font = `${11 * S}px "PingFang SC",sans-serif`
      ctx.fillText('★★ 额外金币 +50', centerX, ry)
      ry += 18 * S
    }
    if (result.bonusStar3) {
      ctx.fillStyle = '#f5d76e'
      ctx.fillText('★★★ 额外灵石 +2', centerX, ry)
    }

    curY = cardY + cardH + 24 * S
  } else {
    curY += 20 * S
    ctx.fillStyle = 'rgba(255,255,255,0.5)'
    ctx.font = `${13 * S}px "PingFang SC",sans-serif`
    ctx.fillText('提升宠物等级或调整编队后再试', centerX, curY)
    curY += 40 * S
  }

  // 按钮
  const btnW = 160 * S, btnH = 44 * S

  // 返回按钮
  g._stageResultBackBtn = [centerX - btnW / 2, curY, btnW, btnH]
  ctx.fillStyle = 'rgba(255,255,255,0.15)'
  R.roundRect(...g._stageResultBackBtn, 10 * S)
  ctx.fill()
  ctx.strokeStyle = color.main
  ctx.lineWidth = 2 * S
  R.roundRect(...g._stageResultBackBtn, 10 * S)
  ctx.stroke()
  ctx.fillStyle = '#fff'
  ctx.font = `bold ${15 * S}px "PingFang SC",sans-serif`
  ctx.fillText('返回关卡', centerX, curY + btnH * 0.62)
  curY += btnH + 16 * S

  // 重新挑战按钮（仅失败时）
  if (result.defeat) {
    g._stageResultRetryBtn = [centerX - btnW / 2, curY, btnW, btnH]
    ctx.fillStyle = color.main
    R.roundRect(...g._stageResultRetryBtn, 10 * S)
    ctx.fill()
    ctx.fillStyle = '#1a1a2e'
    ctx.font = `bold ${15 * S}px "PingFang SC",sans-serif`
    ctx.fillText('重新挑战', centerX, curY + btnH * 0.62)
  } else {
    // 下一关按钮（如果有下一关）
    if (g.selectedStage < 20) {
      g._stageResultNextBtn = [centerX - btnW / 2, curY, btnW, btnH]
      ctx.fillStyle = color.main
      R.roundRect(...g._stageResultNextBtn, 10 * S)
      ctx.fill()
      ctx.fillStyle = '#1a1a2e'
      ctx.font = `bold ${15 * S}px "PingFang SC",sans-serif`
      ctx.fillText('下一关 →', centerX, curY + btnH * 0.62)
    }
    g._stageResultRetryBtn = null
  }
}

// ===== 触摸：关卡选择 =====
let _touchStartY = 0
let _touchMoved = false

function tStageSelect(g, type, x, y) {
  if (type === 'start') {
    _touchStartY = y
    _touchMoved = false
    return
  }

  if (type === 'move') {
    const dy = _touchStartY - y
    if (Math.abs(dy) > 5) _touchMoved = true
    g.stageScrollY = Math.max(0, g.stageScrollY + dy)
    _touchStartY = y
    return
  }

  if (type !== 'end') return
  if (_touchMoved) return

  // 返回按钮
  if (g._stageBackBtn && _hit(x, y, g._stageBackBtn)) {
    g.scene = 'home'
    return
  }

  // 关卡按钮
  if (g._stageBtns) {
    for (const btn of g._stageBtns) {
      if (btn.unlocked && _hit(x, y, btn.rect)) {
        g.selectedStage = btn.stageNum
        // 直接进入战斗
        const stageMgr = require('../engine/stageManager')
        const ok = stageMgr.enterStageBattle(g, g.selectedArea, btn.stageNum)
        if (!ok && g._staminaShortage) {
          g._staminaShortage = false
          // TODO: 显示体力不足提示
        }
        return
      }
    }
  }
}

// ===== 触摸：关卡结算 =====
function tStageResult(g, type, x, y) {
  if (type !== 'end') return

  // 返回关卡列表
  if (g._stageResultBackBtn && _hit(x, y, g._stageResultBackBtn)) {
    g.scene = 'stageSelect'
    g.stageResult = null
    return
  }

  // 重新挑战
  if (g._stageResultRetryBtn && _hit(x, y, g._stageResultRetryBtn)) {
    g.stageResult = null
    const stageMgr = require('../engine/stageManager')
    stageMgr.enterStageBattle(g, g.selectedArea, g.selectedStage)
    return
  }

  // 下一关
  if (g._stageResultNextBtn && _hit(x, y, g._stageResultNextBtn)) {
    g.stageResult = null
    g.selectedStage++
    const stageMgr = require('../engine/stageManager')
    stageMgr.enterStageBattle(g, g.selectedArea, g.selectedStage)
    return
  }
}

// ===== 工具函数 =====
function _hit(x, y, rect) {
  return x >= rect[0] && x <= rect[0] + rect[2] && y >= rect[1] && y <= rect[1] + rect[3]
}

function _getAreaTotalStars(g, area) {
  let total = 0
  const prog = g.storage.stageProgress[area]
  if (prog && prog.stars) {
    for (const s of Object.values(prog.stars)) total += s
  }
  return total
}

module.exports = {
  rStageSelect,
  rStageResult,
  tStageSelect,
  tStageResult,
}
