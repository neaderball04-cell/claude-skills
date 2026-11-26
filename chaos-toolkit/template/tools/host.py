"""Inject Sparky (original cartoon radio host) into every built scene."""
import json, re, wave, os
import numpy as np
ROOT = '/home/claude/t2c2/video'
T = json.load(open(f'{ROOT}/work/timing.json'))

SVG = '<div id="SID-hb" style="position:absolute;left:0;top:0;width:404px;height:381px"><div id="SID-body" style="position:absolute;inset:0"><div class="SID-p" id="SID-p-c" style="position:absolute;inset:0;opacity:1"><img class="SID-m0" src="assets/img/sp3/c_m0.png" style="position:absolute;left:0;top:0;width:404px;height:381px;opacity:1"><img class="SID-m1" src="assets/img/sp3/c_m1.png" style="position:absolute;left:0;top:0;width:404px;height:381px;opacity:0"><img class="SID-m2" src="assets/img/sp3/c_m2.png" style="position:absolute;left:0;top:0;width:404px;height:381px;opacity:0"><img class="SID-m3" src="assets/img/sp3/c_m3.png" style="position:absolute;left:0;top:0;width:404px;height:381px;opacity:0"></div><div class="SID-p" id="SID-p-l" style="position:absolute;inset:0;opacity:0"><img class="SID-m0" src="assets/img/sp3/l_m0.png" style="position:absolute;left:0;top:0;width:404px;height:381px;opacity:1"><img class="SID-m1" src="assets/img/sp3/l_m1.png" style="position:absolute;left:0;top:0;width:404px;height:381px;opacity:0"><img class="SID-m2" src="assets/img/sp3/l_m2.png" style="position:absolute;left:0;top:0;width:404px;height:381px;opacity:0"><img class="SID-m3" src="assets/img/sp3/l_m3.png" style="position:absolute;left:0;top:0;width:404px;height:381px;opacity:0"></div><div class="SID-p" id="SID-p-r" style="position:absolute;inset:0;opacity:0"><img class="SID-m0" src="assets/img/sp3/r_m0.png" style="position:absolute;left:0;top:0;width:404px;height:381px;opacity:1"><img class="SID-m1" src="assets/img/sp3/r_m1.png" style="position:absolute;left:0;top:0;width:404px;height:381px;opacity:0"><img class="SID-m2" src="assets/img/sp3/r_m2.png" style="position:absolute;left:0;top:0;width:404px;height:381px;opacity:0"><img class="SID-m3" src="assets/img/sp3/r_m3.png" style="position:absolute;left:0;top:0;width:404px;height:381px;opacity:0"></div><div class="SID-p" id="SID-p-pr0" style="position:absolute;inset:0;opacity:0"><img class="SID-m0" src="assets/img/sp3/pr0_m0.png" style="position:absolute;left:0;top:0;width:404px;height:381px;opacity:1"><img class="SID-m1" src="assets/img/sp3/pr0_m1.png" style="position:absolute;left:0;top:0;width:404px;height:381px;opacity:0"><img class="SID-m2" src="assets/img/sp3/pr0_m2.png" style="position:absolute;left:0;top:0;width:404px;height:381px;opacity:0"><img class="SID-m3" src="assets/img/sp3/pr0_m3.png" style="position:absolute;left:0;top:0;width:404px;height:381px;opacity:0"></div><div class="SID-p" id="SID-p-pr" style="position:absolute;inset:0;opacity:0"><img class="SID-m0" src="assets/img/sp3/pr_m0.png" style="position:absolute;left:0;top:0;width:404px;height:381px;opacity:1"><img class="SID-m1" src="assets/img/sp3/pr_m1.png" style="position:absolute;left:0;top:0;width:404px;height:381px;opacity:0"><img class="SID-m2" src="assets/img/sp3/pr_m2.png" style="position:absolute;left:0;top:0;width:404px;height:381px;opacity:0"><img class="SID-m3" src="assets/img/sp3/pr_m3.png" style="position:absolute;left:0;top:0;width:404px;height:381px;opacity:0"></div><div class="SID-p" id="SID-p-pl0" style="position:absolute;inset:0;opacity:0"><img class="SID-m0" src="assets/img/sp3/pl0_m0.png" style="position:absolute;left:0;top:0;width:404px;height:381px;opacity:1"><img class="SID-m1" src="assets/img/sp3/pl0_m1.png" style="position:absolute;left:0;top:0;width:404px;height:381px;opacity:0"><img class="SID-m2" src="assets/img/sp3/pl0_m2.png" style="position:absolute;left:0;top:0;width:404px;height:381px;opacity:0"><img class="SID-m3" src="assets/img/sp3/pl0_m3.png" style="position:absolute;left:0;top:0;width:404px;height:381px;opacity:0"></div><div class="SID-p" id="SID-p-pl" style="position:absolute;inset:0;opacity:0"><img class="SID-m0" src="assets/img/sp3/pl_m0.png" style="position:absolute;left:0;top:0;width:404px;height:381px;opacity:1"><img class="SID-m1" src="assets/img/sp3/pl_m1.png" style="position:absolute;left:0;top:0;width:404px;height:381px;opacity:0"><img class="SID-m2" src="assets/img/sp3/pl_m2.png" style="position:absolute;left:0;top:0;width:404px;height:381px;opacity:0"><img class="SID-m3" src="assets/img/sp3/pl_m3.png" style="position:absolute;left:0;top:0;width:404px;height:381px;opacity:0"></div></div></div>'

CSS = '''
    
    .host { position:absolute; left:0; top:0; width:404px; height:381px; z-index:50; pointer-events:none; filter:drop-shadow(0 12px 6px rgba(0,0,0,.35)); }
'''

JS = r'''
    (() => {
      const S = "SID", D = DATA, H = "#" + S + "-host";
      const tgt = (sel) => { const b = D.box[sel.slice(1)]; return b ? { x:b[0] + b[2] / 2, y:b[1] + b[3] / 2 } : null; };
      const FX = 217, FY = 381, SHXR = 87, SHXL = -90, SHY = -278, HO = "217px 381px", BO = "217px 300px";
      const occ = [];
      for (const id in D.box) { const [x, y, w, h] = D.box[id]; if ((w > 1500 && h > 800) || id.endsWith("-rail")) continue; const wt = id.endsWith("-h") ? 3 : 1; occ.push([x - 16, y - 16, x + w + 16, y + h + 16, wt]); }
      const ovl = (fx, fy) => { const b = [fx - 175, fy - 350, fx + 175, fy]; let a = 0;
        for (const o of occ) { const w = Math.min(b[2], o[2]) - Math.max(b[0], o[0]), h = Math.min(b[3], o[3]) - Math.max(b[1], o[1]); if (w > 0 && h > 0) a += w * h * (o[4] || 1); } return a; };
      const cands = [];
      for (let fx = 200; fx <= 1720; fx += 40) for (let fy = 470; fy <= 1075; fy += 30) cands.push([fx, fy, ovl(fx, fy)]);
      let cx = 1720, cy = 1040;
      const pick = (p) => { let best = null, bc = 1e18;
        for (const [fx, fy, ov] of cands) { const d = Math.hypot(p.x - (fx + (p.x > fx ? SHXR : SHXL)), p.y - (fy + SHY));
          const c = ov * 0.6 + Math.abs(d - 320) + 0.35 * Math.hypot(fx - cx, fy - cy); if (c < bc) { bc = c; best = [fx, fy]; } }
        return best; };
      if (D.points.length) { const p0 = tgt(D.points[0][1]); if (p0) [cx, cy] = pick(p0); }
      tl.set(H, { x:cx - FX, y:cy - FY + 700 }, 0);
      tl.to(H, { y:cy - FY, duration:0.7, ease:"back.out(1.6)" }, 0.05);
      // pose timeline
      const poseEv = [[0, "c"]];
      let last = -9, busyUntil = 0;
      for (const [t, sel] of D.points) {
        const p = tgt(sel); if (!p) continue;
        if (t - last > 1.8 && t > busyUntil) {
          const [nx, ny] = pick(p); const dist = Math.hypot(nx - cx, ny - cy);
          if (dist > 40) {
            const t0 = Math.max(0.8, t - 0.85), d = dist > 420 ? 0.85 : 0.75;
            tl.to(H, { x:nx - FX, duration:d, ease:"sine.inOut" }, t0);
            if (dist > 420) tl.to(H, { keyframes:[{ y:Math.max(470, Math.min(cy, ny) - 140) - FY, duration:d / 2, ease:"sine.out" }, { y:ny - FY, duration:d / 2, ease:"sine.in" }] }, t0);
            else tl.to(H, { keyframes:[{ y:(cy + ny) / 2 - FY - 40, duration:d / 2, ease:"sine.out" }, { y:ny - FY, duration:d / 2, ease:"sine.in" }] }, t0);
            tl.to("#" + S + "-hb", { keyframes:[{ scaleY:0.92, scaleX:1.05, duration:0.1, ease:"sine.out" }, { scaleY:1, scaleX:1, duration:0.2, ease:"sine.inOut" }], transformOrigin:HO }, t0 + d - 0.05);
            poseEv.push([t0, nx > cx ? "r" : "l"]); poseEv.push([t0 + d, "c"]);
            busyUntil = t0 + d + 0.3; cx = nx; cy = ny;
          }
        }
        const right = p.x >= cx;
        poseEv.push([t - 0.25, right ? "pr0" : "pl0"]); poseEv.push([t - 0.12, right ? "pr" : "pl"]);
        poseEv.push([t + 1.45, right ? "pr0" : "pl0"]); poseEv.push([t + 1.58, "c"]);
        tl.to("#" + S + "-body", { x:right ? 6 : -6, duration:0.25, ease:"sine.inOut", yoyo:true, repeat:1 }, t);
        last = t;
      }
      poseEv.sort((a, b) => a[0] - b[0]);
      let cur = "c";
      for (const [t, p] of poseEv) { if (p === cur) continue; tl.set("#" + S + "-p-" + cur, { opacity:0 }, Math.max(0, t)); tl.set("#" + S + "-p-" + p, { opacity:1 }, Math.max(0, t)); cur = p; }
      for (const t of D.hops) {
        tl.to("#" + S + "-hb", { keyframes:[{ scaleY:0.9, scaleX:1.06, y:6, duration:0.14, ease:"sine.out" }, { scaleY:1.05, scaleX:0.97, y:-110, duration:0.3, ease:"sine.out" },
          { scaleY:1, scaleX:1, y:0, duration:0.3, ease:"sine.in" }, { scaleY:0.95, scaleX:1.03, duration:0.08 }, { scaleY:1, scaleX:1, duration:0.14, ease:"sine.out" }], transformOrigin:HO }, t);
      }
      for (const t of D.gags) tl.to("#" + S + "-hb", { keyframes:[{ rotation:4, duration:0.16 }, { rotation:-4, duration:0.16 }, { rotation:4, duration:0.16 }, { rotation:-4, duration:0.16 }, { rotation:0, duration:0.2 }], ease:"sine.inOut", transformOrigin:HO }, t + 0.1);
      // mouth: 4 levels, swap sprites
      let ml = 0;
      for (const [t, v] of D.mouth) { const lv = v < 0.12 ? 0 : v < 0.4 ? 1 : v < 0.7 ? 2 : 3;
        if (lv !== ml) { tl.set("#" + S + "-host .SID-m" + ml, { opacity:0 }, t); tl.set("#" + S + "-host .SID-m" + lv, { opacity:1 }, t); ml = lv; } }
      // breathing + talk bob
      const n = Math.ceil(D.dur / 1.6);
      tl.fromTo("#" + S + "-hb", { scaleY:1 }, { scaleY:1.015, transformOrigin:HO, duration:1.6, ease:"sine.inOut", yoyo:true, repeat:n, immediateRender:false }, 0.8);
      for (const [t, v] of D.bob) tl.to("#" + S + "-body", { y:-v * 5, rotation:v * D.wob * 0.5, transformOrigin:BO, duration:0.3, ease:"sine.inOut" }, t);
      for (const t of D.listen) tl.to("#" + S + "-hb", { rotation:4, transformOrigin:HO, duration:0.4, ease:"sine.inOut" }, t);
      for (const t of D.unlisten) tl.to("#" + S + "-hb", { rotation:0, duration:0.4, ease:"sine.inOut" }, t);
    })();
'''

BOX = json.load(open(f'{ROOT}/work/boxes.json'))
JOKES = json.load(open(f'{ROOT}/work/jokes.json'))
HOP_WORDS = ('Step', 'Hey hey', 'Rule time', 'Uh oh', 'Now, back')


def env(lid, sr_fps=15):
    import soundfile as _sf
    x, sr = _sf.read(f'{ROOT}/work/cl_{lid}.wav', dtype='float32', always_2d=True); x = x.mean(1)
    hop = sr // sr_fps
    e = np.array([np.sqrt(np.mean(x[i * hop:(i + 1) * hop] ** 2)) for i in range(len(x) // hop)])
    return e


def run():
    allv = np.concatenate([env(l) for s in T.values() if isinstance(s, dict) and 'lines' in s for l, v in s['lines'].items() if v['voice'] == 'n'])
    ref = np.percentile(allv[allv > 0.005], 90)
    for sid, sc in T.items():
        if not isinstance(sc, dict) or 'lines' not in sc:
            continue
        fn = f'{ROOT}/compositions/{sid}.html'
        h = open(fn).read()
        if f'{sid}-host' in h:
            continue
        calm = sid == 's13'
        js_part = h[h.index('const tl = gsap.timeline'):]
        pts = []
        for m in re.finditer(r'\b(show|pop|slam)\("(#[\w-]+)",\s*([0-9.+\- ]+?)\s*[,)]', js_part):
            try:
                t = eval(m.group(3))
            except Exception:
                continue
            sel = m.group(2)
            if sel.endswith('-rail') or sel.endswith('-h') or sel in (f'#{sid}-logo',):
                continue
            pts.append((round(t, 2), sel))
        pts.sort()
        thin = []
        for t, s in pts:
            if not thin or t - thin[-1][0] > 0.9:
                thin.append([t, s])
        mouth, bob, hops, listen, unlisten, gags = [], [], [], [], [], []
        for lid, l in sc['lines'].items():
            if l['voice'] != 'n':
                listen.append(round(l['start'], 2)); unlisten.append(round(l['end'], 2)); continue
            e = np.clip(env(lid) / ref, 0, 1)
            e = np.convolve(e, [0.25, 0.5, 0.25], mode='same')
            e10 = np.interp(np.arange(0, len(e) / 15, 0.1), np.arange(len(e)) / 15, e)
            e10 = np.where(e10 < 0.12, 0, e10) ** 0.75
            for i, v in enumerate(e10):
                mouth.append([round(l['start'] + i * 0.1, 2), round(float(min(1, v)), 2)])
            mouth.append([round(l['start'] + len(e10) * 0.1, 2), 0])
            for i in range(0, len(e10), 3):
                bob.append([round(l['start'] + i * 0.1, 2), round(float(e10[i:i + 3].mean()) * (0.4 if calm else 1), 2)])
            if lid in JOKES:
                gags.append(round(l['start'] + (l['end'] - l['start']) * (1 - len(JOKES[lid]) / len(l['text'])) + 0.3, 2))
            if not calm and l['text'].startswith(HOP_WORDS):
                hops.append(round(l['start'], 2))
            if not calm and lid != 'n7' and len(thin) == 0:
                pass
        side0 = 'R'
        data = dict(box=BOX.get(sid, {}), gags=gags, points=thin, mouth=mouth, bob=bob, hops=hops, listen=listen, unlisten=unlisten, dur=sc['dur'], side0=side0, wob=1 if calm else 3)
        html = f'<div class="host" id="{sid}-host" data-layout-ignore>' + SVG.replace('SID', sid) + '</div>'
        h = h.replace('    </div></div>\n  </div>\n  <script>', '    </div></div>\n' + html + '\n  </div>\n  <script>', 1)
        h = h.replace('  </style>', CSS + '  </style>', 1)
        h = h.replace(f'    window.__timelines["{sid}"] = tl;', JS.replace('SID', sid).replace('DATA', json.dumps(data)) + f'    window.__timelines["{sid}"] = tl;', 1)
        assert f'{sid}-host' in h and 'const S = ' in h, sid
        open(fn, 'w').write(h)
        print(sid, len(thin), 'points', len(hops), 'hops')


run()
