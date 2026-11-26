"""CHAOS MDMP fundamentals — s01-s14."""
from base import wrap
from jb import it
from ea import svg, card, person, ic
from kit import CSS as KCSS, li, tile, num, quote, H1, WIPE, OUT, DRIFT

STEPS = ['Receipt', 'Mission analysis', 'COA dev', 'War game', 'Compare', 'Approve', 'Orders']

THEME = '''
    @font-face { font-family:"Alfa Slab One"; font-weight:400; src:url("assets/fonts/alfa-slab-one-latin-400-normal.woff2") format("woff2"); }
    @font-face { font-family:"Barlow"; font-weight:400; src:url("assets/fonts/barlow-latin-400-normal.woff2") format("woff2"); }
    @font-face { font-family:"Barlow"; font-weight:500; src:url("assets/fonts/barlow-latin-500-normal.woff2") format("woff2"); }
    @font-face { font-family:"Barlow"; font-weight:600; src:url("assets/fonts/barlow-latin-600-normal.woff2") format("woff2"); }
    @font-face { font-family:"Barlow Semi Condensed"; font-weight:600; src:url("assets/fonts/barlow-semi-condensed-latin-600-normal.woff2") format("woff2"); }
    @font-face { font-family:"Barlow Semi Condensed"; font-weight:700; src:url("assets/fonts/barlow-semi-condensed-latin-700-normal.woff2") format("woff2"); }
    .h1, .disp, .bigq, .tile b, .stp > div > span { font-family:"Alfa Slab One","Archivo Black",serif !important; letter-spacing:.01em; }
    .h1 { color:#e3963e !important; }
    .lab { font-family:"Barlow Semi Condensed","Oswald",sans-serif !important; font-weight:700 !important; color:#d4a24c !important; }
    .tile { background:#242427 !important; border:3px solid #b8893a !important; box-shadow:none !important; }
    .tile b { color:#e3963e !important; font-weight:400; }
    .tile i, .stp > div > i { font-family:"Barlow","Oswald",sans-serif !important; color:#d8d2c6 !important; }
    .stp { background:#242427 !important; border:3px solid #b8893a; box-shadow:none !important; }
    .stp > div > span { color:#e3963e !important; font-weight:400; }
    .chip { font-family:"Barlow Semi Condensed","Oswald",sans-serif !important; font-weight:700 !important; }
    .li { font-family:"Barlow Semi Condensed","Oswald",sans-serif !important; font-weight:700 !important; color:#ece6da !important; }
    .rail div { background:#2a2a2e; } .rail div.d { background:#3a3326; color:#d4a24c; } .rail div.on { background:#b23a2a; }
    .card { background:#242427 !important; border:3px solid #b8893a !important; }
    .bigq em { color:#e3963e !important; }
    .tbox { position:absolute; border:3px solid #b8893a; background:#26262a; padding:26px 34px; }
    .redbar { position:absolute; height:14px; background:#b23a2a; }
'''
CSS = KCSS + '''
    .rail { position:absolute; left:120px; top:990px; width:1680px; display:flex; gap:8px; }
    .rail div { flex:1; height:56px; background:#2a2d32; color:#8d877b; font-family:"Oswald"; font-weight:700; font-size:28px; letter-spacing:.04em; text-transform:uppercase; display:flex; align-items:center; justify-content:center; white-space:nowrap; }
    .rail div.d { background:#3b4a3c; color:#b9d8b9; }
    .rail div.on { background:#d8352c; color:#fff; flex:2.6; }
    .stp { position:absolute; display:flex; align-items:center; height:100px; background:#2a2d32; box-shadow:0 8px 0 rgba(0,0,0,.3); }
    .stp > b { width:100px; height:100px; line-height:100px; text-align:center; font-family:"Archivo Black"; font-size:46px; background:#d9a63a; color:#1b1d20; flex:none; }
    .stp > div { padding:0 24px; }
    .stp > div > span { display:block; font-family:"Archivo Black"; font-size:32px; color:#efe9dc; text-transform:uppercase; }
    .stp > div > i { display:block; font-style:normal; font-family:"Oswald"; font-weight:600; font-size:28px; color:#b9b29e; white-space:nowrap; }
    .rd { position:absolute; width:820px; background:#f4f1ea; color:#1b1d20; padding:26px 30px; box-shadow:0 14px 0 rgba(0,0,0,.35); border-left:10px solid #ff4500; }
    .rd small { display:block; font-family:"Oswald"; font-weight:700; font-size:26px; color:#7a756c; letter-spacing:.04em; }
    .rd p { margin:10px 0 0; font-family:"Oswald"; font-weight:600; font-size:40px; line-height:1.2; }
    .rd i { font-style:normal; font-family:"JetBrains Mono"; font-size:28px; color:#7a756c; display:block; margin-top:12px; }
    .bigq { position:absolute; font-family:"Archivo Black"; text-transform:uppercase; color:#efe9dc; }
    .bigq em { font-style:normal; color:#d9a63a; }
'''

CSS += THEME
DRIFT = lambda sid: ''
OUT = lambda sid: f'tl.to("#{sid}-cam > *:not(svg.full)", {{ opacity:0, y:-40, duration:0.3, stagger:0.01, ease:"power2.in" }}, @@DUR@@ - 0.4);'


def rail(sid, k):
    return f'<div class="rail h" id="{sid}-rail">' + ''.join(f'<div class="{"on" if i == k else "d" if i < k else ""}">{f"{i + 1} · {t}" if i == k else i + 1}</div>' for i, t in enumerate(STEPS)) + '</div>'


RJ = lambda sid: f'show("#{sid}-rail", 0.3, 0.4, {{ y:60 }});'


def stp(id_, x, y, w, n, a, b, col='#d9a63a'):
    return f'<div class="stp h" id="{id_}" style="left:{x}px;top:{y}px;width:{w}px"><b style="background:{col}">{n}</b><div><span>{a}</span><i>{b}</i></div></div>'


def rd(id_, x, y, sub, text, foot):
    return f'<div class="rd h" id="{id_}" style="left:{x}px;top:{y}px"><small>{sub}</small><p>{text}</p><i>{foot}</i></div>'


def chips(id_, x, y, w, items, bg='#2a2d32', fg='#efe9dc', fs=36):
    return (f'<div class="h" id="{id_}" style="position:absolute;left:{x}px;top:{y}px;display:flex;flex-wrap:wrap;gap:14px;width:{w}px">'
            + ''.join(f'<div class="chip" style="position:relative;left:auto;top:auto;font-size:{fs}px;background:{bg};color:{fg}">{t}</div>' for t in items) + '</div>')


def stag(id_, cue, gap=0.45):
    return f'tl.set("#{id_}", {{ opacity:1 }}, {cue} - 0.2); tl.fromTo("#{id_} .chip", {{ opacity:0, y:30 }}, {{ opacity:1, y:0, duration:0.3, stagger:{gap} }}, {cue} - 0.2);'




# ---------------------------------------------------------------- extra components
CSS += '''
    .nb { position:absolute; background:#242427; border:3px solid #b8893a; padding:16px 20px; }
    .nb b { display:block; font-family:"Alfa Slab One",serif; font-weight:400; font-size:30px; color:#e3963e; text-transform:uppercase; line-height:1.1; }
    .nb i { display:block; font-style:normal; font-family:"Barlow",sans-serif; font-weight:500; font-size:30px; color:#d8d2c6; margin-top:6px; line-height:1.2; }
    .nb.g { border-color:#2e9e45; } .nb.g b { color:#5fd07a; }
    .nb.r { border-color:#d8352c; } .nb.r b { color:#ff6a5c; }
    .nb.b { border-color:#4aa3df; } .nb.b b { color:#7cc4f0; }
    .ln { fill:none; stroke:#b8893a; stroke-width:5; stroke-dasharray:1; stroke-dashoffset:1; stroke-linecap:round; }
    .ln.g { stroke:#2e9e45; } .ln.r { stroke:#d8352c; } .ln.d { stroke:#e9e4da; stroke-width:4; }
    .pkt { position:absolute; left:0; top:0; width:34px; height:34px; margin:-17px 0 0 -17px; border-radius:50%; background:#e3963e; box-shadow:0 0 0 8px rgba(227,150,62,.25), 0 0 24px #e3963e; opacity:0; }
    .doc2 { position:absolute; background:#f4f1ea; color:#1b1d20; box-shadow:0 10px 0 rgba(0,0,0,.35); padding:18px 20px; font-family:"Barlow Semi Condensed",sans-serif; font-weight:700; font-size:30px; line-height:1.15; text-transform:uppercase; clip-path:polygon(0 0, calc(100% - 34px) 0, 100% 34px, 100% 100%, 0 100%); }
    .doc2::after { content:""; position:absolute; right:0; top:0; width:34px; height:34px; background:#c9c2b2; }
    .doc2 em { display:block; font-style:normal; font-family:"Barlow",sans-serif; font-weight:500; font-size:28px; text-transform:none; color:#555; margin-top:6px; }
    .stamp { position:absolute; font-family:"Alfa Slab One",serif; font-size:46px; color:#d8352c; border:6px solid #d8352c; padding:6px 20px; transform:rotate(-10deg); background:rgba(244,241,234,.0); letter-spacing:.06em; }
    .mono { font-family:"JetBrains Mono",monospace; font-weight:700; }
    .big { position:absolute; font-family:"Alfa Slab One",serif; color:#e3963e; line-height:1; }
    .sub { position:absolute; font-family:"Barlow",sans-serif; font-weight:500; color:#ddd8cc; line-height:1.3; }
    .browser { position:absolute; background:#242427; border:3px solid #b8893a; border-radius:14px; overflow:hidden; }
    .browser .bar { height:64px; background:#2f2f34; display:flex; align-items:center; gap:12px; padding:0 20px; }
    .browser .bar s { width:18px; height:18px; border-radius:50%; background:#d8352c; display:block; }
    .browser .url { flex:1; height:40px; background:#1c1c1f; border-radius:20px; padding:0 18px; display:flex; align-items:center; font-size:24px; color:#d8d2c6; white-space:nowrap; overflow:hidden; }
    .cal { position:absolute; width:260px; background:#f4f1ea; text-align:center; box-shadow:0 10px 0 rgba(0,0,0,.35); }
    .cal i { display:block; font-style:normal; background:#d8352c; color:#fff; font-family:"Barlow Semi Condensed",sans-serif; font-weight:700; font-size:30px; padding:6px 0; letter-spacing:.1em; }
    .cal b { display:block; font-family:"Alfa Slab One",serif; font-size:110px; color:#1b1d20; line-height:1.15; }
    .cal s { display:block; text-decoration:none; font-family:"Barlow Semi Condensed",sans-serif; font-weight:700; font-size:28px; color:#555; padding-bottom:10px; }
'''

JSX = '''
    const pkt = (s, pts, t, d) => { tl.set(s, { opacity:1, x:pts[0][0], y:pts[0][1] }, t);
      const n = pts.length - 1; tl.to(s, { keyframes:pts.slice(1).map(p => ({ x:p[0], y:p[1], duration:d / n, ease:"sine.inOut" })) }, t);
      tl.to(s, { opacity:0, scale:2, duration:0.3 }, t + d); tl.set(s, { scale:1 }, t + d + 0.31); };
    const cnt = (s, t, a, b, d, suf) => { const o = { v:a }; tl.to(o, { v:b, duration:d, ease:"power1.out", onUpdate:() => { const e = document.querySelector(s); if (e) e.textContent = Math.round(o.v) + (suf || ""); } }, t); };
    const type = (s, t, d) => { tl.set(s, { opacity:1 }, t); tl.fromTo(s, { clipPath:"inset(0 100% 0 0)" }, { clipPath:"inset(0 0% 0 0)", duration:d, ease:"steps(36)" }, t); };
    const fly = (s, t, x, y, sc, d) => tl.to(s, { x:x, y:y, scale:sc, rotation:0, duration:d || 0.6, ease:"power3.inOut" }, t);
'''


def nb(id_, x, y, w, a, b='', k='', h=None):
    hh = f';height:{h}px' if h else ''
    return f'<div class="nb {k} h" id="{id_}" style="left:{x}px;top:{y}px;width:{w}px{hh}"><b>{a}</b>' + (f'<i>{b}</i>' if b else '') + '</div>'


def lines(sid, paths):
    return f'<svg class="full" id="{sid}-ln" viewBox="0 0 1920 1080" style="position:absolute;inset:0;width:1920px;height:1080px" data-layout-ignore>' + ''.join(
        f'<path id="{i}" class="ln {k}" pathLength="1" d="{d}"/>' for i, d, k in paths) + '</svg>'


def doc2(id_, x, y, w, a, b='', rot=0):
    return f'<div class="doc2 h" id="{id_}" style="left:{x}px;top:{y}px;width:{w}px;transform:rotate({rot}deg)">{a}' + (f'<em>{b}</em>' if b else '') + '</div>'


def pk(id_):
    return f'<div class="pkt" id="{id_}" data-layout-ignore></div>'


def people(id_, x, y, n=4, cols=('#e3963e', '#d8d2c6', '#7cc4f0', '#5fd07a'), sc=1.4):
    inner = ''.join(person(60 + i * 80, 110, sc * (1 if i < 2 else 0.75), cols[i % 4], gid=f'{id_}-p{i}') for i in range(n))
    return svg(id_, x, y, 60 + n * 80, 170, inner)


def passport(id_, x, y, col, label, sub):
    g = (f'<rect x="4" y="4" width="232" height="312" rx="16" fill="{col}" stroke="#14140f" stroke-width="6"/>'
         f'<circle cx="120" cy="140" r="46" fill="none" stroke="#e3c27a" stroke-width="6"/><path d="M90 140h60M120 110v60" stroke="#e3c27a" stroke-width="5"/>'
         f'<text x="120" y="60" text-anchor="middle" font-family="Barlow Semi Condensed" font-weight="700" font-size="30" fill="#e3c27a">PASSPORT</text>'
         f'<text x="120" y="240" text-anchor="middle" font-family="Barlow Semi Condensed" font-weight="700" font-size="28" fill="#e3c27a">{label}</text>'
         f'<text x="120" y="276" text-anchor="middle" font-family="Barlow" font-weight="500" font-size="22" fill="#e3c27a">{sub}</text>')
    return svg(id_, x, y, 240, 320, g)




CSS += '''
    .ph { position:absolute; overflow:hidden; border:4px solid #b8893a; background:#111; box-shadow:0 14px 0 rgba(0,0,0,.35); }
    .ph img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; }
    .ph i { position:absolute; left:0; bottom:0; right:0; font-style:normal; background:rgba(20,20,22,.82); color:#e3963e; font-family:"Barlow Semi Condensed",sans-serif; font-weight:700; font-size:28px; letter-spacing:.08em; text-transform:uppercase; padding:8px 14px; }
    .qt { position:absolute; font-family:"Alfa Slab One",serif; color:#efe9dc; line-height:1.15; }
    .qt em { font-style:normal; color:#e3963e; }
    .blk { position:absolute; height:92px; display:flex; align-items:center; background:#242427; border:3px solid #b8893a; }
    .blk b { width:92px; height:86px; line-height:86px; text-align:center; background:#e3963e; color:#1b1d20; font-family:"Alfa Slab One"; font-size:44px; font-weight:400; flex:none; }
    .blk span { padding:0 22px; font-family:"Alfa Slab One"; font-size:34px; color:#efe9dc; text-transform:uppercase; white-space:nowrap; }
    .wn { position:absolute; background:#b23a2a; color:#fff; font-family:"Barlow Semi Condensed"; font-weight:700; font-size:28px; letter-spacing:.08em; padding:8px 16px; }
    .grid7 { position:absolute; display:grid; gap:6px; }
    .grid7 div { background:#2a2a2e; height:46px; }
    .bub { position:absolute; background:#2f7df6; color:#fff; font-family:"Barlow"; font-weight:600; font-size:36px; padding:18px 26px; border-radius:28px 28px 28px 6px; }
'''


def photo(id_, x, y, w, h, img, cap=''):
    return f'<div class="ph h" id="{id_}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><img src="assets/img/ph_{img}.jpg" alt="{cap}">' + (f'<i>{cap}</i>' if cap else '') + '</div>'


def kb(id_, t, d=6, z=1.18):
    return f'tl.fromTo("#{id_} img", {{ scale:{z} }}, {{ scale:1, duration:{d}, ease:"none" }}, {t});'


def blk(id_, x, y, w, n, t):
    return f'<div class="blk h" id="{id_}" style="left:{x}px;top:{y}px;width:{w}px"><b>{n}</b><span>{t}</span></div>'


