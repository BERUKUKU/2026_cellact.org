(function () {
  'use strict';
  var d = document;

  // Mobile menu
  var btn = d.querySelector('.menu-btn');
  var nav = d.getElementById('gnav');
  if (btn && nav) {
    var setOpen = function (open) {
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      nav.classList.toggle('open', open);
    };
    btn.addEventListener('click', function () { setOpen(btn.getAttribute('aria-expanded') !== 'true'); });
    d.addEventListener('keydown', function (e) { if (e.key === 'Escape') { setOpen(false); btn.focus(); } });
    nav.addEventListener('click', function (e) { if (e.target.closest('a')) setOpen(false); });
  }

  // Reveal on scroll
  var targets = d.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && targets.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    targets.forEach(function (t) { io.observe(t); });
  } else {
    targets.forEach(function (t) { t.classList.add('in'); });
  }

  // Contact form: confirm-email match check
  var form = d.querySelector('form[data-contact]');
  if (form) {
    var a = form.querySelector('[name=email]');
    var b2 = form.querySelector('[name=email_confirm]');
    var check = function () {
      b2.setCustomValidity(a.value && b2.value && a.value !== b2.value ? 'メールアドレスが一致しません' : '');
    };
    a.addEventListener('input', check); b2.addEventListener('input', check);
  }

  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var finePointer = window.matchMedia && matchMedia('(pointer: fine)').matches;

  // Scroll progress line under the header
  var bar = d.createElement('div');
  bar.className = 'progress'; bar.setAttribute('aria-hidden', 'true');
  d.body.appendChild(bar);
  var ticking = false;
  var onScroll = function () {
    if (ticking) return; ticking = true;
    requestAnimationFrame(function () {
      var h = d.documentElement.scrollHeight - innerHeight;
      bar.style.transform = 'scaleX(' + (h > 0 ? Math.min(scrollY / h, 1) : 0) + ')';
      ticking = false;
    });
  };
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  // Top hero intro: the capsule logo closes, its hexagon breaks into the site's hexagons, the picture comes into focus, then the copy follows
  var heroEl = d.querySelector('.hero'), introEl = d.querySelector('[data-capsule-intro]');
  var introDelay = 0;                                   // seconds the headline stagger must wait
  if (heroEl && introEl) {
    var seen = false;   // plays on every visit / reload (set to a sessionStorage check to show it once per tab)
    var layer = heroEl.querySelector('.hero-intro'), veil = heroEl.querySelector('.hi-veil');
    var copy = heroEl.querySelector('.hero-inner'), hint = heroEl.querySelector('.scroll-hint');
    var bgImg = heroEl.querySelector('.hero-bg img');
    if (!reduce && !seen) {
      var iSvg = introEl.querySelector('svg'), iTravel = 66, iClose = 2.85;
      var T_BREAK = 3.9, T_FOCUS = 5.4, T_END = 6.0;                    // seconds: hexagon starts to break / picture sharp + logo gone / copy fully in
      var BLUR0 = 16;                                                   // px of blur on the picture at the start
      var iTimer = 0, iDone = false;
      var bc = d.createElement('canvas'); bc.className = 'hi-burst'; layer.appendChild(bc);
      var bx = bc.getContext('2d'), bdpr = Math.min(devicePixelRatio || 1, 2), BW = 0, BH = 0, parts = [];
      var iSet = function (id, k, v) { var e = iSvg.querySelector('#' + id); if (e) e.setAttribute(k, v); };
      var iEase = function (t, a, b) { var x = Math.max(0, Math.min(1, (t - a) / (b - a))); return x * x * x * (x * (x * 6 - 15) + 10); };
      var iFrame = function (t) {
        var q = 1 - iEase(t, 0, iClose), op = iEase(t, .08, 2.2), bl = iEase(t, 2.8, 2.95);
        [['top', -1], ['bottom', 1]].forEach(function (p) { iSet('shell_' + p[0], 'transform', 'translate(0 ' + (p[1] * iTravel * q) + ')'); iSet('shell_' + p[0], 'opacity', op * (1 - bl)); });
        iSet('shell_exact', 'opacity', op * bl);
        ['head', 'plus', 'legs'].forEach(function (id) { iSet(id, 'opacity', iEase(t, .02, 1.75)); });
        iSet('wordmark', 'opacity', iEase(t, 1.5, 3.05));
      };
      var sizeBurst = function () { var r = heroEl.getBoundingClientRect(); BW = r.width; BH = r.height; bc.width = BW * bdpr; bc.height = BH * bdpr; bx.setTransform(bdpr, 0, 0, bdpr, 0, 0); };
      var makeParts = function () {
        // the logo hexagon lives in viewBox units (centre ~ (627,532), circumradius ~ 380); map that outline onto the screen
        var hr = heroEl.getBoundingClientRect(), sr = iSvg.getBoundingClientRect(), vb = iSvg.viewBox.baseVal, sc = sr.width / vb.width;
        var cx = sr.left - hr.left + (627 - vb.x) * sc, cy = sr.top - hr.top + (532 - vb.y) * sc, R = 380 * sc;
        var k = Math.max(0.8, BW / 1400);
        parts = [];
        for (var i = 0; i < 34; i++) {
          var edge = Math.floor(Math.random() * 6), u = Math.random();
          var a1 = (-90 + 60 * edge) * Math.PI / 180, a2 = (-90 + 60 * (edge + 1)) * Math.PI / 180;
          var x = cx + R * ((1 - u) * Math.cos(a1) + u * Math.cos(a2)), y = cy + R * ((1 - u) * Math.sin(a1) + u * Math.sin(a2));
          var dir = Math.atan2(y - cy, x - cx) + (Math.random() - .5) * 0.9, sp = (90 + Math.random() * 230) * k;
          parts.push({ x: x, y: y, vx: Math.cos(dir) * sp, vy: Math.sin(dir) * sp - 18 * k, r: (7 + Math.random() * 20) * k, z: 0.5 + Math.random() * 0.7,
            rot: Math.random() * 6.28, vr: (Math.random() - .5) * 1.6, delay: Math.random() * 0.7, life: 2.2 + Math.random() * 1.6 });
        }
      };
      var drawBurst = function (t) {
        bx.clearRect(0, 0, BW, BH);
        var u = t - T_BREAK; if (u < 0) return;
        bx.shadowColor = 'rgba(255,255,255,.85)'; bx.shadowBlur = 6;
        parts.forEach(function (p) {
          var a = u - p.delay; if (a < 0 || a > p.life) return;
          var m = 1 - Math.exp(-a * 1.6);                                  // fast start, easing out
          var px = p.x + p.vx * m * 0.9, py = p.y + p.vy * m * 0.9, rot = p.rot + p.vr * a;
          var env = Math.sin(Math.PI * Math.min(1, a / p.life)); env = Math.min(1, env * 1.7);
          bx.lineWidth = 1.5 + p.z * 1.1; bx.strokeStyle = 'rgba(11,127,117,' + (0.95 * env) + ')'; bx.fillStyle = 'rgba(255,255,255,' + (0.16 * env) + ')';
          bx.beginPath();
          for (var q = 0; q < 6; q++) { var an = rot + q * Math.PI / 3; var hx = px + Math.cos(an) * p.r, hy = py + Math.sin(an) * p.r; q ? bx.lineTo(hx, hy) : bx.moveTo(hx, hy); }
          bx.closePath(); bx.fill(); bx.stroke();
        });
        bx.shadowBlur = 0;
      };
      var iScene = function (t) {
        iFrame(Math.min(t, 4.1));
        var go = iEase(t, T_BREAK, T_FOCUS);
        introEl.style.opacity = 1 - iEase(t, T_BREAK + 0.15, T_BREAK + 1.2);   // the logo dissolves while its hexagon breaks apart
        veil.style.opacity = 1 - iEase(t, T_BREAK, T_FOCUS - 0.3);
        if (bgImg) bgImg.style.filter = 'blur(' + (BLUR0 * (1 - go)).toFixed(2) + 'px)';
        var cp = iEase(t, T_BREAK + 0.6, T_FOCUS + 1.0);                          // copy fades in once the picture is nearly sharp
        copy.style.opacity = cp; if (hint) hint.style.opacity = cp;
      };
      var iFinish = function () {
        if (iDone) return; iDone = true; clearInterval(iTimer);
        heroEl.classList.remove('intro-on');
        copy.style.opacity = ''; if (hint) hint.style.opacity = '';
        if (bgImg) { bgImg.style.filter = ''; bgImg.classList.remove('intro-blur'); }
        layer.style.display = 'none';
      };
      introDelay = T_FOCUS - 0.15;                                              // headline starts as the picture comes into focus
      sizeBurst(); heroEl.classList.add('intro-on'); copy.style.opacity = 0; if (hint) hint.style.opacity = 0;
      if (bgImg) bgImg.classList.add('intro-blur');
      iScene(0);
      var iStart = Date.now(), madeParts = false;
      iTimer = setInterval(function () {
        var t = (Date.now() - iStart) / 1000;
        
        iScene(t);
        if (t >= T_FOCUS + 1.3) iFinish();
      }, 16);
      addEventListener('resize', sizeBurst);
      var skip = function () { iFinish(); };
      var sk = heroEl.querySelector('.hi-skip'); if (sk) sk.addEventListener('click', function (e) { e.stopPropagation(); skip(); });
      heroEl.addEventListener('click', skip); addEventListener('keydown', skip, { once: true });
    } else if (layer) { layer.style.display = 'none'; }
  }

  // Logo capsule animation (company page): the shell closes from above and below, then the wordmark fades in
  var capEl = d.querySelector('[data-capsule]');
  if (capEl) {
    var capSvg = capEl.querySelector('svg'), capTravel = 66, capClose = 2.85, capTotal = 4.1, capTimer = 0, capStarted = false;
    var capPart = function (id) { return capSvg.querySelector('#' + id); };
    var capSet = function (id, k, v) { var e = capPart(id); if (e) e.setAttribute(k, v); };
    var capEase = function (t, a, b) { var x = Math.max(0, Math.min(1, (t - a) / (b - a))); return x * x * x * (x * (x * 6 - 15) + 10); };
    var capFrame = function (t) {
      var q = 1 - capEase(t, 0, capClose), op = capEase(t, .08, 2.2), blend = capEase(t, 2.8, 2.95);
      [['top', -1], ['bottom', 1]].forEach(function (p) {
        capSet('shell_' + p[0], 'transform', 'translate(0 ' + (p[1] * capTravel * q) + ')');
        capSet('shell_' + p[0], 'opacity', op * (1 - blend));
      });
      capSet('shell_exact', 'opacity', op * blend);
      ['head', 'plus', 'legs'].forEach(function (id) { capSet(id, 'opacity', capEase(t, .02, 1.75)); });
      capSet('wordmark', 'opacity', capEase(t, 1.5, 3.05));
    };
    var playCap = function () {
      cancelAnimationFrame(capTimer); clearInterval(capTimer);
      if (reduce) { capFrame(capTotal); return; }
      capFrame(0); var st = Date.now();
      // timer-driven (not only requestAnimationFrame) so it keeps running when the tab/window has no focus
      capTimer = setInterval(function () {
        var t = (Date.now() - st) / 1000; capFrame(Math.min(t, capTotal));
        if (t >= capTotal) clearInterval(capTimer);
      }, 16);
    };
    capFrame(0);                                         // start from the open shell so the first play is visible
    var capBtn = capEl.querySelector('.lm-replay');
    if (capBtn) capBtn.addEventListener('click', playCap);
    var capGo = function () { if (capStarted) return; capStarted = true; setTimeout(playCap, 250); };
    var capCheck = function () {
      var r = capEl.getBoundingClientRect();
      if (r.top < innerHeight * 0.85 && r.bottom > innerHeight * 0.15) { capGo(); removeEventListener('scroll', capCheck); }
    };
    if (reduce) capFrame(capTotal);
    else {
      // scroll check works everywhere; IntersectionObserver is an extra trigger; a timer is the last-resort fallback
      addEventListener('scroll', capCheck, { passive: true }); capCheck();
      if ('IntersectionObserver' in window) new IntersectionObserver(function (en, o) { if (en[0].isIntersecting) { capGo(); o.disconnect(); } }, { threshold: 0.25 }).observe(capEl);
    }
  }

  if (reduce) return;

  // Hero headline: characters rise in one by one
  var h1 = d.querySelector('.hero h1, .page-hero h1');
  if (h1 && !(introDelay && h1.closest('.hero'))) {   // top hero after the intro: the copy simply fades in with the picture
    var n = 0;
    var wrap = function (node) {
      Array.prototype.slice.call(node.childNodes).forEach(function (c) {
        if (c.nodeType === 3) {
          var f = d.createDocumentFragment();
          var prev = null;
          Array.from(c.textContent).forEach(function (ch) {
            if (prev && /[。、，．]/.test(ch)) { prev.textContent += ch; return; }
            var sp = d.createElement('span');
            sp.className = 'ch'; sp.textContent = ch;
            var topHero = !!h1.closest('.hero');
            sp.style.animationDelay = (0.25 + (topHero ? introDelay : 0) + n++ * (topHero ? 0.11 : 0.06)) + 's';
            if (topHero) sp.style.animationDuration = '1.7s';
            f.appendChild(sp); prev = sp;
          });
          node.replaceChild(f, c);
        } else if (c.nodeType === 1 && c.tagName !== 'BR') { wrap(c); }
      });
    };
    h1.setAttribute('aria-label', h1.textContent.replace(/\s+/g, ''));
    wrap(h1);
    h1.classList.add('chars');
    if (h1.closest('.hero') && introDelay) {
      var tail = 0.25 + introDelay + n * 0.11 + 0.4;               // just after the last letter starts
      var seqEls = [['.hero-eyebrow', 0], ['.hero-sub', tail], ['.hero-actions', tail + 0.7]];
      seqEls.forEach(function (p) {
        var el = d.querySelector('.hero ' + p[0]); if (!el) return;
        el.classList.add('seq'); el.style.animationDelay = (p[0] === '.hero-eyebrow' ? 0.25 + introDelay : p[1]) + 's';
      });
    }
  }

  // Hero: hexagon "cells" (echo the logo) fade in at random spots, drift, fade out and reappear; gently parallaxed by the pointer
  var hero = d.querySelector('.hero, .page-hero');
  if (hero) {
    var light = true; var ink = light ? '11,127,117' : '255,255,255';
    var cv = d.createElement('canvas');
    cv.className = 'hero-fx'; cv.setAttribute('aria-hidden', 'true');
    hero.insertBefore(cv, hero.querySelector('.hero-inner'));
    var ctx = cv.getContext('2d'), W = 0, H = 0, dpr = Math.min(devicePixelRatio || 1, 2);
    var PAR = 52, cells = [], mx = 0, my = 0, tx = 0, ty = 0, visible = true;
    var spawnCell = function (c, first) {
      c.x = Math.random() * W; c.y = H * (0.05 + Math.random() * 0.9); c.r = 10 + Math.random() * 30;
      c.z = 0.3 + Math.random() * 0.9; c.rot = Math.random() * 6.28; c.vr = (Math.random() - .5) * 0.002;
      c.vy = -(0.03 + Math.random() * 0.07); c.a = 0.5 + Math.random() * 0.4; c.dot = Math.random() < 0.35;
      c.life = 3.6 + Math.random() * 3.6;                       // seconds visible
      c.age = first ? -Math.random() * 3.0 : 0;                 // staggered start
    };
    var resize = function () {
      W = hero.clientWidth; H = hero.clientHeight;
      cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      var count = Math.round(Math.min(30, Math.max(8, W * H / 24000)));
      cells = [];
      for (var i = 0; i < count; i++) { var c = {}; spawnCell(c, true); cells.push(c); }
    };
    var hex = function (c) {
      ctx.beginPath();
      for (var k = 0; k < 6; k++) {
        var ang = c.rot + k * Math.PI / 3;
        var px = c.x + tx * c.z * PAR + Math.cos(ang) * c.r, py = c.y + ty * c.z * PAR + Math.sin(ang) * c.r;
        k ? ctx.lineTo(px, py) : ctx.moveTo(px, py);
      }
      ctx.closePath();
    };
    var lastT = 0;
    var frame = function () {
      if (!visible) { lastT = 0; return; }
      var now = Date.now(), dt = lastT ? Math.min((now - lastT) / 1000, 0.1) : 0.033; lastT = now;
      tx += (mx - tx) * 0.055; ty += (my - ty) * 0.055;
      ctx.clearRect(0, 0, W, H);
      cells.forEach(function (c) {
        c.age += dt;
        if (c.age < 0) return;
        if (c.age > c.life) { spawnCell(c, false); c.age = -Math.random() * 0.6; return; }
        c.y += c.vy * c.z * 60 * dt; c.rot += c.vr * 60 * dt;
        var u = c.age / c.life, s = Math.sin(Math.PI * u), env = Math.max(0, Math.min(1, s * s * (3 - 2 * Math.min(1, s * 1.6))));
        ctx.lineWidth = light ? 1.5 + c.z * 1.1 : 1.4 + c.z * 1.6;
        ctx.strokeStyle = 'rgba(' + ink + ',' + (light ? Math.min(1, c.a + 0.35) : c.a) * env + ')';
        ctx.fillStyle = light ? 'rgba(255,255,255,' + (0.16 * env) + ')' : 'rgba(' + ink + ',' + (c.a * 0.16) * env + ')';
        if (light) { ctx.shadowColor = 'rgba(255,255,255,' + (0.9 * env) + ')'; ctx.shadowBlur = 8; }
        else { ctx.shadowColor = 'rgba(8,40,50,.45)'; ctx.shadowBlur = 12; }
        hex(c); ctx.fill(); ctx.stroke();
        ctx.shadowBlur = 0;
        if (c.dot) { ctx.fillStyle = 'rgba(' + ink + ',' + env + ')'; ctx.beginPath(); ctx.arc(c.x + tx * c.z * PAR, c.y + ty * c.z * PAR, 2.8, 0, 6.28); ctx.fill(); }
      });
    };
    resize(); addEventListener('resize', resize);
    if (finePointer) hero.addEventListener('pointermove', function (e) {
      var r = hero.getBoundingClientRect();
      mx = (e.clientX - r.left) / r.width - .5; my = (e.clientY - r.top) / r.height - .5;
    });
    if ('IntersectionObserver' in window) new IntersectionObserver(function (en) { visible = en[0].isIntersecting; }).observe(hero);
    setInterval(frame, 33);                                   // timer-driven: keeps running without window focus

  }

  // Service cards: soft 3D tilt following the pointer
  if (finePointer) d.querySelectorAll('.service-card').forEach(function (card) {
    card.addEventListener('pointermove', function (e) {
      var r = card.getBoundingClientRect();
      var x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
      card.style.setProperty('--rx', (-y * 6).toFixed(2) + 'deg');
      card.style.setProperty('--ry', (x * 8).toFixed(2) + 'deg');
      card.style.setProperty('--gx', ((x + .5) * 100).toFixed(0) + '%');
      card.style.setProperty('--gy', ((y + .5) * 100).toFixed(0) + '%');
    });
    card.addEventListener('pointerleave', function () {
      card.style.setProperty('--rx', '0deg'); card.style.setProperty('--ry', '0deg');
    });
  });

  // Service cards: nine thin teal hexagons fade in at random spots, drift, fade out and reappear elsewhere (paused when off-screen)
  if (!reduce) d.querySelectorAll('.service-card .thumb, .sd-media').forEach(function (thumb) {
    var cv = d.createElement('canvas'); cv.className = 'thumb-fx'; cv.setAttribute('aria-hidden', 'true');
    thumb.appendChild(cv);
    var ctx = cv.getContext('2d'), dpr = Math.min(devicePixelRatio || 1, 2);
    var W = 0, H = 0, hexes = [], px = 0, py = 0, tx = 0, ty = 0, run = false, raf = 0;
    var spawn = function (h, first) {
      var k = Math.max(1, W / 360);
      h.x = W * (0.06 + Math.random() * 0.88); h.y = H * (0.08 + Math.random() * 0.84);
      h.r = (8 + Math.random() * 12) * k; h.z = 0.5 + Math.random() * 0.7;
      h.rot = Math.random() * 6.28; h.vr = (Math.random() - .5) * 0.004; h.vy = -(0.04 + Math.random() * 0.08);
      h.life = (thumb.classList.contains('sd-media') ? 4.2 : 2.6) + Math.random() * 2.6;   // seconds visible
      h.age = first ? -Math.random() * (thumb.classList.contains('sd-media') ? 2.2 : 3.5) : 0;   // negative = waiting to appear (staggered start)
    };
    var layout = function () {
      W = thumb.clientWidth; H = thumb.clientHeight;
      cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      hexes = [];
      var big = thumb.classList.contains('sd-media'); var total = big ? 20 : 9;
      for (var i = 0; i < total; i++) { var h = {}; spawn(h, true); hexes.push(h); }
    };
    var last = 0;
    var draw = function () {
      if (!run) return;
      var now = Date.now();
      var dt = last ? Math.min((now - last) / 1000, 0.1) : 0.016; last = now;
      tx += (px - tx) * 0.07; ty += (py - ty) * 0.07;
      ctx.clearRect(0, 0, W, H);
      ctx.fillStyle = 'rgba(11,127,117,.04)';
      ctx.shadowColor = 'rgba(255,255,255,.7)'; ctx.shadowBlur = 3;
      hexes.forEach(function (h) {
        h.age += dt;
        if (h.age < 0) return;                                  // not born yet
        if (h.age > h.life) { spawn(h, false); h.age = -Math.random() * (thumb.classList.contains('sd-media') ? 0.3 : 0.8); return; }
        h.y += h.vy * h.z * 60 * dt; h.rot += h.vr * 60 * dt;
        var u = h.age / h.life;
        var env = Math.sin(Math.PI * u); env = env * env * (3 - 2 * Math.min(1, env * 1.6));   // soft in, soft out
        ctx.lineWidth = 1.2 + h.z * 0.9;
        ctx.strokeStyle = 'rgba(11,127,117,.85)';
        ctx.beginPath();
        for (var k = 0; k < 6; k++) {
          var a = h.rot + k * Math.PI / 3;
          var x = h.x + tx * h.z * 18 + Math.cos(a) * h.r, y = h.y + ty * h.z * 18 + Math.sin(a) * h.r;
          k ? ctx.lineTo(x, y) : ctx.moveTo(x, y);
        }
        // fade out near the bottom-left corner so the card number stays readable
        var fx = Math.max(0, Math.min(1, (h.x - W * 0.2) / (W * 0.12)));
        var fy = Math.max(0, Math.min(1, (H * 0.88 - h.y) / (H * 0.2)));
        ctx.globalAlpha = Math.max(0, Math.min(1, env)) * Math.max(fx, fy);
        ctx.closePath(); ctx.fill(); ctx.stroke();
        ctx.globalAlpha = 1;
      });
    };
    layout(); addEventListener('resize', layout);
    if (finePointer) (thumb.closest('.service-card') || thumb).addEventListener('pointermove', function (e) {
      var r = thumb.getBoundingClientRect();
      px = (e.clientX - r.left) / r.width - .5; py = (e.clientY - r.top) / r.height - .5;
    });
    (thumb.closest('.service-card') || thumb).addEventListener('pointerleave', function () { px = 0; py = 0; });
    var start = function () { if (!run) { run = true; last = 0; raf = setInterval(draw, 33); } }, stop = function () { run = false; clearInterval(raf); };
    // run only while on screen: scroll check works everywhere, IntersectionObserver is an extra trigger
    var onScreen = function () { var r = thumb.getBoundingClientRect(); return r.bottom > -40 && r.top < innerHeight + 40; };
    var sync = function () { onScreen() ? start() : stop(); };
    addEventListener('scroll', sync, { passive: true }); addEventListener('resize', sync); sync();
    if ('IntersectionObserver' in window) new IntersectionObserver(function (en) { en[0].isIntersecting ? start() : sync(); }).observe(thumb);
  });

})();
