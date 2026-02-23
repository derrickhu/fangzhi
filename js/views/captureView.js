/**
 * 捕获界面渲染 — 灵宠放置传 (Phase 4)
 * 在战斗胜利后显示捕获UI：球选择、捕获动画、结果
 */
const V = require('./env')
const { CAPTURE_BALLS, calcCaptureRate } = require('../data/items')
const { getPetById, getPetAvatarPath } = require('../data/pets')

const BALL_ORDER = ['normalBall', 'superBall', 'masterBall', 'ultraBall']

// ===== 渲染捕获界面覆盖层 =====
function rCaptureOverlay(g) {
  const { ctx, R, W, H, S } = V
  const cp = g._capturePhase
  if (!cp || !cp.canCapture) return

  // 半透明遮罩
  ctx.save()
  ctx.fillStyle = 'rgba(0,0,0,0.65)'
  ctx.fillRect(0, 0, W, H)

  // 捕获动画中
  if (cp.captureResult && cp.animTimer > 0) {
    _renderCaptureAnim(g)
    ctx.restore()
    return
  }

  // 捕获结果
  if (cp.captureResult && cp.animTimer <= 0) {
    _renderCaptureResult(g)
    ctx.restore()
    return
  }

  // ── 捕获选择界面 ──
  const template = getPetById(cp.petId)
  const enemyName = cp.enemy ? cp.enemy.name : '???'
  const petName = template ? template.name : enemyName

  // 标题
  ctx.fillStyle = '#ffd700'
  ctx.font = `bold ${18*S}px "PingFang SC",sans-serif`
  ctx.textAlign = 'center'
  ctx.fillText('可以捕获！', W/2, H*0.22)

  ctx.fillStyle = '#fff'
  ctx.font = `${14*S}px "PingFang SC",sans-serif`
  ctx.fillText(petName, W/2, H*0.28)

  // 宠物头像
  if (template) {
    const avatarPath = getPetAvatarPath({ ...template, star: 1 })
    try {
      const img = R.getImage(avatarPath)
      if (img) {
        const imgS = 80*S
        ctx.save()
        R.roundRect((W-imgS)/2, H*0.30, imgS, imgS, 10*S); ctx.clip()
        ctx.drawImage(img, (W-imgS)/2, H*0.30, imgS, imgS)
        ctx.restore()
        ctx.strokeStyle = '#ffd700'; ctx.lineWidth = 2*S
        R.roundRect((W-imgS)/2, H*0.30, imgS, imgS, 10*S); ctx.stroke()
      }
    } catch(e) {}
  }

  // 灵珠选择按钮
  const btnY = H*0.56
  const btnW = 70*S, btnH = 70*S, btnGap = 8*S
  const totalW = BALL_ORDER.length * (btnW + btnGap) - btnGap
  const startX = (W - totalW) / 2

  g._captureBallBtns = []
  for (let i = 0; i < BALL_ORDER.length; i++) {
    const ballKey = BALL_ORDER[i]
    const ball = CAPTURE_BALLS[ballKey]
    const count = g.storage.getItemCount(ballKey)
    const bx = startX + i * (btnW + btnGap)
    const btnRect = [bx, btnY, btnW, btnH]
    g._captureBallBtns.push({ rect: btnRect, ballKey })

    const hasAny = count > 0
    ctx.fillStyle = hasAny ? 'rgba(40,40,70,0.9)' : 'rgba(20,20,30,0.7)'
    R.roundRect(...btnRect, 8*S); ctx.fill()

    if (hasAny) {
      ctx.strokeStyle = _ballColor(ball.rarity); ctx.lineWidth = 1.5*S
      R.roundRect(...btnRect, 8*S); ctx.stroke()
    }

    // 球名
    ctx.fillStyle = hasAny ? '#fff' : 'rgba(255,255,255,0.3)'
    ctx.font = `${10*S}px "PingFang SC",sans-serif`
    ctx.textAlign = 'center'
    ctx.fillText(ball.name.replace('灵珠',''), bx+btnW/2, btnY+20*S)

    // 概率
    const rate = calcCaptureRate(ballKey, cp.enemy, null)
    ctx.fillStyle = hasAny ? '#4dcc4d' : 'rgba(255,255,255,0.2)'
    ctx.font = `${11*S}px "PingFang SC",sans-serif`
    ctx.fillText(`${Math.round(rate*100)}%`, bx+btnW/2, btnY+38*S)

    // 数量
    ctx.fillStyle = hasAny ? '#f5d76e' : 'rgba(255,255,255,0.2)'
    ctx.font = `bold ${13*S}px "PingFang SC",sans-serif`
    ctx.fillText(`×${count}`, bx+btnW/2, btnY+56*S)
  }

  // 跳过按钮
  g._captureSkipBtn = [W/2-50*S, H*0.82, 100*S, 34*S]
  ctx.fillStyle = 'rgba(255,255,255,0.15)'
  R.roundRect(...g._captureSkipBtn, 8*S); ctx.fill()
  ctx.fillStyle = 'rgba(255,255,255,0.6)'
  ctx.font = `${13*S}px "PingFang SC",sans-serif`
  ctx.fillText('跳过', W/2, H*0.82+22*S)

  ctx.restore()
}

// ===== 捕获动画 =====
function _renderCaptureAnim(g) {
  const { ctx, R, W, H, S } = V
  const cp = g._capturePhase
  const progress = 1 - (cp.animTimer / 60)

  // 灵珠抖动动画
  const ballSize = 40*S
  const ballX = W/2 - ballSize/2
  const ballY = H*0.4
  const shake = cp.animTimer > 20 ? Math.sin(cp.animTimer * 0.5) * 8*S : 0

  ctx.fillStyle = _ballColor(CAPTURE_BALLS[cp.captureResult.ballType]?.rarity || 'normal')
  ctx.beginPath()
  ctx.arc(W/2 + shake, ballY + ballSize/2, ballSize/2, 0, Math.PI*2)
  ctx.fill()

  // 文字
  ctx.fillStyle = '#fff'
  ctx.font = `bold ${16*S}px "PingFang SC",sans-serif`
  ctx.textAlign = 'center'
  if (cp.animTimer > 30) {
    ctx.fillText('捕获中...', W/2, ballY + ballSize + 30*S)
  } else if (cp.animTimer > 10) {
    const dots = '.'.repeat(Math.floor((30 - cp.animTimer) / 7) + 1)
    ctx.fillText(`捕获中${dots}`, W/2, ballY + ballSize + 30*S)
  }
}

// ===== 捕获结果 =====
function _renderCaptureResult(g) {
  const { ctx, R, W, H, S } = V
  const cp = g._capturePhase

  if (cp.captureResult.success) {
    // 成功
    ctx.fillStyle = '#ffd700'
    ctx.font = `bold ${24*S}px "PingFang SC",sans-serif`
    ctx.textAlign = 'center'
    ctx.fillText('捕获成功！', W/2, H*0.35)

    // 宠物头像
    if (cp.capturedPet) {
      const tmpl = getPetById(cp.capturedPet.id)
      if (tmpl) {
        const avatarPath = getPetAvatarPath({ ...tmpl, star: 1 })
        try {
          const img = R.getImage(avatarPath)
          if (img) {
            const imgS = 80*S
            ctx.save()
            R.roundRect((W-imgS)/2, H*0.40, imgS, imgS, 10*S); ctx.clip()
            ctx.drawImage(img, (W-imgS)/2, H*0.40, imgS, imgS)
            ctx.restore()
          }
        } catch(e) {}
        ctx.fillStyle = '#fff'; ctx.font = `${14*S}px "PingFang SC",sans-serif`
        ctx.fillText(tmpl.name, W/2, H*0.40 + 90*S)
      }
    }
  } else {
    // 失败
    ctx.fillStyle = '#ff5040'
    ctx.font = `bold ${24*S}px "PingFang SC",sans-serif`
    ctx.textAlign = 'center'
    ctx.fillText('捕获失败...', W/2, H*0.40)

    ctx.fillStyle = 'rgba(255,255,255,0.5)'
    ctx.font = `${13*S}px "PingFang SC",sans-serif`
    ctx.fillText('灵宠挣脱了灵珠的束缚', W/2, H*0.48)
  }

  // 继续按钮
  g._captureConfirmBtn = [W/2-60*S, H*0.72, 120*S, 40*S]
  ctx.fillStyle = '#f5d76e'
  R.roundRect(...g._captureConfirmBtn, 8*S); ctx.fill()
  ctx.fillStyle = '#1a1a2e'
  ctx.font = `bold ${14*S}px "PingFang SC",sans-serif`
  ctx.fillText('继续', W/2, H*0.72+26*S)
}

// ===== 触摸处理 =====
function tCaptureOverlay(g, type, x, y) {
  if (type !== 'end') return false
  const cp = g._capturePhase
  if (!cp || !cp.canCapture) return false

  // 捕获动画中 → 不响应
  if (cp.captureResult && cp.animTimer > 0) return true

  // 捕获结果 → 确认
  if (cp.captureResult && cp.animTimer <= 0) {
    if (g._captureConfirmBtn && _hit(x,y,g._captureConfirmBtn)) {
      const stageMgr = require('../engine/stageManager')
      stageMgr.confirmCapture(g)
      return true
    }
    return true // 模态
  }

  // 选球
  if (g._captureBallBtns) {
    for (const btn of g._captureBallBtns) {
      if (_hit(x,y,btn.rect)) {
        const count = g.storage.getItemCount(btn.ballKey)
        if (count > 0) {
          const stageMgr = require('../engine/stageManager')
          stageMgr.attemptCapture(g, btn.ballKey)
        }
        return true
      }
    }
  }

  // 跳过
  if (g._captureSkipBtn && _hit(x,y,g._captureSkipBtn)) {
    const stageMgr = require('../engine/stageManager')
    stageMgr.skipCapture(g)
    return true
  }

  return true // 模态
}

function _hit(x,y,r) { return x>=r[0]&&x<=r[0]+r[2]&&y>=r[1]&&y<=r[1]+r[3] }

function _ballColor(rarity) {
  switch(rarity) {
    case 'rare': return '#4dabff'
    case 'epic': return '#b388ff'
    case 'legendary': return '#ffd700'
    default: return '#8bc34a'
  }
}

module.exports = { rCaptureOverlay, tCaptureOverlay }
