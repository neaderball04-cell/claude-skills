#!/usr/bin/env python3
"""Builds index.html and compositions/sNN.html from scene templates + voice timing.
Scene templates live in tools/scenes_*.py as plain strings with @@tokens@@:
  @@n8@@            start of voice line n8 (seconds, scene-local)
  @@n8.end@@        end of that line
  @@n8:phrase@@     estimated moment the phrase is spoken inside the line
  @@DUR@@           scene duration
  @@STEEL:p@@ @@PAPER:p@@ @@RIDGE:p@@ @@JS@@   shared snippets
"""
import json, math, os, re, sys
ROOT = '/home/claude/t2c2/video'
os.chdir(ROOT)
sys.path.insert(0, os.path.join(ROOT, 'tools'))
T = json.load(open('work/timing.json'))

# ---------------------------------------------------------------- shared art
def steel(p):
    return '''<svg class="full" viewBox="0 0 1920 1080" data-layout-ignore>
  <rect width="1920" height="1080" fill="#c4572f"/>
  <rect x="16" y="16" width="1888" height="1048" rx="30" fill="#1c1c1f"/>
  <rect x="22" y="22" width="1876" height="1036" rx="26" fill="none" stroke="#e9e4da" stroke-width="2" opacity=".35"/>
</svg>'''

def contours(seed=1, hills=((520, 330, 300), (1480, 780, 360), (1650, 180, 220))):
    out = []
    for hi, (cx, cy, rmax) in enumerate(hills):
        k = 0
        r = 46
        while r < rmax:
            pts = []
            for i in range(0, 73):
                a = i / 72 * 2 * math.pi
                rr = r * (1 + 0.16 * math.sin(3 * a + seed + hi * 1.7 + k * 0.35) + 0.09 * math.sin(5 * a + seed * 2.1 + hi) + 0.05 * math.sin(7 * a + k))
                pts.append(f'{cx + rr * math.cos(a) * 1.25:.1f} {cy + rr * math.sin(a):.1f}')
            out.append('<path d="M' + 'L'.join(pts) + 'Z"/>')
            r += 52
            k += 1
    return ''.join(out)

def paper(p, grid='', seed=1):
    return f'''<svg class="full" viewBox="0 0 1920 1080" data-layout-ignore>
  <rect width="1920" height="1080" fill="#e3dbc8"/>
  <g fill="none" stroke="#cdbf9f" stroke-width="3">{contours(seed)}</g>
  {grid}
</svg>'''

def bmp(x, y, s=1.0, flip=False):
    """Side-view tracked IFV silhouette, ~150x60 at s=1, lit along its top edge."""
    sx = -s if flip else s
    return f'''<g transform="translate({x} {y}) scale({sx} {s})">
  <path d="M-74 22L-66 4L-30 -2L-18 -16L22 -16L30 -2L62 2L76 14L70 30L-66 30Z" fill="#0b0c0e"/>
  <path d="M-12 -16L-8 -30L20 -30L24 -16Z" fill="#0b0c0e"/>
  <path d="M20 -25H74" stroke="#0b0c0e" stroke-width="5"/>
  <path d="M-66 4L-30 -2L-18 -16L-12 -16L-8 -30L20 -30L24 -16L30 -2L62 2L76 14" fill="none" stroke="#d9722a" stroke-width="2.5"/>
  <g fill="#050506"><circle cx="-52" cy="30" r="9"/><circle cx="-30" cy="32" r="9"/><circle cx="-8" cy="32" r="9"/><circle cx="14" cy="32" r="9"/><circle cx="36" cy="32" r="9"/><circle cx="56" cy="30" r="9"/></g>
</g>'''

def ridge(p, mast=True, bmps=True, anim=False):
    """Dusk ridge world. Layers are separate elements so a scene can drift them."""
    mast_svg = f'''
  <g id="{p}-mast">
    <path d="M250 676V246" stroke="#0a0b0c" stroke-width="9"/>
    <path d="M250 300L150 692M250 300L352 716M250 430L190 688M250 430L312 706" stroke="#0a0b0c" stroke-width="2.5" fill="none"/>
    <path d="M226 246H274M232 276H268M250 246V206" stroke="#0a0b0c" stroke-width="6"/>
    <circle cx="250" cy="204" r="6" fill="#d8352c"/>
  </g>''' if mast else ''
    bmps_svg = f'''<g id="{p}-bmps">{bmp(1290, 786, 1.0)}{bmp(1470, 804, 1.0)}</g>''' if bmps else ''
    return f'''<svg class="full" viewBox="0 0 1920 1080" data-layout-ignore>
  <defs>
    <linearGradient id="{p}-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0f1013"/><stop offset=".5" stop-color="#1e1a1c"/><stop offset=".78" stop-color="#5c1d17"/><stop offset=".93" stop-color="#b8361d"/><stop offset="1" stop-color="#e07a2c"/></linearGradient>
    <linearGradient id="{p}-val" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3a2a26"/><stop offset="1" stop-color="#1c1b1d"/></linearGradient>
  </defs>
  <rect width="1920" height="700" fill="url(#{p}-sky)"/>
  <g id="{p}-far"><path d="M-80 660L60 612L200 640L380 566L560 628L760 580L940 632L1130 590L1330 636L1520 598L1720 640L2000 600V760H-80Z" fill="#17171a"/>
    <path d="M-80 660L60 612L200 640L380 566L560 628L760 580L940 632L1130 590L1330 636L1520 598L1720 640L2000 600" fill="none" stroke="#7a2a1c" stroke-width="2"/></g>
  <rect y="690" width="1920" height="390" fill="url(#{p}-val)"/>
  <path d="M700 1080C900 900 1150 820 1920 790V830C1250 850 1000 930 860 1080Z" fill="#4a3a33" opacity=".55"/>
  {bmps_svg}
  <g id="{p}-near">
    <path d="M-60 1080V694L120 652L300 702L470 762L640 832L820 902L1000 962L1200 1012L1400 1052L1620 1080Z" fill="#0a0b0c"/>
    <path d="M330 706L346 672L470 672L506 700L520 748L330 742Z" fill="#0a0b0c"/>
    <path d="M360 672V640M372 640H348" stroke="#0a0b0c" stroke-width="4"/>
    <g fill="#0a0b0c"><circle cx="590" cy="760" r="13"/><path d="M574 836L578 778L604 778L610 846Z"/><circle cx="650" cy="790" r="13"/><path d="M634 866L638 808L664 808L670 876Z"/></g>
    {mast_svg}
  </g>
</svg>'''

def burst(bid, x, y, size=130, cls='h'):
    return f'''<div class="burst {cls}" id="{bid}" style="left:{x}px;top:{y}px;width:{size}px;height:{size}px;margin:-{size//2}px 0 0 -{size//2}px"><svg viewBox="-60 -60 120 120" width="{size}" height="{size}"><path d="M0 -56L13 -19L52 -30L26 4L56 34L17 30L0 60L-17 30L-56 34L-26 4L-52 -30L-13 -19Z" fill="#1b1d20"/><path d="M0 -30L8 -10L28 -16L14 3L30 19L9 17L0 33L-9 17L-30 19L-14 3L-28 -16L-8 -10Z" fill="#d8352c"/><circle r="9" fill="#f0b84a"/></svg></div>'''

def reticle(rid, x, y, size=220, cls='h', color='#d8352c', sw=7):
    h = size // 2
    return f'''<div class="ret {cls}" id="{rid}" style="left:{x}px;top:{y}px;width:{size}px;height:{size}px;margin:-{h}px 0 0 -{h}px"><svg viewBox="-100 -100 200 200" width="{size}" height="{size}"><circle r="62" fill="none" stroke="{color}" stroke-width="{sw}"/><path d="M-96 0H-34M34 0H96M0 -96V-34M0 34V96" stroke="{color}" stroke-width="{sw}"/></svg></div>'''

CSS = '''
    #root { position:absolute; inset:0; overflow:hidden; font-family:"Oswald",sans-serif; color:#efe9dc; }
    .full { position:absolute; left:0; top:0; width:1920px; height:1080px; }
    .stage { position:absolute; inset:0; overflow:hidden; }
    .cam { position:absolute; inset:0; }
    .h { opacity:0; }
    .abs { position:absolute; }
    .disp { font-family:"Archivo Black",sans-serif; text-transform:uppercase; line-height:1; white-space:nowrap; }
    .lab { font-family:"Oswald",sans-serif; font-weight:600; text-transform:uppercase; letter-spacing:.12em; line-height:1.1; white-space:nowrap; }
    .mono { font-family:"JetBrains Mono",monospace; font-weight:700; line-height:1.1; white-space:pre; }
    .chip { position:absolute; background:#d9a63a; color:#1b1d20; font-family:"Oswald",sans-serif; font-weight:600; font-size:40px; letter-spacing:.16em; text-transform:uppercase; padding:10px 22px 12px; line-height:1; white-space:nowrap; }
    .burst, .ret { position:absolute; }
    .tape { position:absolute; left:192px; top:834px; width:1536px; height:150px; background:#1b1d20; border-left:18px solid #d9a63a; box-shadow:0 12px 0 rgba(0,0,0,.28); display:flex; align-items:center; padding-left:34px; }
    .tape.fdc { border-left-color:#d8352c; }
    .tape .who { position:absolute; left:-18px; top:-52px; height:52px; background:#d9a63a; color:#1b1d20; font-family:"Oswald",sans-serif; font-weight:600; font-size:32px; letter-spacing:.16em; padding:0 20px; display:flex; align-items:center; white-space:nowrap; }
    .tape.fdc .who { background:#d8352c; color:#fff; }
    .tape .tx { font-family:"JetBrains Mono",monospace; font-weight:700; color:#efe9dc; white-space:pre; line-height:1; }
    .tape .tx span { display:inline-block; }
    .mtr { position:absolute; right:30px; top:50%; height:70px; margin-top:-35px; display:flex; gap:8px; align-items:center; }
    .mtr i { display:block; width:10px; height:70px; background:#d9a63a; }
    .tape.fdc .mtr i { background:#d8352c; }
'''

JS = '''
    const tl = gsap.timeline({ paused: true });
    const ZERO = { x:0, y:0, scale:1, scaleX:1, scaleY:1, rotation:0 };
    const show = (s, t, d = 0.45, from = {}, ease = "expo.out") => {
      const to = { opacity:1, duration:d, ease };
      for (const k in from) if (k in ZERO) to[k] = ZERO[k];
      return tl.fromTo(s, Object.assign({ opacity:0 }, from), to, t);
    };
    const hide = (s, t, d = 0.22, to = {}) => tl.to(s, Object.assign({ opacity:0, duration:d, ease:"power2.in" }, to), t);
    const shake = (s, t, a = 12) => tl.to(s, { keyframes:[
      { x:-a, y:a*0.6, duration:0.04 }, { x:a*0.8, y:-a*0.5, duration:0.05 }, { x:-a*0.5, y:a*0.3, duration:0.05 },
      { x:a*0.25, y:0, duration:0.05 }, { x:0, y:0, duration:0.06 } ], ease:"none" }, t);
    const slam = (s, t, cam, a = 12, from = 1.8) => {
      tl.fromTo(s, { opacity:0, scale:from }, { opacity:1, scale:1, duration:0.2, ease:"power4.in" }, t);
      if (cam) shake(cam, t + 0.2, a);
    };
    const draw = (s, t, d = 0.6, ease = "power2.inOut") => tl.fromTo(s, { strokeDashoffset:1 }, { strokeDashoffset:0, duration:d, ease }, t);
    const meter = (sel, t0, t1) => document.querySelectorAll(sel + " i").forEach((el, i) => {
      const n = Math.max(1, Math.floor((t1 - t0) / 0.16));
      tl.fromTo(el, { scaleY:0.18 }, { scaleY:1, duration:0.16, repeat:n, yoyo:true, ease:"sine.inOut" }, t0 + i * 0.045);
      tl.to(el, { scaleY:0.18, duration:0.12 }, t0 + i * 0.045 + (n + 1) * 0.16);
    });
    const sp = (s, t, d = 0.32) => tl.fromTo(s, { opacity:0, scale:0.2, transformOrigin:"50% 50%" }, { opacity:1, scale:1, duration:d, ease:"back.out(2.2)" }, t);
    const pop = (s, t, d = 0.3) => tl.fromTo(s, { opacity:0, scale:0.2 }, { opacity:1, scale:1, duration:d, ease:"back.out(2.2)" }, t);
'''

def tape(tid, who, tokens, size=84, fdc=False, top=834):
    spans = ''.join(f'<span class="h" id="{tid}-k{i}">{tok}</span>' for i, tok in enumerate(tokens))
    return f'''<div class="tape{' fdc' if fdc else ''} h" id="{tid}" style="top:{top}px"><div class="who">{who}</div><div class="tx" style="font-size:{size}px">{spans}</div><div class="mtr" id="{tid}-m"><i></i><i></i><i></i><i></i><i></i></div></div>'''

# ---------------------------------------------------------------- tokens
def cue(sid, lid, phrase=None, end=False):
    ln = T[sid]['lines'][lid]
    if end:
        return ln['end']
    if not phrase:
        return ln['start']
    txt = ln['text'].lower()
    i = txt.find(phrase.lower())
    if i < 0:
        raise SystemExit(f'cue phrase not found: {sid} {lid} "{phrase}" in "{ln["text"]}"')
    return round(ln['start'] + (i / len(txt)) * (ln['end'] - ln['start']), 2)

def render(sid, tpl):
    def rep(m):
        k = m.group(1)
        if k == 'DUR':
            return str(T[sid]['dur'])
        if k == 'JS':
            return JS
        if k == 'CSS':
            return CSS
        if k.startswith('STEEL:'):
            return steel(k[6:])
        if k.startswith('EXPR:'):
            return str(round(eval(k[5:], {'c': lambda lid, ph=None: cue(sid, lid, ph), 'e': lambda lid: cue(sid, lid, end=True), 'D': T[sid]['dur']}), 3))
        if k.endswith('.end'):
            return str(cue(sid, k[:-4], end=True))
        if ':' in k:
            lid, ph = k.split(':', 1)
            return str(cue(sid, lid, ph))
        return str(cue(sid, k))
    return re.sub(r'@@([^@]+)@@', rep, tpl)

# ---------------------------------------------------------------- assemble
import scenes
SC = scenes.build(globals())

order = [f's{i:02d}' for i in range(1, 30) if f's{i:02d}' in T]
OVERLAP = 0.6
hosts, audio = [], []
total = T['_total']
for i, sid in enumerate(order):
    st, du = T[sid]['start'], T[sid]['dur']
    slot = round(du + (OVERLAP if i < len(order) - 1 else 0), 2)
    open(f'compositions/{sid}.html', 'w').write(render(sid, SC[sid]))
    hosts.append(f'      <div id="{sid}" data-composition-id="{sid}" data-composition-src="compositions/{sid}.html" data-start="{st}" data-duration="{slot}" data-track-index="{1 + i % 2}" data-track-kind="graphics" data-width="1920" data-height="1080" style="z-index:{i + 1}" data-layout-allow-overlap></div>')
    audio.append(f'      <audio id="vo-{sid}" class="clip" src="assets/voice/{sid}.wav" data-start="{st}" data-duration="{du}" data-track-index="10" data-volume="1"></audio>')

def g(sid, local):
    return round(T[sid]['start'] + local, 3)
sfx = []
def add(i, f, start, dur, vol, extra=''):
    sfx.append(f'      <audio id="sfx-{i}" class="clip" src="assets/sfx/{f}" data-start="{max(0, round(start, 3))}" data-duration="{dur}" data-track-index="{11 + len(sfx)}" data-volume="{vol}"{extra}></audio>')
for item in scenes.SFX(cue):
    sid, local, f, dur, vol = item[:5]
    add(f'x{len(sfx)}', f, g(sid, local), dur, vol, item[5] if len(item) > 5 else '')

index = f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <title>CHAOS T2C2 Lite</title>
    <script src="lib/gsap.min.js"></script>
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ margin: 0; width: 1920px; height: 1080px; overflow: hidden; background: #1b1d20; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{total}" data-width="1920" data-height="1080">
{chr(10).join(hosts)}
{chr(10).join(audio)}
{chr(10).join(sfx)}
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
'''
open('index.html', 'w').write(index)
print('built', len(order), 'scenes, total', total)
