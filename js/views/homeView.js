/**
 * 主页视图 — 灵宠放置传
 * 显示玩家信息、资源、队伍预览、挂机状态、功能入口
 */
const V = require('./env')
const { AREAS, AREA_ORDER, isAreaUnlocked, getAvailableAreas } = require('../data/stages')
const { getPetById, getPetInstanceStats, getPetAvatarPath } = require('../data/pets')

// ===== 区域中文名/颜色映射 =====
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

// ===== 渲染主页 =====
function rHome(g) {
  const { ctx, R, TH, W, H, S, safeTop } = V

  // 背景
  R.drawHomeBg(g.af)

  // ── 顶部信息栏 ──
  const topY = safeTop + 8 * S
  const barH = 36 * S

  // 半透明底条
  ctx.fillStyle = 'rgba(0,0,0,0.5)'
  R.roundRect(8 * S, topY, W - 16 * S, barH, 10 * S)
  ctx.fill()

  // 玩家等级
  ctx.fillStyle = '#f5d76e'
  ctx.font = `bold ${14 * S}px "PingFang SC",sans-serif`
  ctx.textAlign = 'left'
  ctx.fillText(`Lv.${g.storage.playerLevel}`, 20 * S, topY + barH * 0.6)

  // 金币
  ctx.fillStyle = '#ffd700'
  ctx.font = `${12 * S}px "PingFang SC",sans-serif`
  const goldX = 80 * S
  ctx.fillText(`💰 ${_formatNum(g.storage.gold)}`, goldX, topY + barH * 0.6)

  // 灵石
  ctx.fillStyle = '#b388ff'
  const gemX = 160 * S
  ctx.fillText(`💎 ${g.storage.gem}`, gemX, topY + barH * 0.6)

  // 体力
  g.storage.updateStamina()
  ctx.fillStyle = '#4dcc4d'
  const staX = 240 * S
  ctx.fillText(`⚡ ${g.storage.stamina}/${g.storage.staminaMax}`, staX, topY + barH * 0.6)

  // ── 战队预览 ──
  const teamY = topY + barH + 16 * S
  const teamH = 70 * S
  ctx.fillStyle = 'rgba(0,0,0,0.4)'
  R.roundRect(8 * S, teamY, W - 16 * S, teamH, 10 * S)
  ctx.fill()

  ctx.fillStyle = 'rgba(255,255,255,0.6)'
  ctx.font = `${11 * S}px "PingFang SC",sans-serif`
  ctx.textAlign = 'left'
  ctx.fillText('战斗队伍', 20 * S, teamY + 16 * S)

  // 战力
  const power = g.storage.calcTeamPower(g.storage.teams.battle)
  ctx.fillStyle = '#ff6b6b'
  ctx.textAlign = 'right'
  ctx.fillText(`战力 ${power}`, W - 20 * S, teamY + 16 * S)

  // 宠物头像
  const teamUids = g.storage.teams.battle
  const iconSize = 40 * S
  const iconGap = 8 * S
  const iconStartX = 20 * S
  const iconY = teamY + 24 * S
  for (let i = 0; i < 5; i++) {
    const ix = iconStartX + i * (iconSize + iconGap)
    // 槽位底
    ctx.fillStyle = 'rgba(255,255,255,0.1)'
    R.roundRect(ix, iconY, iconSize, iconSize, 6 * S)
    ctx.fill()

    if (i < teamUids.length) {
      const uid = teamUids[i]
      const inst = g.storage.getPetByUid(uid)
      if (inst) {
        const template = getPetById(inst.id)
        if (template) {
          // 尝试绘制头像图片
          const avatarPath = getPetAvatarPath({ ...template, star: inst.star })
          try {
            const img = R.getImage(avatarPath)
            if (img) {
              ctx.save()
              R.roundRect(ix, iconY, iconSize, iconSize, 6 * S)
              ctx.clip()
              ctx.drawImage(img, ix, iconY, iconSize, iconSize)
              ctx.restore()
            }
          } catch(e) {}

          // 属性色边框
          const aColor = AREA_COLORS[inst.attr]?.main || '#fff'
          ctx.strokeStyle = aColor
          ctx.lineWidth = 2 * S
          R.roundRect(ix, iconY, iconSize, iconSize, 6 * S)
          ctx.stroke()

          // 等级
          ctx.fillStyle = '#fff'
          ctx.font = `${9 * S}px "PingFang SC",sans-serif`
          ctx.textAlign = 'center'
          ctx.fillText(`Lv${inst.level}`, ix + iconSize / 2, iconY + iconSize + 10 * S)
        }
      }
    } else {
      // 空槽位 +
      ctx.fillStyle = 'rgba(255,255,255,0.3)'
      ctx.font = `${20 * S}px "PingFang SC",sans-serif`
      ctx.textAlign = 'center'
      ctx.fillText('+', ix + iconSize / 2, iconY + iconSize * 0.65)
    }
  }

  // ── 挂机状态卡 ──
  const idleY = teamY + teamH + 16 * S
  const idleH = 50 * S
  const idle = g.storage.idle

  ctx.fillStyle = 'rgba(0,0,0,0.4)'
  R.roundRect(8 * S, idleY, W - 16 * S, idleH, 10 * S)
  ctx.fill()

  ctx.textAlign = 'left'
  if (idle.area && idle.startTime) {
    const elapsedMs = Date.now() - idle.startTime
    const hours = Math.min(elapsedMs / 3600000, idle.maxHours || 8)
    const areaName = AREA_NAMES[idle.area] || idle.area

    ctx.fillStyle = '#4dcc4d'
    ctx.font = `bold ${13 * S}px "PingFang SC",sans-serif`
    ctx.fillText(`🏕️ 挂机中: ${areaName}`, 20 * S, idleY + 22 * S)

    ctx.fillStyle = 'rgba(255,255,255,0.7)'
    ctx.font = `${11 * S}px "PingFang SC",sans-serif`
    ctx.fillText(`已挂机 ${hours.toFixed(1)} 小时`, 20 * S, idleY + 40 * S)

    // 领取按钮
    g._idleCollectBtn = [W - 90 * S, idleY + 8 * S, 78 * S, 34 * S]
    ctx.fillStyle = '#f5d76e'
    R.roundRect(...g._idleCollectBtn, 8 * S)
    ctx.fill()
    ctx.fillStyle = '#1a1a2e'
    ctx.font = `bold ${12 * S}px "PingFang SC",sans-serif`
    ctx.textAlign = 'center'
    ctx.fillText('领取', g._idleCollectBtn[0] + g._idleCollectBtn[2] / 2, idleY + 30 * S)
  } else {
    ctx.fillStyle = 'rgba(255,255,255,0.5)'
    ctx.font = `${12 * S}px "PingFang SC",sans-serif`
    ctx.fillText('🏕️ 未挂机 — 通关关卡后可派遣队伍挂机', 20 * S, idleY + 30 * S)
    g._idleCollectBtn = null
  }

  // ── 区域入口按钮列表 ──
  const areaStartY = idleY + idleH + 20 * S
  const areaBtnH = 56 * S
  const areaBtnGap = 10 * S
  g._areaBtns = []

  const availableAreas = getAvailableAreas(g.storage.stageProgress)

  for (let i = 0; i < AREA_ORDER.length; i++) {
    const areaId = AREA_ORDER[i]
    const area = AREAS[areaId]
    const ay = areaStartY + i * (areaBtnH + areaBtnGap)
    const unlocked = availableAreas.includes(areaId)
    const cleared = g.storage.getStageClearedCount(areaId)
    const color = AREA_COLORS[areaId] || { main: '#999', bg: '#222' }

    const btnRect = [12 * S, ay, W - 24 * S, areaBtnH]
    g._areaBtns.push({ rect: btnRect, area: areaId, unlocked })

    // 背景
    ctx.fillStyle = unlocked ? color.bg : 'rgba(30,30,30,0.6)'
    R.roundRect(...btnRect, 10 * S)
    ctx.fill()

    // 属性色左侧标记条
    ctx.fillStyle = unlocked ? color.main : '#555'
    ctx.fillRect(btnRect[0], ay + 8 * S, 4 * S, areaBtnH - 16 * S)

    // 区域名称
    ctx.fillStyle = unlocked ? '#fff' : '#666'
    ctx.font = `bold ${15 * S}px "PingFang SC",sans-serif`
    ctx.textAlign = 'left'
    ctx.fillText(area.name, btnRect[0] + 16 * S, ay + 24 * S)

    // 描述
    ctx.fillStyle = unlocked ? 'rgba(255,255,255,0.6)' : 'rgba(255,255,255,0.3)'
    ctx.font = `${10 * S}px "PingFang SC",sans-serif`
    ctx.fillText(area.desc, btnRect[0] + 16 * S, ay + 42 * S)

    // 进度
    ctx.textAlign = 'right'
    if (unlocked) {
      ctx.fillStyle = color.main
      ctx.font = `bold ${12 * S}px "PingFang SC",sans-serif`
      ctx.fillText(`${cleared}/20`, btnRect[0] + btnRect[2] - 12 * S, ay + 24 * S)

      ctx.fillStyle = 'rgba(255,255,255,0.5)'
      ctx.font = `${10 * S}px "PingFang SC",sans-serif`
      ctx.fillText(`体力 ${area.staminaCost}`, btnRect[0] + btnRect[2] - 12 * S, ay + 42 * S)
    } else {
      ctx.fillStyle = '#666'
      ctx.font = `${11 * S}px "PingFang SC",sans-serif`
      ctx.fillText('🔒 未解锁', btnRect[0] + btnRect[2] - 12 * S, ay + 32 * S)
    }
  }

  // ── 每日副本入口 ──
  const { DAILY_DUNGEONS } = require('../data/stages')
  const dungeonY = areaStartY + AREA_ORDER.length * (areaBtnH + areaBtnGap) + 10 * S
  const dungeonKeys = Object.keys(DAILY_DUNGEONS)
  const dungeonBtnW = (W - 24 * S - (dungeonKeys.length - 1) * 8 * S) / dungeonKeys.length
  const dungeonBtnH = 50 * S
  g._dungeonBtns = []

  ctx.fillStyle = 'rgba(255,255,255,0.5)'
  ctx.font = `bold ${12 * S}px "PingFang SC",sans-serif`
  ctx.textAlign = 'left'
  ctx.fillText('每日副本', 20 * S, dungeonY - 2 * S)

  for (let i = 0; i < dungeonKeys.length; i++) {
    const dk = dungeonKeys[i]
    const dungeon = DAILY_DUNGEONS[dk]
    const dx = 12 * S + i * (dungeonBtnW + 8 * S)
    const dRect = [dx, dungeonY, dungeonBtnW, dungeonBtnH]

    // 检查是否今天可用
    let available = true
    if (Array.isArray(dungeon.available)) {
      const dow = new Date().getDay()
      available = dungeon.available.includes(dow)
    }
    const usedCount = g.storage.getDungeonCount(dk)
    const remaining = dungeon.maxDaily - usedCount

    g._dungeonBtns.push({ rect: dRect, id: dk, available: available && remaining > 0 })

    ctx.fillStyle = (available && remaining > 0) ? 'rgba(50,30,80,0.8)' : 'rgba(30,30,30,0.6)'
    R.roundRect(...dRect, 8 * S); ctx.fill()

    ctx.fillStyle = (available && remaining > 0) ? '#b388ff' : '#666'
    ctx.font = `bold ${11 * S}px "PingFang SC",sans-serif`
    ctx.textAlign = 'center'
    ctx.fillText(dungeon.name, dx + dungeonBtnW / 2, dungeonY + 20 * S)

    ctx.fillStyle = (available && remaining > 0) ? 'rgba(255,255,255,0.6)' : 'rgba(255,255,255,0.25)'
    ctx.font = `${9 * S}px "PingFang SC",sans-serif`
    ctx.fillText(available ? `剩余 ${Math.max(0, remaining)}/${dungeon.maxDaily}` : '今日未开', dx + dungeonBtnW / 2, dungeonY + 38 * S)
  }

  // ── 底部功能栏 ──
  const bottomH = 56 * S
  const bottomY = H - bottomH
  ctx.fillStyle = 'rgba(0,0,0,0.7)'
  ctx.fillRect(0, bottomY, W, bottomH)

  const tabs = [
    { id: 'adventure', label: '冒险', icon: '⚔️' },
    { id: 'pets', label: '灵宠', icon: '🐾' },
    { id: 'bag', label: '背包', icon: '🎒' },
    { id: 'shop', label: '商店', icon: '🏪' },
    { id: 'idle', label: '挂机', icon: '🏕️' },
    { id: 'tower', label: '通天塔', icon: '🗼' },
  ]
  const tabW = W / tabs.length
  g._homeTabs = []

  for (let i = 0; i < tabs.length; i++) {
    const tx = i * tabW
    const tab = tabs[i]
    const active = g.homeTab === tab.id

    g._homeTabs.push({ rect: [tx, bottomY, tabW, bottomH], id: tab.id })

    if (active) {
      ctx.fillStyle = 'rgba(245,215,110,0.15)'
      ctx.fillRect(tx, bottomY, tabW, bottomH)
    }

    ctx.fillStyle = active ? '#f5d76e' : 'rgba(255,255,255,0.5)'
    ctx.font = `${18 * S}px "PingFang SC",sans-serif`
    ctx.textAlign = 'center'
    ctx.fillText(tab.icon, tx + tabW / 2, bottomY + 24 * S)

    ctx.font = `${10 * S}px "PingFang SC",sans-serif`
    ctx.fillText(tab.label, tx + tabW / 2, bottomY + 42 * S)
  }

  // 挂机收益提示弹窗
  if (g._pendingIdleCollect && g._idleRewards) {
    _drawIdleRewardsPopup(g)
  }

  // 每日副本结果弹窗
  if (g._dungeonResult) {
    _drawDungeonResultPopup(g)
  }
}

// ===== 挂机收益弹窗 =====
function _drawIdleRewardsPopup(g) {
  const { ctx, R, TH, W, H, S } = V

  // 遮罩
  ctx.fillStyle = 'rgba(0,0,0,0.6)'
  ctx.fillRect(0, 0, W, H)

  const pw = 280 * S, ph = 200 * S
  const px = (W - pw) / 2, py = (H - ph) / 2

  ctx.fillStyle = 'rgba(20,20,40,0.95)'
  R.roundRect(px, py, pw, ph, 12 * S)
  ctx.fill()
  ctx.strokeStyle = '#f5d76e'
  ctx.lineWidth = 2 * S
  R.roundRect(px, py, pw, ph, 12 * S)
  ctx.stroke()

  const rw = g._idleRewards
  ctx.fillStyle = '#f5d76e'
  ctx.font = `bold ${16 * S}px "PingFang SC",sans-serif`
  ctx.textAlign = 'center'
  ctx.fillText('挂机收益', px + pw / 2, py + 30 * S)

  ctx.fillStyle = '#fff'
  ctx.font = `${13 * S}px "PingFang SC",sans-serif`
  ctx.fillText(`挂机 ${rw.hours} 小时`, px + pw / 2, py + 56 * S)
  ctx.fillText(`金币 +${rw.gold}`, px + pw / 2, py + 80 * S)
  ctx.fillText(`经验 +${rw.exp}`, px + pw / 2, py + 100 * S)

  if (rw.petDrops && rw.petDrops.length > 0) {
    ctx.fillStyle = '#4dcc4d'
    ctx.fillText(`🎉 获得宠物 ×${rw.petDrops.length}！`, px + pw / 2, py + 124 * S)
  }

  // 确认按钮
  g._idleRewardOkBtn = [px + pw / 2 - 50 * S, py + ph - 46 * S, 100 * S, 34 * S]
  ctx.fillStyle = '#f5d76e'
  R.roundRect(...g._idleRewardOkBtn, 8 * S)
  ctx.fill()
  ctx.fillStyle = '#1a1a2e'
  ctx.font = `bold ${14 * S}px "PingFang SC",sans-serif`
  ctx.fillText('确认', g._idleRewardOkBtn[0] + g._idleRewardOkBtn[2] / 2, py + ph - 24 * S)
}

// ===== 触摸处理 =====
function tHome(g, type, x, y) {
  if (type !== 'end') return

  // 挂机收益弹窗
  if (g._pendingIdleCollect && g._idleRewards && g._idleRewardOkBtn) {
    if (_hit(x, y, g._idleRewardOkBtn)) {
      g._pendingIdleCollect = false
      g._idleRewards = null
      return
    }
    return // 弹窗模态
  }

  // 自动领取挂机（首次进入时）
  if (g._pendingIdleCollect && !g._idleRewards) {
    const rewards = g.storage.collectIdleRewards()
    if (rewards) {
      g._idleRewards = rewards
    } else {
      g._pendingIdleCollect = false
    }
    return
  }

  // 每日副本结果弹窗
  if (g._dungeonResult) {
    if (g._dungeonResultOkBtn && _hit(x, y, g._dungeonResultOkBtn)) {
      g._dungeonResult = null
      g._dungeonResultOkBtn = null
    }
    return // 模态
  }

  // 挂机领取按钮
  if (g._idleCollectBtn && _hit(x, y, g._idleCollectBtn)) {
    const rewards = g.storage.collectIdleRewards()
    if (rewards) {
      g._idleRewards = rewards
      g._pendingIdleCollect = true
    }
    return
  }

  // 区域按钮
  if (g._areaBtns) {
    for (const btn of g._areaBtns) {
      if (btn.unlocked && _hit(x, y, btn.rect)) {
        g.selectedArea = btn.area
        g.stageScrollY = 0
        g.scene = 'stageSelect'
        return
      }
    }
  }

  // 每日副本按钮
  if (g._dungeonBtns) {
    for (const btn of g._dungeonBtns) {
      if (btn.available && _hit(x, y, btn.rect)) {
        // TODO: 进入每日副本战斗（当前版本简化处理为直接发放奖励）
        const { DAILY_DUNGEONS } = require('../data/stages')
        const dungeon = DAILY_DUNGEONS[btn.id]
        if (dungeon) {
          // 消耗体力
          if (!g.storage.spendStamina(dungeon.staminaCost)) {
            console.log('[Dungeon] 体力不足')
            return
          }
          // 记录次数
          g.storage.addDungeonCount(btn.id)
          // 发放奖励
          const level = g.storage.playerLevel
          const rewards = dungeon.generateRewards(level)
          for (const [key, val] of Object.entries(rewards)) {
            if (key === 'gold') g.storage.addGold(val)
            else g.storage.addItem(key, val)
          }
          // 简易提示（复用挂机弹窗机制）
          g._dungeonResult = { name: dungeon.name, rewards }
        }
        return
      }
    }
  }

  // 底部功能栏
  if (g._homeTabs) {
    for (const tab of g._homeTabs) {
      if (_hit(x, y, tab.rect)) {
        if (tab.id === 'tower') {
          // 进入通天塔（原版title）
          g.scene = 'title'
        } else if (tab.id === 'pets') {
          const petManageView = require('./petManageView')
          petManageView.resetView()
          g.scene = 'petManage'
        } else if (tab.id === 'bag') {
          g.scene = 'inventory'
        } else if (tab.id === 'shop') {
          g.scene = 'shopNew'
        } else if (tab.id === 'idle') {
          g.scene = 'idleManage'
        } else {
          g.homeTab = tab.id
        }
        return
      }
    }
  }
}

function _hit(x, y, rect) {
  return x >= rect[0] && x <= rect[0] + rect[2] && y >= rect[1] && y <= rect[1] + rect[3]
}

// ===== 每日副本结果弹窗 =====
function _drawDungeonResultPopup(g) {
  const { ctx, R, TH, W, H, S } = V

  ctx.fillStyle = 'rgba(0,0,0,0.6)'
  ctx.fillRect(0, 0, W, H)

  const pw = 260 * S, ph = 180 * S
  const px = (W - pw) / 2, py = (H - ph) / 2

  ctx.fillStyle = 'rgba(20,20,40,0.95)'
  R.roundRect(px, py, pw, ph, 12 * S); ctx.fill()
  ctx.strokeStyle = '#b388ff'; ctx.lineWidth = 2 * S
  R.roundRect(px, py, pw, ph, 12 * S); ctx.stroke()

  const dr = g._dungeonResult
  ctx.fillStyle = '#b388ff'
  ctx.font = `bold ${16 * S}px "PingFang SC",sans-serif`
  ctx.textAlign = 'center'
  ctx.fillText(dr.name + ' 完成！', px + pw / 2, py + 30 * S)

  ctx.fillStyle = '#fff'
  ctx.font = `${13 * S}px "PingFang SC",sans-serif`
  let ry = py + 56 * S
  for (const [key, val] of Object.entries(dr.rewards)) {
    const label = _itemLabel(key)
    ctx.fillText(`${label} +${val}`, px + pw / 2, ry)
    ry += 22 * S
  }

  g._dungeonResultOkBtn = [px + pw / 2 - 50 * S, py + ph - 46 * S, 100 * S, 34 * S]
  ctx.fillStyle = '#b388ff'
  R.roundRect(...g._dungeonResultOkBtn, 8 * S); ctx.fill()
  ctx.fillStyle = '#fff'
  ctx.font = `bold ${14 * S}px "PingFang SC",sans-serif`
  ctx.fillText('确认', g._dungeonResultOkBtn[0] + g._dungeonResultOkBtn[2] / 2, py + ph - 24 * S)
}

function _itemLabel(key) {
  const labels = {
    gold: '金币', gem: '灵石', exp: '经验',
    normalBall: '普通灵珠', superBall: '高级灵珠', masterBall: '大师灵珠',
    expOrb_s: '小经验珠', expOrb_m: '中经验珠', expOrb_l: '大经验珠',
  }
  return labels[key] || key
}

function _formatNum(n) {
  if (n >= 10000) return (n / 10000).toFixed(1) + 'w'
  if (n >= 1000) return (n / 1000).toFixed(1) + 'k'
  return '' + n
}

module.exports = { rHome, tHome }
