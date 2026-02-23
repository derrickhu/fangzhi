/**
 * 宠物管理视图 — 灵宠放置传 (Phase 3)
 * 宠物列表、详情、升级、升星、编队管理
 */
const V = require('./env')
const {
  getPetById, getPetInstanceStats, getPetAvatarPath, getPetSkillDesc,
  getMaxLevel, getExpToLevel, MAX_STAR, getPetLore, getPetStarAtk,
} = require('../data/pets')
const { EXP_ITEMS } = require('../data/items')

const ATTR_COLORS = {
  metal: '#f5d76e', wood: '#6dd400', earth: '#d4a24e',
  water: '#4dabff', fire: '#ff5040',
}
const ATTR_NAMES = {
  metal: '金', wood: '木', earth: '土', water: '水', fire: '火',
}

// ===== 状态 =====
let _tab = 'list'          // 'list' | 'detail' | 'team'
let _scrollY = 0
let _selectedPetUid = null
let _filterAttr = null      // null=全部, 'metal'/'wood'/...
let _sortMode = 'level'     // 'level' | 'star' | 'atk'
let _teamEditSlot = -1      // 编辑中的队伍槽位
let _teamType = 'battle'    // 'battle' | 'idle'
let _expItemUse = null       // { itemKey, count }
let _fusionTarget = null     // 升星确认目标uid

// ===== 渲染宠物列表 =====
function rPetManage(g) {
  const { ctx, R, TH, W, H, S, safeTop } = V

  ctx.fillStyle = '#0d0d1a'
  ctx.fillRect(0, 0, W, H)

  if (_tab === 'detail' && _selectedPetUid) {
    _renderDetail(g)
    return
  }
  if (_tab === 'team') {
    _renderTeamEdit(g)
    return
  }

  // ── 顶部栏 ──
  const topY = safeTop
  const topH = 42 * S
  ctx.fillStyle = 'rgba(0,0,0,0.7)'
  ctx.fillRect(0, topY, W, topH)

  // 返回
  g._petBackBtn = [8*S, topY+6*S, 56*S, 30*S]
  ctx.fillStyle = 'rgba(255,255,255,0.15)'
  R.roundRect(...g._petBackBtn, 6*S); ctx.fill()
  ctx.fillStyle = '#fff'; ctx.font = `${12*S}px "PingFang SC",sans-serif`
  ctx.textAlign = 'center'
  ctx.fillText('← 返回', g._petBackBtn[0]+g._petBackBtn[2]/2, topY+25*S)

  // 标题
  ctx.fillStyle = '#f5d76e'; ctx.font = `bold ${16*S}px "PingFang SC",sans-serif`
  ctx.textAlign = 'center'
  ctx.fillText('灵宠管理', W/2, topY+28*S)

  // 编队按钮
  g._teamEditBtn = [W-68*S, topY+6*S, 58*S, 30*S]
  ctx.fillStyle = '#4dabff'
  R.roundRect(...g._teamEditBtn, 6*S); ctx.fill()
  ctx.fillStyle = '#fff'; ctx.font = `bold ${11*S}px "PingFang SC",sans-serif`
  ctx.fillText('编队', g._teamEditBtn[0]+g._teamEditBtn[2]/2, topY+25*S)

  // ── 属性筛选栏 ──
  const filterY = topY + topH + 4*S
  const filterH = 28*S
  const attrs = [null, 'metal', 'wood', 'earth', 'water', 'fire']
  const attrLabels = ['全部', '金', '木', '土', '水', '火']
  const attrW = W / attrs.length
  g._filterBtns = []
  for (let i = 0; i < attrs.length; i++) {
    const fx = i * attrW
    const active = _filterAttr === attrs[i]
    g._filterBtns.push({ rect: [fx, filterY, attrW, filterH], attr: attrs[i] })
    ctx.fillStyle = active ? 'rgba(245,215,110,0.2)' : 'transparent'
    ctx.fillRect(fx, filterY, attrW, filterH)
    ctx.fillStyle = active ? '#f5d76e' : 'rgba(255,255,255,0.5)'
    ctx.font = `${11*S}px "PingFang SC",sans-serif`
    ctx.textAlign = 'center'
    ctx.fillText(attrLabels[i], fx + attrW/2, filterY + filterH*0.68)
  }

  // ── 宠物网格 ──
  const gridY = filterY + filterH + 6*S
  const gridH = H - gridY
  const pets = _getFilteredPets(g)
  const cols = 4
  const cellPad = 6*S
  const cellW = (W - cellPad * (cols + 1)) / cols
  const cellH = cellW + 28*S
  const rows = Math.ceil(pets.length / cols)

  ctx.save()
  ctx.beginPath()
  ctx.rect(0, gridY, W, gridH)
  ctx.clip()

  g._petCells = []
  for (let i = 0; i < pets.length; i++) {
    const col = i % cols
    const row = Math.floor(i / cols)
    const cx = cellPad + col * (cellW + cellPad)
    const cy = gridY + row * (cellH + cellPad) - _scrollY

    if (cy + cellH < gridY || cy > gridY + gridH) continue

    const inst = pets[i]
    const template = getPetById(inst.id)
    if (!template) continue
    const stats = getPetInstanceStats(inst)

    g._petCells.push({ rect: [cx, cy, cellW, cellH], uid: inst.uid })

    // 卡片背景
    const aColor = ATTR_COLORS[inst.attr] || '#999'
    ctx.fillStyle = 'rgba(30,30,50,0.8)'
    R.roundRect(cx, cy, cellW, cellH, 6*S); ctx.fill()

    // 头像
    const avatarPath = getPetAvatarPath({ ...template, star: inst.star })
    try {
      const img = R.getImage(avatarPath)
      if (img) {
        ctx.save()
        R.roundRect(cx+2*S, cy+2*S, cellW-4*S, cellW-4*S, 4*S); ctx.clip()
        ctx.drawImage(img, cx+2*S, cy+2*S, cellW-4*S, cellW-4*S)
        ctx.restore()
      }
    } catch(e) {}

    // 属性色边框
    ctx.strokeStyle = aColor; ctx.lineWidth = 1.5*S
    R.roundRect(cx, cy, cellW, cellH, 6*S); ctx.stroke()

    // 星级
    let starStr = ''
    for (let s = 0; s < MAX_STAR; s++) starStr += (s < inst.star) ? '★' : '☆'
    ctx.fillStyle = '#ffd700'; ctx.font = `${8*S}px "PingFang SC",sans-serif`
    ctx.textAlign = 'center'
    ctx.fillText(starStr, cx + cellW/2, cy + cellW + 10*S)

    // 等级
    ctx.fillStyle = '#fff'; ctx.font = `${9*S}px "PingFang SC",sans-serif`
    ctx.fillText(`Lv${inst.level}`, cx + cellW/2, cy + cellW + 22*S)

    // 编队中标记
    if (g.storage.teams.battle.includes(inst.uid)) {
      ctx.fillStyle = '#ff5040'; ctx.font = `bold ${8*S}px "PingFang SC",sans-serif`
      ctx.textAlign = 'left'
      ctx.fillText('战', cx+3*S, cy+12*S)
    }
    if (g.storage.teams.idle.includes(inst.uid)) {
      ctx.fillStyle = '#4dcc4d'; ctx.font = `bold ${8*S}px "PingFang SC",sans-serif`
      ctx.textAlign = 'left'
      ctx.fillText('挂', cx+3*S, cy+22*S)
    }
  }

  ctx.restore()

  // 宠物数量
  ctx.fillStyle = 'rgba(255,255,255,0.4)'; ctx.font = `${10*S}px "PingFang SC",sans-serif`
  ctx.textAlign = 'right'
  ctx.fillText(`${g.storage.ownedPets.length}只`, W-12*S, gridY - 2*S)
}

// ===== 宠物详情页 =====
function _renderDetail(g) {
  const { ctx, R, TH, W, H, S, safeTop } = V
  const inst = g.storage.getPetByUid(_selectedPetUid)
  if (!inst) { _tab = 'list'; return }
  const template = getPetById(inst.id)
  if (!template) { _tab = 'list'; return }
  const stats = getPetInstanceStats(inst)
  const maxLv = getMaxLevel(inst.star)

  // 背景
  const aColor = ATTR_COLORS[inst.attr] || '#999'
  ctx.fillStyle = '#0d0d1a'; ctx.fillRect(0, 0, W, H)

  // 返回
  const topY = safeTop
  g._detailBackBtn = [8*S, topY+6*S, 56*S, 30*S]
  ctx.fillStyle = 'rgba(255,255,255,0.15)'
  R.roundRect(...g._detailBackBtn, 6*S); ctx.fill()
  ctx.fillStyle = '#fff'; ctx.font = `${12*S}px "PingFang SC",sans-serif`
  ctx.textAlign = 'center'
  ctx.fillText('← 返回', g._detailBackBtn[0]+g._detailBackBtn[2]/2, topY+25*S)

  let curY = topY + 50*S

  // 头像大图
  const imgSize = 120*S
  const imgX = (W - imgSize) / 2
  const avatarPath = getPetAvatarPath({ ...template, star: inst.star })
  try {
    const img = R.getImage(avatarPath)
    if (img) {
      ctx.save()
      R.roundRect(imgX, curY, imgSize, imgSize, 10*S); ctx.clip()
      ctx.drawImage(img, imgX, curY, imgSize, imgSize)
      ctx.restore()
    }
  } catch(e) {}
  ctx.strokeStyle = aColor; ctx.lineWidth = 2*S
  R.roundRect(imgX, curY, imgSize, imgSize, 10*S); ctx.stroke()

  curY += imgSize + 12*S

  // 名称和星级
  ctx.fillStyle = '#fff'; ctx.font = `bold ${18*S}px "PingFang SC",sans-serif`
  ctx.textAlign = 'center'
  ctx.fillText(template.name, W/2, curY)
  curY += 22*S

  let starStr = ''
  for (let s = 0; s < MAX_STAR; s++) starStr += (s < inst.star) ? '★' : '☆'
  ctx.fillStyle = '#ffd700'; ctx.font = `${14*S}px "PingFang SC",sans-serif`
  ctx.fillText(starStr, W/2, curY)
  curY += 22*S

  // 属性和等级
  ctx.fillStyle = aColor; ctx.font = `${13*S}px "PingFang SC",sans-serif`
  ctx.fillText(`${ATTR_NAMES[inst.attr]}属性  Lv.${inst.level}/${maxLv}`, W/2, curY)
  curY += 20*S

  // 经验条
  if (inst.level < maxLv) {
    const needed = getExpToLevel(inst.level + 1)
    const pct = needed > 0 ? inst.exp / needed : 1
    const barW = 200*S, barH = 10*S
    const barX = (W - barW) / 2
    ctx.fillStyle = 'rgba(255,255,255,0.15)'
    R.roundRect(barX, curY, barW, barH, 4*S); ctx.fill()
    ctx.fillStyle = '#4dabff'
    R.roundRect(barX, curY, barW * pct, barH, 4*S); ctx.fill()
    ctx.fillStyle = 'rgba(255,255,255,0.6)'; ctx.font = `${9*S}px "PingFang SC",sans-serif`
    ctx.fillText(`${inst.exp}/${needed}`, W/2, curY + barH + 12*S)
    curY += barH + 18*S
  } else {
    ctx.fillStyle = '#f5d76e'; ctx.font = `${11*S}px "PingFang SC",sans-serif`
    ctx.fillText('已达当前星级上限', W/2, curY)
    curY += 18*S
  }

  // 属性值
  const statY = curY
  const cardW = W - 40*S, cardX = 20*S
  ctx.fillStyle = 'rgba(30,30,50,0.7)'
  R.roundRect(cardX, statY, cardW, 70*S, 8*S); ctx.fill()

  ctx.font = `${12*S}px "PingFang SC",sans-serif`
  ctx.textAlign = 'left'
  ctx.fillStyle = '#ff5040'; ctx.fillText(`HP: ${stats.hp}`, cardX+16*S, statY+22*S)
  ctx.fillStyle = '#ffd700'; ctx.fillText(`ATK: ${stats.atk}`, cardX+16*S, statY+42*S)
  ctx.fillStyle = '#4dcc4d'; ctx.fillText(`REC: ${stats.rec}`, cardX+16*S, statY+62*S)

  // 技能描述
  ctx.textAlign = 'right'
  const skillDesc = getPetSkillDesc({ ...template, star: inst.star })
  if (skillDesc) {
    ctx.fillStyle = '#b388ff'; ctx.font = `${11*S}px "PingFang SC",sans-serif`
    ctx.fillText(template.skill.name, cardX + cardW - 16*S, statY+22*S)
    ctx.fillStyle = 'rgba(255,255,255,0.7)'; ctx.font = `${10*S}px "PingFang SC",sans-serif`
    // 简单文本截断
    const desc = skillDesc.length > 18 ? skillDesc.substr(0, 18) + '…' : skillDesc
    ctx.fillText(desc, cardX + cardW - 16*S, statY+42*S)
    ctx.fillStyle = 'rgba(255,255,255,0.4)'; ctx.font = `${10*S}px "PingFang SC",sans-serif`
    ctx.fillText(`CD: ${template.cd}回合`, cardX + cardW - 16*S, statY+62*S)
  } else {
    ctx.fillStyle = 'rgba(255,255,255,0.3)'; ctx.font = `${11*S}px "PingFang SC",sans-serif`
    ctx.fillText('★2解锁技能', cardX + cardW - 16*S, statY+42*S)
  }

  curY = statY + 80*S

  // ── 操作按钮 ──
  const btnW = 100*S, btnH = 36*S, btnGap = 12*S

  // 使用经验珠
  g._detailExpBtn = [(W - btnW*2 - btnGap)/2, curY, btnW, btnH]
  ctx.fillStyle = '#4dabff'
  R.roundRect(...g._detailExpBtn, 8*S); ctx.fill()
  ctx.fillStyle = '#fff'; ctx.font = `bold ${12*S}px "PingFang SC",sans-serif`
  ctx.textAlign = 'center'
  const expOrbCount = g.storage.getItemCount('expOrb_s') + g.storage.getItemCount('expOrb_m') + g.storage.getItemCount('expOrb_l')
  ctx.fillText(`升级(${expOrbCount})`, g._detailExpBtn[0]+btnW/2, curY+btnH*0.62)

  // 升星
  g._detailStarBtn = [g._detailExpBtn[0] + btnW + btnGap, curY, btnW, btnH]
  const canStarUp = inst.star < MAX_STAR && _canFuseForStarUp(g, inst)
  ctx.fillStyle = canStarUp ? '#f5d76e' : 'rgba(255,255,255,0.15)'
  R.roundRect(...g._detailStarBtn, 8*S); ctx.fill()
  ctx.fillStyle = canStarUp ? '#1a1a2e' : 'rgba(255,255,255,0.3)'
  ctx.fillText(inst.star >= MAX_STAR ? '已满星' : '升星', g._detailStarBtn[0]+btnW/2, curY+btnH*0.62)

  // 经验珠使用弹窗
  if (_expItemUse) {
    _renderExpItemPopup(g)
  }

  // 升星确认弹窗
  if (_fusionTarget) {
    _renderFusionConfirm(g)
  }
}

// ===== 经验珠使用弹窗 =====
function _renderExpItemPopup(g) {
  const { ctx, R, W, H, S } = V
  ctx.fillStyle = 'rgba(0,0,0,0.6)'; ctx.fillRect(0, 0, W, H)

  const pw = 260*S, ph = 200*S
  const px = (W-pw)/2, py = (H-ph)/2
  ctx.fillStyle = 'rgba(20,20,40,0.95)'
  R.roundRect(px, py, pw, ph, 12*S); ctx.fill()
  ctx.strokeStyle = '#4dabff'; ctx.lineWidth = 2*S
  R.roundRect(px, py, pw, ph, 12*S); ctx.stroke()

  ctx.fillStyle = '#4dabff'; ctx.font = `bold ${14*S}px "PingFang SC",sans-serif`
  ctx.textAlign = 'center'
  ctx.fillText('使用经验珠', px+pw/2, py+26*S)

  const items = [
    { key: 'expOrb_s', name: '小经验珠', exp: 100 },
    { key: 'expOrb_m', name: '中经验珠', exp: 500 },
    { key: 'expOrb_l', name: '大经验珠', exp: 2000 },
  ]

  g._expItemBtns = []
  let iy = py + 50*S
  for (const item of items) {
    const count = g.storage.getItemCount(item.key)
    const btnRect = [px+20*S, iy, pw-40*S, 34*S]
    g._expItemBtns.push({ rect: btnRect, key: item.key, exp: item.exp })

    ctx.fillStyle = count > 0 ? 'rgba(77,171,255,0.2)' : 'rgba(255,255,255,0.05)'
    R.roundRect(...btnRect, 6*S); ctx.fill()
    ctx.fillStyle = count > 0 ? '#fff' : 'rgba(255,255,255,0.3)'
    ctx.font = `${12*S}px "PingFang SC",sans-serif`
    ctx.textAlign = 'left'
    ctx.fillText(`${item.name} (+${item.exp}exp)`, btnRect[0]+10*S, iy+22*S)
    ctx.textAlign = 'right'
    ctx.fillText(`×${count}`, btnRect[0]+btnRect[2]-10*S, iy+22*S)
    iy += 40*S
  }

  // 关闭按钮
  g._expCloseBtn = [px+pw/2-40*S, py+ph-40*S, 80*S, 30*S]
  ctx.fillStyle = 'rgba(255,255,255,0.15)'
  R.roundRect(...g._expCloseBtn, 6*S); ctx.fill()
  ctx.fillStyle = '#fff'; ctx.font = `${12*S}px "PingFang SC",sans-serif`
  ctx.textAlign = 'center'
  ctx.fillText('关闭', g._expCloseBtn[0]+40*S, py+ph-20*S)
}

// ===== 升星确认弹窗 =====
function _renderFusionConfirm(g) {
  const { ctx, R, W, H, S } = V
  ctx.fillStyle = 'rgba(0,0,0,0.6)'; ctx.fillRect(0, 0, W, H)

  const inst = g.storage.getPetByUid(_selectedPetUid)
  if (!inst) { _fusionTarget = null; return }
  const template = getPetById(inst.id)
  if (!template) { _fusionTarget = null; return }

  const pw = 260*S, ph = 160*S
  const px = (W-pw)/2, py = (H-ph)/2
  ctx.fillStyle = 'rgba(20,20,40,0.95)'
  R.roundRect(px, py, pw, ph, 12*S); ctx.fill()
  ctx.strokeStyle = '#f5d76e'; ctx.lineWidth = 2*S
  R.roundRect(px, py, pw, ph, 12*S); ctx.stroke()

  ctx.fillStyle = '#f5d76e'; ctx.font = `bold ${14*S}px "PingFang SC",sans-serif`
  ctx.textAlign = 'center'
  ctx.fillText('确认升星？', px+pw/2, py+26*S)

  ctx.fillStyle = '#fff'; ctx.font = `${12*S}px "PingFang SC",sans-serif`
  ctx.fillText(`${template.name}  ★${inst.star} → ★${inst.star+1}`, px+pw/2, py+54*S)

  ctx.fillStyle = 'rgba(255,255,255,0.5)'; ctx.font = `${11*S}px "PingFang SC",sans-serif`
  ctx.fillText(`需要消耗1只同名宠物`, px+pw/2, py+78*S)

  // 确认/取消
  g._fusionOkBtn = [px+20*S, py+ph-44*S, 100*S, 32*S]
  ctx.fillStyle = '#f5d76e'
  R.roundRect(...g._fusionOkBtn, 6*S); ctx.fill()
  ctx.fillStyle = '#1a1a2e'; ctx.font = `bold ${12*S}px "PingFang SC",sans-serif`
  ctx.fillText('确认', g._fusionOkBtn[0]+50*S, py+ph-23*S)

  g._fusionCancelBtn = [px+pw-120*S, py+ph-44*S, 100*S, 32*S]
  ctx.fillStyle = 'rgba(255,255,255,0.15)'
  R.roundRect(...g._fusionCancelBtn, 6*S); ctx.fill()
  ctx.fillStyle = '#fff'
  ctx.fillText('取消', g._fusionCancelBtn[0]+50*S, py+ph-23*S)
}

// ===== 编队编辑页 =====
function _renderTeamEdit(g) {
  const { ctx, R, TH, W, H, S, safeTop } = V
  const topY = safeTop
  const topH = 42*S

  ctx.fillStyle = 'rgba(0,0,0,0.7)'; ctx.fillRect(0, topY, W, topH)

  // 返回
  g._teamBackBtn = [8*S, topY+6*S, 56*S, 30*S]
  ctx.fillStyle = 'rgba(255,255,255,0.15)'
  R.roundRect(...g._teamBackBtn, 6*S); ctx.fill()
  ctx.fillStyle = '#fff'; ctx.font = `${12*S}px "PingFang SC",sans-serif`
  ctx.textAlign = 'center'
  ctx.fillText('← 返回', g._teamBackBtn[0]+g._teamBackBtn[2]/2, topY+25*S)

  // 切换战斗/挂机队
  g._teamTypeBtns = []
  const types = [{id:'battle',label:'战斗队'},{id:'idle',label:'挂机队'}]
  for (let i = 0; i < types.length; i++) {
    const bx = W/2 - 60*S + i*70*S
    const active = _teamType === types[i].id
    const btnR = [bx, topY+8*S, 60*S, 26*S]
    g._teamTypeBtns.push({ rect: btnR, type: types[i].id })
    ctx.fillStyle = active ? '#f5d76e' : 'rgba(255,255,255,0.1)'
    R.roundRect(...btnR, 6*S); ctx.fill()
    ctx.fillStyle = active ? '#1a1a2e' : 'rgba(255,255,255,0.5)'
    ctx.font = `${11*S}px "PingFang SC",sans-serif`
    ctx.fillText(types[i].label, bx+30*S, topY+25*S)
  }

  // 当前队伍槽位
  const teamUids = _teamType === 'battle' ? [...g.storage.teams.battle] : [...g.storage.teams.idle]
  const slotY = topY + topH + 16*S
  const slotSize = 50*S
  const slotGap = 10*S
  const slotStartX = (W - 5*(slotSize+slotGap) + slotGap) / 2

  g._teamSlots = []
  for (let i = 0; i < 5; i++) {
    const sx = slotStartX + i*(slotSize+slotGap)
    const slotRect = [sx, slotY, slotSize, slotSize]
    g._teamSlots.push({ rect: slotRect, index: i })

    const isEdit = _teamEditSlot === i
    ctx.fillStyle = isEdit ? 'rgba(245,215,110,0.3)' : 'rgba(255,255,255,0.1)'
    R.roundRect(...slotRect, 8*S); ctx.fill()
    ctx.strokeStyle = isEdit ? '#f5d76e' : 'rgba(255,255,255,0.2)'
    ctx.lineWidth = isEdit ? 2*S : 1*S
    R.roundRect(...slotRect, 8*S); ctx.stroke()

    if (i < teamUids.length && teamUids[i]) {
      const inst = g.storage.getPetByUid(teamUids[i])
      if (inst) {
        const tmpl = getPetById(inst.id)
        if (tmpl) {
          const avatarPath = getPetAvatarPath({ ...tmpl, star: inst.star })
          try {
            const img = R.getImage(avatarPath)
            if (img) {
              ctx.save()
              R.roundRect(sx+2*S, slotY+2*S, slotSize-4*S, slotSize-4*S, 6*S); ctx.clip()
              ctx.drawImage(img, sx+2*S, slotY+2*S, slotSize-4*S, slotSize-4*S)
              ctx.restore()
            }
          } catch(e) {}
        }
        ctx.fillStyle = '#fff'; ctx.font = `${8*S}px "PingFang SC",sans-serif`
        ctx.textAlign = 'center'
        ctx.fillText(`Lv${inst.level}`, sx+slotSize/2, slotY+slotSize+10*S)
      }
    } else {
      ctx.fillStyle = 'rgba(255,255,255,0.2)'; ctx.font = `${20*S}px "PingFang SC",sans-serif`
      ctx.textAlign = 'center'
      ctx.fillText('+', sx+slotSize/2, slotY+slotSize*0.65)
    }
  }

  // 宠物列表（可选入队的）
  const listY = slotY + slotSize + 24*S
  const listH = H - listY
  const allPets = g.storage.ownedPets.slice().sort((a, b) => b.level - a.level || b.star - a.star)
  const cellW = 50*S, cellH = 60*S, cellGap = 6*S
  const cols = Math.floor((W - cellGap) / (cellW + cellGap))

  ctx.save()
  ctx.beginPath(); ctx.rect(0, listY, W, listH); ctx.clip()

  g._teamPetCells = []
  for (let i = 0; i < allPets.length; i++) {
    const col = i % cols, row = Math.floor(i / cols)
    const cx = cellGap + col*(cellW+cellGap)
    const cy = listY + row*(cellH+cellGap) - _scrollY
    if (cy + cellH < listY || cy > listY + listH) continue

    const inst = allPets[i]
    const inTeam = teamUids.includes(inst.uid)
    g._teamPetCells.push({ rect: [cx, cy, cellW, cellH], uid: inst.uid })

    ctx.fillStyle = inTeam ? 'rgba(245,215,110,0.15)' : 'rgba(30,30,50,0.7)'
    R.roundRect(cx, cy, cellW, cellH, 4*S); ctx.fill()

    if (inTeam) {
      ctx.strokeStyle = '#f5d76e'; ctx.lineWidth = 1.5*S
      R.roundRect(cx, cy, cellW, cellH, 4*S); ctx.stroke()
    }

    const tmpl = getPetById(inst.id)
    if (tmpl) {
      const avatarPath = getPetAvatarPath({ ...tmpl, star: inst.star })
      try {
        const img = R.getImage(avatarPath)
        if (img) {
          ctx.save()
          R.roundRect(cx+2*S, cy+2*S, cellW-4*S, cellW-4*S, 3*S); ctx.clip()
          ctx.drawImage(img, cx+2*S, cy+2*S, cellW-4*S, cellW-4*S)
          ctx.restore()
        }
      } catch(e) {}
    }

    ctx.fillStyle = '#fff'; ctx.font = `${8*S}px "PingFang SC",sans-serif`
    ctx.textAlign = 'center'
    ctx.fillText(`Lv${inst.level}`, cx+cellW/2, cy+cellW+8*S)
  }

  ctx.restore()
}

// ===== 触摸处理 =====
let _touchStartY = 0, _touchMoved = false

function tPetManage(g, type, x, y) {
  if (type === 'start') { _touchStartY = y; _touchMoved = false; return }
  if (type === 'move') {
    if (Math.abs(y - _touchStartY) > 5) _touchMoved = true
    _scrollY = Math.max(0, _scrollY + (_touchStartY - y))
    _touchStartY = y
    return
  }
  if (type !== 'end') return
  if (_touchMoved) return

  // 经验珠弹窗
  if (_expItemUse) {
    if (g._expCloseBtn && _hit(x,y,g._expCloseBtn)) { _expItemUse = null; return }
    if (g._expItemBtns) {
      for (const btn of g._expItemBtns) {
        if (_hit(x,y,btn.rect) && g.storage.getItemCount(btn.key) > 0) {
          g.storage.useItem(btn.key, 1)
          g.storage.addPetExp(_selectedPetUid, btn.exp)
          return
        }
      }
    }
    return
  }

  // 升星确认弹窗
  if (_fusionTarget) {
    if (g._fusionOkBtn && _hit(x,y,g._fusionOkBtn)) {
      _doFusion(g)
      _fusionTarget = null
      return
    }
    if (g._fusionCancelBtn && _hit(x,y,g._fusionCancelBtn)) { _fusionTarget = null; return }
    return
  }

  // 详情页
  if (_tab === 'detail') {
    if (g._detailBackBtn && _hit(x,y,g._detailBackBtn)) { _tab = 'list'; _scrollY = 0; return }
    if (g._detailExpBtn && _hit(x,y,g._detailExpBtn)) { _expItemUse = true; return }
    if (g._detailStarBtn && _hit(x,y,g._detailStarBtn)) {
      const inst = g.storage.getPetByUid(_selectedPetUid)
      if (inst && inst.star < MAX_STAR && _canFuseForStarUp(g, inst)) {
        _fusionTarget = _selectedPetUid
      }
      return
    }
    return
  }

  // 编队页
  if (_tab === 'team') {
    if (g._teamBackBtn && _hit(x,y,g._teamBackBtn)) { _tab = 'list'; _scrollY = 0; return }
    if (g._teamTypeBtns) {
      for (const btn of g._teamTypeBtns) {
        if (_hit(x,y,btn.rect)) { _teamType = btn.type; _teamEditSlot = -1; _scrollY = 0; return }
      }
    }
    if (g._teamSlots) {
      for (const slot of g._teamSlots) {
        if (_hit(x,y,slot.rect)) {
          const teamUids = _teamType === 'battle' ? g.storage.teams.battle : g.storage.teams.idle
          if (slot.index < teamUids.length && teamUids[slot.index]) {
            // 点击已有宠物槽 → 移除
            const newTeam = teamUids.filter((_, i) => i !== slot.index)
            if (_teamType === 'battle') g.storage.setBattleTeam(newTeam)
            else g.storage.setIdleTeam(newTeam)
          }
          _teamEditSlot = slot.index
          return
        }
      }
    }
    if (g._teamPetCells) {
      for (const cell of g._teamPetCells) {
        if (_hit(x,y,cell.rect)) {
          const teamUids = _teamType === 'battle' ? [...g.storage.teams.battle] : [...g.storage.teams.idle]
          if (teamUids.includes(cell.uid)) {
            // 已在队中 → 移除
            const idx = teamUids.indexOf(cell.uid)
            teamUids.splice(idx, 1)
          } else if (teamUids.length < 5) {
            teamUids.push(cell.uid)
          }
          if (_teamType === 'battle') g.storage.setBattleTeam(teamUids)
          else g.storage.setIdleTeam(teamUids)
          return
        }
      }
    }
    return
  }

  // 列表页
  if (g._petBackBtn && _hit(x,y,g._petBackBtn)) { g.scene = 'home'; _tab = 'list'; _scrollY = 0; return }
  if (g._teamEditBtn && _hit(x,y,g._teamEditBtn)) { _tab = 'team'; _scrollY = 0; return }
  if (g._filterBtns) {
    for (const btn of g._filterBtns) {
      if (_hit(x,y,btn.rect)) { _filterAttr = btn.attr; _scrollY = 0; return }
    }
  }
  if (g._petCells) {
    for (const cell of g._petCells) {
      if (_hit(x,y,cell.rect)) {
        _selectedPetUid = cell.uid
        _tab = 'detail'
        return
      }
    }
  }
}

// ===== 工具 =====
function _hit(x, y, r) { return x>=r[0]&&x<=r[0]+r[2]&&y>=r[1]&&y<=r[1]+r[3] }

function _getFilteredPets(g) {
  let pets = g.storage.ownedPets.slice()
  if (_filterAttr) pets = pets.filter(p => p.attr === _filterAttr)
  if (_sortMode === 'level') pets.sort((a,b) => b.level-a.level || b.star-a.star)
  else if (_sortMode === 'star') pets.sort((a,b) => b.star-a.star || b.level-a.level)
  return pets
}

function _canFuseForStarUp(g, inst) {
  // 需要同ID、非本体、非编队中的宠物作为素材
  return g.storage.ownedPets.some(p =>
    p.uid !== inst.uid &&
    p.id === inst.id &&
    !g.storage.teams.battle.includes(p.uid) &&
    !g.storage.teams.idle.includes(p.uid) &&
    !p.locked
  )
}

function _doFusion(g) {
  const inst = g.storage.getPetByUid(_selectedPetUid)
  if (!inst || inst.star >= MAX_STAR) return
  // 找素材宠物
  const material = g.storage.ownedPets.find(p =>
    p.uid !== inst.uid &&
    p.id === inst.id &&
    !g.storage.teams.battle.includes(p.uid) &&
    !g.storage.teams.idle.includes(p.uid) &&
    !p.locked
  )
  if (!material) return
  g.storage.removePet(material.uid)
  g.storage.starUpPet(inst.uid)
}

function resetView() {
  _tab = 'list'
  _scrollY = 0
  _selectedPetUid = null
  _expItemUse = null
  _fusionTarget = null
}

module.exports = { rPetManage, tPetManage, resetView }
