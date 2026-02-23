/**
 * 挂机放置视图 — 灵宠放置传 (Phase 5)
 * 挂机区域选择、队伍派遣、收益查看
 */
const V = require('./env')
const { AREAS, AREA_ORDER, getAvailableAreas } = require('../data/stages')
const { getPetById, getPetAvatarPath, getPetInstanceStats } = require('../data/pets')

const AREA_COLORS = {
  metal: { main: '#f5d76e', bg: '#3a3520' },
  wood:  { main: '#6dd400', bg: '#1a3a10' },
  earth: { main: '#d4a24e', bg: '#3a2a10' },
  water: { main: '#4dabff', bg: '#102a3a' },
  fire:  { main: '#ff5040', bg: '#3a1010' },
}

const AREA_NAMES = {
  metal: '金灵域', wood: '木灵域', earth: '土灵域',
  water: '水灵域', fire: '火灵域',
}

let _selectedArea = null
let _confirmStart = false

function rIdleManage(g) {
  const { ctx, R, TH, W, H, S, safeTop } = V

  ctx.fillStyle = '#0d0d1a'
  ctx.fillRect(0, 0, W, H)

  const topY = safeTop
  const topH = 42*S
  ctx.fillStyle = 'rgba(0,0,0,0.7)'; ctx.fillRect(0, topY, W, topH)

  // 返回
  g._idleBackBtn = [8*S, topY+6*S, 56*S, 30*S]
  ctx.fillStyle = 'rgba(255,255,255,0.15)'
  R.roundRect(...g._idleBackBtn, 6*S); ctx.fill()
  ctx.fillStyle = '#fff'; ctx.font = `${12*S}px "PingFang SC",sans-serif`
  ctx.textAlign = 'center'
  ctx.fillText('← 返回', g._idleBackBtn[0]+g._idleBackBtn[2]/2, topY+25*S)

  ctx.fillStyle = '#4dcc4d'; ctx.font = `bold ${16*S}px "PingFang SC",sans-serif`
  ctx.textAlign = 'center'
  ctx.fillText('挂机放置', W/2, topY+28*S)

  let curY = topY + topH + 12*S
  const idle = g.storage.idle

  // ── 当前挂机状态 ──
  if (idle.area && idle.startTime) {
    const elapsedMs = Date.now() - idle.startTime
    const hours = Math.min(elapsedMs / 3600000, idle.maxHours || 8)
    const areaName = AREA_NAMES[idle.area] || idle.area
    const clearedCount = g.storage.getStageClearedCount(idle.area)
    const baseExpPerHour = 50 + clearedCount * 15
    const baseGoldPerHour = 30 + clearedCount * 10

    // 状态卡
    const cardH = 140*S
    ctx.fillStyle = 'rgba(30,60,30,0.6)'
    R.roundRect(12*S, curY, W-24*S, cardH, 10*S); ctx.fill()

    ctx.fillStyle = '#4dcc4d'; ctx.font = `bold ${15*S}px "PingFang SC",sans-serif`
    ctx.textAlign = 'left'
    ctx.fillText(`🏕️ 挂机中: ${areaName}`, 24*S, curY+24*S)

    ctx.fillStyle = '#fff'; ctx.font = `${12*S}px "PingFang SC",sans-serif`
    ctx.fillText(`已挂机: ${hours.toFixed(1)} / ${idle.maxHours} 小时`, 24*S, curY+48*S)
    ctx.fillText(`预估金币: +${Math.floor(baseGoldPerHour * hours)}`, 24*S, curY+68*S)
    ctx.fillText(`预估经验: +${Math.floor(baseExpPerHour * hours)}`, 24*S, curY+88*S)

    // 挂机队伍头像
    const iconSize = 36*S, iconGap = 6*S
    const iconY = curY + 100*S
    for (let i = 0; i < (idle.teamUids || []).length; i++) {
      const ix = 24*S + i*(iconSize+iconGap)
      const inst = g.storage.getPetByUid(idle.teamUids[i])
      if (inst) {
        const tmpl = getPetById(inst.id)
        if (tmpl) {
          const avatarPath = getPetAvatarPath({...tmpl, star: inst.star})
          try {
            const img = R.getImage(avatarPath)
            if (img) {
              ctx.save()
              R.roundRect(ix, iconY, iconSize, iconSize, 4*S); ctx.clip()
              ctx.drawImage(img, ix, iconY, iconSize, iconSize)
              ctx.restore()
            }
          } catch(e) {}
        }
      }
    }

    // 领取 & 停止
    g._idleCollectBtn2 = [W-170*S, curY+cardH-44*S, 70*S, 32*S]
    ctx.fillStyle = '#f5d76e'
    R.roundRect(...g._idleCollectBtn2, 6*S); ctx.fill()
    ctx.fillStyle = '#1a1a2e'; ctx.font = `bold ${12*S}px "PingFang SC",sans-serif`
    ctx.textAlign = 'center'
    ctx.fillText('领取', g._idleCollectBtn2[0]+35*S, curY+cardH-23*S)

    g._idleStopBtn = [W-90*S, curY+cardH-44*S, 70*S, 32*S]
    ctx.fillStyle = '#ff5040'
    R.roundRect(...g._idleStopBtn, 6*S); ctx.fill()
    ctx.fillStyle = '#fff'
    ctx.fillText('停止', g._idleStopBtn[0]+35*S, curY+cardH-23*S)

    curY += cardH + 20*S
  } else {
    // 未挂机 → 选择区域
    ctx.fillStyle = 'rgba(255,255,255,0.5)'; ctx.font = `${13*S}px "PingFang SC",sans-serif`
    ctx.textAlign = 'center'
    ctx.fillText('选择已通关区域派遣队伍挂机', W/2, curY+10*S)
    curY += 30*S

    // 区域列表
    const available = getAvailableAreas(g.storage.stageProgress)
    g._idleAreaBtns = []

    for (let i = 0; i < AREA_ORDER.length; i++) {
      const areaId = AREA_ORDER[i]
      const area = AREAS[areaId]
      const cleared = g.storage.getStageClearedCount(areaId)
      const unlocked = available.includes(areaId) && cleared > 0
      const color = AREA_COLORS[areaId]
      const selected = _selectedArea === areaId

      const btnRect = [16*S, curY, W-32*S, 50*S]
      g._idleAreaBtns.push({ rect: btnRect, area: areaId, unlocked })

      ctx.fillStyle = selected ? 'rgba(77,204,77,0.2)' : (unlocked ? color.bg : 'rgba(30,30,30,0.5)')
      R.roundRect(...btnRect, 8*S); ctx.fill()

      if (selected) {
        ctx.strokeStyle = '#4dcc4d'; ctx.lineWidth = 2*S
        R.roundRect(...btnRect, 8*S); ctx.stroke()
      }

      ctx.fillStyle = unlocked ? color.main : '#555'
      ctx.font = `bold ${14*S}px "PingFang SC",sans-serif`
      ctx.textAlign = 'left'
      ctx.fillText(area.name, btnRect[0]+14*S, curY+22*S)

      ctx.fillStyle = unlocked ? 'rgba(255,255,255,0.5)' : '#333'
      ctx.font = `${11*S}px "PingFang SC",sans-serif`
      ctx.fillText(unlocked ? `已通关 ${cleared}/20` : '未开放', btnRect[0]+14*S, curY+40*S)

      curY += 56*S
    }

    // 开始挂机按钮
    if (_selectedArea) {
      const saBtnW = 180*S, saBtnH = 42*S
      g._idleStartBtn = [(W-saBtnW)/2, curY+10*S, saBtnW, saBtnH]
      ctx.fillStyle = '#4dcc4d'
      R.roundRect(...g._idleStartBtn, 10*S); ctx.fill()
      ctx.fillStyle = '#1a1a2e'; ctx.font = `bold ${14*S}px "PingFang SC",sans-serif`
      ctx.textAlign = 'center'
      ctx.fillText('开始挂机', W/2, curY+10*S+saBtnH*0.62)
    }
  }

  // 收益弹窗
  if (g._idleRewardPopup) {
    _drawIdleRewardPopup(g)
  }
}

function _drawIdleRewardPopup(g) {
  const { ctx, R, W, H, S } = V
  ctx.fillStyle = 'rgba(0,0,0,0.6)'; ctx.fillRect(0, 0, W, H)

  const rw = g._idleRewardPopup
  const pw = 260*S, ph = 180*S
  const px = (W-pw)/2, py = (H-ph)/2
  ctx.fillStyle = 'rgba(20,20,40,0.95)'
  R.roundRect(px, py, pw, ph, 12*S); ctx.fill()
  ctx.strokeStyle = '#4dcc4d'; ctx.lineWidth = 2*S
  R.roundRect(px, py, pw, ph, 12*S); ctx.stroke()

  ctx.fillStyle = '#4dcc4d'; ctx.font = `bold ${15*S}px "PingFang SC",sans-serif`
  ctx.textAlign = 'center'
  ctx.fillText('挂机收益', px+pw/2, py+26*S)

  ctx.fillStyle = '#fff'; ctx.font = `${13*S}px "PingFang SC",sans-serif`
  ctx.fillText(`挂机 ${rw.hours} 小时`, px+pw/2, py+52*S)
  ctx.fillText(`💰 金币 +${rw.gold}`, px+pw/2, py+76*S)
  ctx.fillText(`📖 经验 +${rw.exp}`, px+pw/2, py+96*S)

  if (rw.petDrops && rw.petDrops.length > 0) {
    ctx.fillStyle = '#ffd700'; ctx.fillText(`🐾 获得宠物!`, px+pw/2, py+118*S)
  }

  g._idleRewardOkBtn2 = [px+pw/2-40*S, py+ph-42*S, 80*S, 30*S]
  ctx.fillStyle = '#4dcc4d'
  R.roundRect(...g._idleRewardOkBtn2, 6*S); ctx.fill()
  ctx.fillStyle = '#1a1a2e'; ctx.font = `bold ${12*S}px "PingFang SC",sans-serif`
  ctx.fillText('确认', g._idleRewardOkBtn2[0]+40*S, py+ph-22*S)
}

// ===== 触摸 =====
function tIdleManage(g, type, x, y) {
  if (type !== 'end') return

  // 收益弹窗
  if (g._idleRewardPopup) {
    if (g._idleRewardOkBtn2 && _hit(x,y,g._idleRewardOkBtn2)) {
      g._idleRewardPopup = null
      return
    }
    return
  }

  if (g._idleBackBtn && _hit(x,y,g._idleBackBtn)) {
    g.scene = 'home'; _selectedArea = null; return
  }

  // 领取
  if (g._idleCollectBtn2 && _hit(x,y,g._idleCollectBtn2)) {
    const rw = g.storage.collectIdleRewards()
    if (rw) g._idleRewardPopup = rw
    return
  }

  // 停止
  if (g._idleStopBtn && _hit(x,y,g._idleStopBtn)) {
    const rw = g.storage.stopIdle()
    if (rw) g._idleRewardPopup = rw
    return
  }

  // 区域选择
  if (g._idleAreaBtns) {
    for (const btn of g._idleAreaBtns) {
      if (btn.unlocked && _hit(x,y,btn.rect)) {
        _selectedArea = btn.area
        return
      }
    }
  }

  // 开始挂机
  if (g._idleStartBtn && _selectedArea && _hit(x,y,g._idleStartBtn)) {
    const teamUids = g.storage.teams.idle.length > 0
      ? g.storage.teams.idle
      : g.storage.teams.battle
    if (teamUids.length > 0) {
      g.storage.startIdle(_selectedArea, teamUids)
      _selectedArea = null
    }
    return
  }
}

function _hit(x,y,r) { return x>=r[0]&&x<=r[0]+r[2]&&y>=r[1]&&y<=r[1]+r[3] }

module.exports = { rIdleManage, tIdleManage }
