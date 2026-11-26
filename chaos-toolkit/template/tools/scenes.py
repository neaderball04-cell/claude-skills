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


CSS += '''
    .ring { position:absolute; border-radius:50%; border:6px solid; }
    .ltr { position:absolute; width:120px; height:120px; line-height:120px; text-align:center; background:#e3963e; color:#1b1d20; font-family:"Alfa Slab One"; font-size:84px; }
    .lrow { position:absolute; left:340px; width:1390px; font-family:"Barlow Semi Condensed"; font-weight:700; font-size:40px; color:#efe9dc; line-height:1.15; }
    .lrow b { display:block; font-family:"Alfa Slab One"; font-weight:400; color:#e3963e; font-size:44px; }
    .drl { position:absolute; display:flex; align-items:center; gap:18px; height:84px; padding:0 22px; background:#242427; border:3px solid #b8893a; font-family:"Alfa Slab One"; font-size:38px; color:#efe9dc; text-transform:uppercase; }
    .drl b { color:#e3963e; font-weight:400; }
    .drone { position:absolute; }
'''


def drone(id_, x, y, s=1, col='#efe9dc'):
    return (f'<svg class="drone h" id="{id_}" style="left:{x}px;top:{y}px;width:{int(160*s)}px;height:{int(90*s)}px" viewBox="0 0 160 90">'
            f'<g fill="none" stroke="{col}" stroke-width="6"><path d="M30 45 H130 M80 45 V30"/><ellipse class="pr" cx="30" cy="22" rx="26" ry="5"/><ellipse class="pr" cx="130" cy="22" rx="26" ry="5"/>'
            f'<path d="M30 45 V22 M130 45 V22"/></g><rect x="62" y="38" width="36" height="22" rx="6" fill="{col}"/><circle cx="80" cy="66" r="8" fill="#ff4a3d"/></svg>')


def drl(id_, x, y, w, n, t):
    return f'<div class="drl h" id="{id_}" style="left:{x}px;top:{y}px;width:{w}px"><b>{n}</b>{t}</div>'


def hover(id_, t, dur=8):
    return f'tl.to("#{id_}", {{ y:"-=18", duration:0.8, ease:"sine.inOut", yoyo:true, repeat:{int(dur/0.8)} }}, {t});'


def card3(id_, x, y, w, h, top, title, ex, col):
    return (f'<div class="h" id="{id_}" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:#242427;border:3px solid #b8893a;border-top:10px solid {col};padding:18px 22px">'
            f'<div style="font-family:Barlow Semi Condensed;font-weight:700;font-size:28px;letter-spacing:.08em;color:{col};text-transform:uppercase">{top}</div>'
            f'<div style="font-family:Alfa Slab One;font-size:44px;color:#efe9dc;margin:6px 0 10px;text-transform:uppercase">{title}</div>'
            f'<div style="font-family:Barlow;font-weight:600;font-size:32px;color:#d8d2c6;line-height:1.25">{ex}</div></div>')


def stepchip(id_, n, t):
    return f'<div class="h" id="{id_}" style="position:absolute;left:1500px;top:70px;font-family:Barlow Semi Condensed;font-weight:700;font-size:34px;color:#1b1d20;background:#e3963e;padding:6px 16px;border-radius:4px">STEP {n} / 6 · {t}</div>'


def build(G):
    S = {}
    J = JSX

    S['s01'] = wrap('s01', CSS + '''
    #s01-a { left:150px; top:120px; font-size:34px; }
    #s01-t { left:150px; top:180px; font-size:190px; text-align:left; width:1100px; }
    #s01-box { left:150px; top:560px; width:880px; height:200px; text-align:left; }
    #s01-ph { position:absolute; left:1180px; top:150px; width:600px; height:540px; }
    #s01-logo { position:absolute; left:1480px; top:640px; width:330px; height:322px; }''',
        '@@STEEL:s01@@' +
        '<div class="lab h" id="s01-a" style="position:absolute">Commander\'s class · CHAOS Troop</div>' +
        '<div class="big h" id="s01-t">' + ''.join(f'<span class="ch" style="display:inline-block">{c}</span>' for c in 'T2C2') + '</div>' +
        '<div class="sub h" id="s01-f" style="left:156px;top:400px;font-family:Alfa Slab One;font-size:80px;color:#efe9dc">LITE</div>' +
        '<div class="tbox h" id="s01-box"><div style="font-family:Alfa Slab One,serif;font-size:56px;line-height:1.08;color:#e3963e;text-align:left">The command post<br>that inflates</div></div>' +
        '<div class="sub h" id="s01-s" style="left:150px;top:800px;font-size:36px">AN/TSC-232 · CS23 QRG · TM 11-5895-2063-13&amp;P</div>' +
        photo('s01-ph', 1180, 150, 600, 540, 'lite_ant', '') +
        '<img id="s01-logo" class="h" src="assets/img/chaos_logo.png" alt="CHAOS">' +
        '<div class="redbar h" id="s01-bar" style="left:60px;top:1010px;width:1040px"></div>',
        J + '''
    show("#s01-a", 0.2, 0.5, { x:-60 });
    tl.set("#s01-t", { opacity:1 }, 0.35);
    tl.from("#s01-t .ch", { opacity:0, y:120, rotationX:-90, duration:0.55, stagger:0.1, ease:"back.out(2)" }, 0.35);
    show("#s01-f", 0.9, 0.5, { x:-80 });
    tl.set("#s01-box", { opacity:1 }, 1.3);
    tl.fromTo("#s01-box", { clipPath:"inset(0 100% 0 0)" }, { clipPath:"inset(0 0% 0 0)", duration:0.6, ease:"power3.inOut" }, 1.3);
    show("#s01-s", 1.8, 0.5, { y:30 });
    tl.set("#s01-ph", { opacity:1 }, 0.8);
    tl.fromTo("#s01-ph", { scale:0.2, opacity:0 }, { scale:1, opacity:1, duration:1.4, ease:"elastic.out(1,0.5)" }, 0.8);''' + kb('s01-ph', 2.2, 14, 1.12) + '''
    tl.fromTo("#s01-logo", { opacity:0, scale:0.3, rotation:-200 }, { opacity:1, scale:1, rotation:0, duration:1.0, ease:"back.out(1.4)" }, 1.6);
    tl.set("#s01-bar", { opacity:1 }, 1.9); tl.fromTo("#s01-bar", { scaleX:0, transformOrigin:"0 50%" }, { scaleX:1, duration:0.8, ease:"power3.out" }, 1.9);
    tl.to(["#s01-a","#s01-t","#s01-f","#s01-box","#s01-s","#s01-bar","#s01-ph"], { opacity:0, x:-80, duration:0.4, stagger:0.04, ease:"power2.in" }, @@DUR@@ - 0.5);
    tl.to("#s01-logo", { opacity:0, scale:1.4, duration:0.4 }, @@DUR@@ - 0.45);''')

    # s02 what is it + inflatable
    S['s02'] = wrap('s02', CSS, '@@STEEL:s02@@' + H1('s02', 'What is T2C2?', 60) +
        '<div class="h" id="s02-g1" style="position:absolute;inset:0">' +
        nb('s02-n', 192, 190, 1540, 'Transportable Tactical Command Communications', 'Beyond-line-of-sight SATCOM · voice · video · data · at the halt', '', 150) +
        chips('s02-c', 192, 400, 1540, ['Early entry', 'Command posts', 'Tactical edge', 'No ground infrastructure'], '#e3963e', '#1b1d20', 42) +
        svg('s02-sat', 192, 520, 1540, 420,
            '<g id="s02-s"><rect x="720" y="20" width="100" height="50" fill="#7cc4f0"/><rect x="600" y="35" width="110" height="20" fill="#3a6f8f"/><rect x="830" y="35" width="110" height="20" fill="#3a6f8f"/></g>'
            '<path id="s02-up" class="ln g" pathLength="1" d="M280 320 L760 80" style="stroke-width:6"/><path id="s02-dn" class="ln b" pathLength="1" d="M780 80 L1260 320" style="stroke-width:6"/>'
            '<circle cx="260" cy="330" r="40" fill="#cdbf9a"/><text x="260" y="405" text-anchor="middle" font-family="Barlow Semi Condensed" font-weight="700" font-size="30" fill="#e3963e">T2C2 LITE</text>'
            '<rect x="1220" y="310" width="90" height="60" fill="#7cc4f0"/><text x="1265" y="405" text-anchor="middle" font-family="Barlow Semi Condensed" font-weight="700" font-size="30" fill="#7cc4f0">THE NETWORK</text>', cls='') + '</div>' +
        '<div class="h" id="s02-g2" style="position:absolute;inset:0">' +
        nb('s02-t1', 192, 200, 700, '⛺ Camping tent', 'Packs small', 'b', 140) +
        nb('s02-t2', 192, 370, 700, '🏠 Big dish', 'Inflates big · more bandwidth', 'g', 140) +
        photo('s02-ph', 960, 190, 770, 700, 'lite_ant', '1.2 m inflatable antenna') + '</div>',
        WIPE('s02') + J + '''
    slam("#s02-h", @@n2@@, "#s02-cam", 6, 1.3);
    tl.set("#s02-g1", { opacity:1 }, @@n2@@);
    show("#s02-n", @@n2:Transportable@@ - 0.2, 0.45, { y:60 });
    tl.from("#s02-sat", { opacity:0, duration:0.4 }, @@n2:satellite@@ - 0.3);
    draw("#s02-up", @@n2:satellite@@, 0.7); draw("#s02-dn", @@n2:satellite@@ + 0.6, 0.7);
    ''' + stag('s02-c', '@@n2:early entry@@ - 0.2', 0.5) + '''
    tl.to("#s02-g1", { opacity:0, duration:0.4 }, @@n3@@ - 0.2);
    tl.set("#s02-g2", { opacity:1 }, @@n3@@);
    show("#s02-ph", @@n3:inflatable@@ - 0.3, 0.6, { scale:0.3 });''' + kb('s02-ph', '@@n3:inflatable@@', 10) + '''
    show("#s02-t1", @@n3:camping tent@@ - 0.2, 0.4, { x:-60 });
    show("#s02-t2", @@n3:big dish@@ - 0.2, 0.4, { x:-60 });''' + OUT('s02'))

    # s03 lite vs heavy
    def spec(rows, col):
        return ''.join(f'<div style="display:flex;justify-content:space-between;border-bottom:2px solid #3a3a3e;padding:8px 0;font-family:Barlow Semi Condensed;font-weight:700;font-size:32px"><span style="color:#b9b29e">{a}</span><span style="color:{col}">{b}</span></div>' for a, b in rows)
    S['s03'] = wrap('s03', CSS, '@@STEEL:s03@@' + H1('s03', 'Lite vs. Heavy', 60) +
        '<div class="h" id="s03-l" style="position:absolute;left:192px;top:190px;width:740px;height:760px;background:#242427;border:3px solid #b8893a;border-top:12px solid #e3963e;padding:20px 26px">'
        '<div style="font-family:Alfa Slab One;font-size:56px;color:#e3963e">T2C2 LITE</div><div style="font-family:Barlow;font-size:30px;color:#d8d2c6;margin-bottom:10px">AN/TSC-232 · 🎒 carry-on</div>' +
        spec([('Antenna', '1.2 m'), ('Crew', '2 Soldiers'), ('Setup', '~25 min'), ('Stage', '5 × 5 ft'), ('Cases', '94 · 41 · 86 lb')], '#efe9dc') +
        '<img src="assets/img/ph_lite_ant.jpg" style="width:300px;margin:16px auto 0;display:block;border:3px solid #b8893a"></div>' +
        '<div class="h" id="s03-hv" style="position:absolute;left:990px;top:190px;width:740px;height:760px;background:#242427;border:3px solid #b8893a;border-top:12px solid #7cc4f0;padding:20px 26px">'
        '<div style="font-family:Alfa Slab One;font-size:56px;color:#7cc4f0">T2C2 HEAVY</div><div style="font-family:Barlow;font-size:30px;color:#d8d2c6;margin-bottom:10px">🧳 checked luggage</div>' +
        spec([('Antenna', '2.4 m'), ('Bands', 'Tri-band'), ('Setup', '~35 min'), ('Stage', '12 × 12 ft'), ('Cases', '4 × 90–112 lb')], '#efe9dc') +
        '<img src="assets/img/ph_heavy_ant.jpg" style="width:300px;margin:16px auto 0;display:block;border:3px solid #b8893a"></div>',
        WIPE('s03') + J + '''
    slam("#s03-h", @@n4@@, "#s03-cam", 6, 1.3);
    show("#s03-l", @@n4:The Lite@@ - 0.2, 0.5, { x:-120 });
    show("#s03-hv", @@n4:The Heavy@@ - 0.2, 0.5, { x:120 });
    tl.to("#s03-l", { scale:1.03, duration:0.3, yoyo:true, repeat:1 }, @@n4:carry-on@@);''' + OUT('s03'))

    # s04 components
    comp = [('lite_point', 'Pointing', 'Pointing components'), ('lite_ant', '1.2 m antenna', 'one point two meter antenna'), ('lite_feed', 'Feed: BUC · LNB · OMT', 'feed assembly'), ('lite_power', 'Power: CUPS', 'Power'), ('lite_anchor', 'Anchor plates', 'Anchor plates'), ('baseband', 'Router modules', 'networking case')]
    S['s04'] = wrap('s04', CSS + '#s04-p0 img, #s04-p5 img { object-fit:contain; background:#fff; }', '@@STEEL:s04@@' + H1('s04', 'What\'s in the Lite', 60) +
        ''.join(photo(f's04-p{i}', 192 + (i % 3) * 520, 190 + (i // 3) * 390, 490, 360, im, cap) for i, (im, cap, _) in enumerate(comp)),
        WIPE('s04') + J + '''
    slam("#s04-h", @@n5@@, "#s04-cam", 6, 1.3);
    ''' + ''.join(f'show("#s04-p{i}", @@n5:{c}@@ - 0.2, 0.4, {{ scale:0.6, rotation:{(-3, 2, -2, 3, -2, 2)[i]} }});' for i, (_, _, c) in enumerate(comp)) + OUT('s04'))

    # s05 site
    req = [('👁️', 'Clear look angle', 'clear look angle'), ('📏', 'Level ground', 'level ground'), ('⚡', 'No electrical interference', 'electrical interference'), ('🔩', 'No metal nearby', 'metal objects'), ('⬛', '5 × 5 ft stage', 'five by five'), ('🔌', '≤ 25 ft to network gear', 'twenty-five feet')]
    S['s05'] = wrap('s05', CSS + '''
    .wt { position:absolute; width:750px; height:104px; display:flex; align-items:center; gap:18px; background:#242427; border:3px solid #b8893a; padding:0 20px; font-family:"Barlow Semi Condensed"; font-weight:700; font-size:38px; color:#efe9dc; }
    .wt span { font-size:52px; }''',
        '@@STEEL:s05@@' + H1('s05', 'Pick the site', 60) + stepchip('s05-st', 1, 'SITE') +
        ''.join(f'<div class="wt h" id="s05-w{i}" style="left:{192 + (i % 2) * 790}px;top:{190 + (i // 2) * 128}px"><span>{e}</span>{t}</div>' for i, (e, t, _) in enumerate(req)) +
        svg('s05-tv', 192, 600, 1540, 340,
            '<path d="M0 320 H1540" stroke="#b8893a" stroke-width="4"/><rect x="120" y="250" width="160" height="70" fill="#3a3a40"/><path d="M200 250 L250 170" stroke="#efe9dc" stroke-width="8"/><ellipse cx="260" cy="160" rx="40" ry="24" fill="#cdbf9a"/>'
            '<path id="s05-ray" class="ln g" pathLength="1" d="M280 150 L1400 30" style="stroke-width:6"/><g id="s05-tree"><path d="M820 320 V200" stroke="#6b4a2a" stroke-width="20"/><circle cx="820" cy="150" r="90" fill="#2f6b3a"/></g>'
            '<text x="1420" y="40" font-family="Barlow Semi Condensed" font-weight="700" font-size="32" fill="#7cc4f0">🛰️</text>'
            '<g id="s05-np"><rect x="980" y="160" width="300" height="70" rx="8" fill="#b23a2a"/><text x="1130" y="207" text-anchor="middle" font-family="Alfa Slab One" font-size="34" fill="#fff">NO PICTURE</text></g>', cls='h'),
        WIPE('s05') + J + '''
    slam("#s05-h", @@n6@@, "#s05-cam", 6, 1.3); pop("#s05-st", @@n6@@ + 0.3);
    ''' + ''.join(f'show("#s05-w{i}", @@n6:{c}@@ - 0.15, 0.35, {{ scale:0.6 }});' for i, (_, _, c) in enumerate(req)) + '''
    show("#s05-tv", @@n6:Real life@@ - 0.2, 0.4);
    draw("#s05-ray", @@n6:satellite TV@@, 0.6);
    tl.fromTo("#s05-tree", { scale:0, svgOrigin:"820 320" }, { scale:1, duration:0.5, ease:"back.out(2)" }, @@n6:Trees@@);
    tl.to("#s05-ray", { opacity:0.15, duration:0.3 }, @@n6:Trees@@ + 0.4);
    tl.fromTo("#s05-np", { opacity:0, scale:2, svgOrigin:"1130 195" }, { opacity:1, scale:1, duration:0.3, ease:"power4.in" }, @@n6:no picture@@);''' + OUT('s05'))

    # s06 point & anchor
    bl = [('10 mph', '30 lb', 'ten miles'), ('20 mph', '60 lb', 'ten miles'), ('30 mph', '90 lb', 'up to one hundred'), ('40 mph', '120 lb', 'up to one hundred')]
    S['s06'] = wrap('s06', CSS, '@@STEEL:s06@@' + H1('s06', 'Point and anchor', 60) + stepchip('s06-st', 2, 'POINT') +
        svg('s06-cmp', 192, 190, 560, 560,
            '<circle cx="280" cy="280" r="250" fill="#242427" stroke="#b8893a" stroke-width="6"/>' + ''.join(f'<text x="{280 + 200 * __import__("math").sin(a * 3.14159 / 180):.0f}" y="{290 - 200 * __import__("math").cos(a * 3.14159 / 180):.0f}" text-anchor="middle" font-family="Alfa Slab One" font-size="40" fill="#efe9dc">{t}</text>' for a, t in [(0, 'N'), (90, 'E'), (180, 'S'), (270, 'W')]) +
            '<g id="s06-ndl"><path d="M280 100 L300 280 L280 460 L260 280 Z" fill="#efe9dc"/><path d="M280 100 L300 280 L260 280 Z" fill="#ff4a3d"/></g><circle cx="280" cy="280" r="16" fill="#e3963e"/>'
            '<g id="s06-az"><path d="M280 280 L280 40" stroke="#5fd07a" stroke-width="8" stroke-dasharray="14 10"/><text x="280" y="30" text-anchor="middle" font-family="Barlow Semi Condensed" font-weight="700" font-size="28" fill="#5fd07a">SATELLITE</text></g>', cls='h') +
        nb('s06-saa', 192, 790, 560, 'SAA', 'Gives the magnetic azimuth', 'b') +
        '<div class="h" id="s06-tb" style="position:absolute;left:830px;top:190px;width:900px">' +
        '<div style="display:grid;grid-template-columns:1fr 1fr;background:#e3963e;color:#1b1d20;font-family:Barlow Semi Condensed;font-weight:700;font-size:34px;padding:10px 20px"><span>WIND</span><span>BALLAST / PLATE</span></div>' +
        ''.join(f'<div class="s06-r" style="display:grid;grid-template-columns:1fr 1fr;padding:14px 20px;border-bottom:2px solid #3a3a3e;font-family:Alfa Slab One;font-size:44px;color:#efe9dc"><span>{a}</span><span style="color:#e3963e">{b}</span></div>' for a, b, _ in bl) + '</div>' +
        photo('s06-ph', 830, 690, 440, 260, 'lite_anchor', 'Anchor plates') +
        '<div class="stamp h" id="s06-lim" style="left:1320px;top:740px;font-size:46px;background:rgba(244,241,234,.92);transform:rotate(-6deg)">40 MPH = LIMIT</div>',
        WIPE('s06') + J + '''
    slam("#s06-h", @@n7@@, "#s06-cam", 6, 1.3); pop("#s06-st", @@n7@@ + 0.3);
    show("#s06-saa", @@n7:satellite access@@ - 0.2, 0.4, { y:60 });
    show("#s06-cmp", @@n7:magnetic azimuth@@ - 0.4, 0.5, { scale:0.6 });
    tl.fromTo("#s06-ndl", { rotation:-120, svgOrigin:"280 280" }, { rotation:0, duration:1.6, ease:"elastic.out(1,0.4)" }, @@n7:compass@@);
    tl.from("#s06-az", { opacity:0, duration:0.4 }, @@n7:satellite arrow@@);
    tl.to("#s06-az", { opacity:0.3, duration:0.2, yoyo:true, repeat:3 }, @@n7:Recheck@@);
    show("#s06-ph", @@n7:anchor plates@@ - 0.2, 0.45, { scale:0.7 });
    tl.set("#s06-tb", { opacity:1 }, @@n7:ballast@@ - 0.2);
    tl.from(".s06-r", { opacity:0, x:80, duration:0.3, stagger:0.55 }, @@n7:thirty pounds@@ - 0.3);
    slam("#s06-lim", @@n7:Forty is the limit@@, "#s06-cam", 8, 1.6);''' + OUT('s06'))

    # s07 power & inflate
    chain = [('GFCI', 'GFCI'), ('240 W supply', 'two-forty'), ('CUPS', 'CUPS'), ('Split cable', 'split cable'), ('CIU', 'to the CIU')]
    S['s07'] = wrap('s07', CSS, '@@STEEL:s07@@' + H1('s07', 'Power and inflate', 60) + stepchip('s07-st', 3, 'INFLATE') +
        '<div class="h" id="s07-ch" style="position:absolute;left:192px;top:190px;width:1540px;display:flex;align-items:center;gap:14px">' +
        ''.join(f'<div class="s07-c" style="flex:1;height:110px;display:flex;align-items:center;justify-content:center;background:#242427;border:3px solid #e3963e;font-family:Alfa Slab One;font-size:34px;color:#efe9dc;text-align:center">{t}</div>' + ('<div class="s07-c" style="font-family:Alfa Slab One;font-size:50px;color:#e3963e">→</div>' if i < 4 else '') for i, (t, _) in enumerate(chain)) + '</div>' +
        svg('s07-ball', 192, 360, 620, 560,
            '<ellipse cx="310" cy="530" rx="260" ry="22" fill="#3a3326"/><circle id="s07-b" cx="310" cy="300" r="230" fill="#cdbf9a" stroke="#8a7d5c" stroke-width="6"/>', cls='h') +
        ''.join(f'<div class="h" id="s07-led{i}" style="position:absolute;left:880px;top:{380 + i * 120}px;display:flex;align-items:center;gap:24px;font-family:Barlow Semi Condensed;font-weight:700;font-size:40px;color:#efe9dc"><div class="s07-l" style="width:60px;height:60px;border-radius:50%;background:#555"></div>{t}</div>' for i, t in enumerate(['Pressure LED', 'Differential LED'])) +
        nb('s07-ctr', 880, 630, 850, 'Center on the black line', 'Then take slack out of the hold-down cables', '', 130) +
        '<div class="warn h" id="s07-w" style="position:absolute;left:880px;top:790px;width:850px;background:#b23a2a;color:#fff;font-family:Barlow Semi Condensed;font-weight:700;font-size:38px;padding:18px 22px">🎈 Bouncy castle rule: never leave it unattended while inflating</div>',
        WIPE('s07') + J + '''
    slam("#s07-h", @@n8@@, "#s07-cam", 6, 1.3); pop("#s07-st", @@n8@@ + 0.3);
    tl.set("#s07-ch", { opacity:1 }, @@n8:GFCI@@ - 0.2);
    tl.fromTo(".s07-c", { opacity:0, x:-40 }, { opacity:1, x:0, duration:0.25, stagger:0.28 }, @@n8:GFCI@@ - 0.2);
    show("#s07-ball", @@n8:starts inflating@@ - 0.6, 0.3);
    tl.fromTo("#s07-b", { attr:{ r:20, cy:510 } }, { attr:{ r:230, cy:300 }, duration:3.0, ease:"power1.out" }, @@n8:starts inflating@@ - 0.4);
    show("#s07-led0", @@n8:pressure@@ - 0.2, 0.3, { x:40 }); show("#s07-led1", @@n8:differential@@ - 0.2, 0.3, { x:40 });
    tl.to("#s07-led0 .s07-l", { background:"#5fd07a", boxShadow:"0 0 30px #5fd07a", duration:0.3 }, @@n8:go green@@ - 0.2);
    tl.to("#s07-led1 .s07-l", { background:"#5fd07a", boxShadow:"0 0 30px #5fd07a", duration:0.3 }, @@n8:go green@@ + 0.1);
    show("#s07-ctr", @@n8:black line@@ - 0.3, 0.4, { y:60 });
    slam("#s07-w", @@n8:bouncy castle@@, "#s07-cam", 8, 1.5);''' + OUT('s07'))

    # s08 feed
    S['s08'] = wrap('s08', CSS, '@@STEEL:s08@@' + H1('s08', 'Attach the feed', 60) + stepchip('s08-st', 4, 'FEED') +
        photo('s08-ph', 192, 190, 760, 600, 'lite_feed', 'Feed assembly') +
        drl('s08-a', 1010, 200, 720, '1', 'Match the color stripes') +
        '<div class="h" id="s08-b" style="position:absolute;left:1010px;top:320px;width:720px;display:flex;gap:16px"><div style="flex:1;background:#242427;border:3px solid #ff6a5c;padding:16px;text-align:center"><div style="font-family:Alfa Slab One;font-size:46px;color:#ff6a5c">TX</div><div style="font-family:Barlow Semi Condensed;font-weight:700;font-size:34px;color:#efe9dc">→ BUC</div></div><div style="flex:1;background:#242427;border:3px solid #7cc4f0;padding:16px;text-align:center"><div style="font-family:Alfa Slab One;font-size:46px;color:#7cc4f0">RX</div><div style="font-family:Barlow Semi Condensed;font-weight:700;font-size:34px;color:#efe9dc">→ LNB</div></div></div>' +
        '<div class="h" id="s08-c" style="position:absolute;left:1010px;top:520px;width:720px;display:flex;flex-direction:column;gap:14px">' +
        '<div style="background:#efe9dc;color:#1b1d20;padding:18px 22px;font-family:Alfa Slab One;font-size:36px">WHITE legs → UPPER</div><div style="background:#b23a2a;color:#fff;padding:18px 22px;font-family:Alfa Slab One;font-size:36px">RED legs → LOWER</div></div>',
        WIPE('s08') + J + '''
    slam("#s08-h", @@n9@@, "#s08-cam", 6, 1.3); pop("#s08-st", @@n9@@ + 0.3);
    show("#s08-ph", @@n9@@ + 0.2, 0.5, { scale:0.85 });''' + kb('s08-ph', '@@n9@@', 12) + '''
    show("#s08-a", @@n9:color stripes@@ - 0.3, 0.4, { x:80 });
    show("#s08-b", @@n9:Transmit@@ - 0.2, 0.4, { x:80 });
    show("#s08-c", @@n9:White-labeled@@ - 0.2, 0.4, { x:80 });''' + OUT('s08'))

    # s09 DCIU & modem
    S['s09'] = wrap('s09', CSS, '@@STEEL:s09@@' + H1('s09', 'DCIU and modem', 60) + stepchip('s09-st', 5, 'CONNECT') +
        svg('s09-k', 192, 190, 900, 380,
            ''.join(f'<g id="s09-k{i}"><circle cx="{220 + i * 460}" cy="170" r="110" fill="#242427" stroke="#b8893a" stroke-width="6"/><path class="s09-ptr" d="M{220 + i * 460} 170 L{220 + i * 460} 80" stroke="#ff6a5c" stroke-width="14" stroke-linecap="round"/><text x="{220 + i * 460}" y="340" text-anchor="middle" font-family="Alfa Slab One" font-size="36" fill="#efe9dc">{t}</text></g>' for i, t in enumerate(['DC INJECTION', '10 MHz'])), cls='h') +
        '<div class="stamp h" id="s09-off" style="left:430px;top:300px;font-size:60px;background:rgba(244,241,234,.92);transform:rotate(-6deg)">OFF FIRST</div>' +
        ''.join(li(f's09-l{i}', 1140, 200 + i * 86, '✓', t, 'y', 36) for i, t in enumerate(['Cable BUC · LNB · modem', 'Apply 24 VDC', 'Status light green', '10 MHz → BUC & LNB', 'DC injection → LNB'])) +
        '<div class="h" id="s09-led" style="position:absolute;left:1140px;top:660px;width:90px;height:90px;border-radius:50%;background:#555"></div>' +
        nb('s09-g', 192, 640, 900, '⏚ Star ground kit', 'Ground it. Every time.', 'r', 150),
        WIPE('s09') + J + '''
    slam("#s09-h", @@n10@@, "#s09-cam", 6, 1.3); pop("#s09-st", @@n10@@ + 0.3);
    show("#s09-k", @@n10:DC injection@@ - 0.3, 0.4);
    slam("#s09-off", @@n10:to off@@, "#s09-cam", 8, 1.6);
    ''' + ''.join(f'show("#s09-l{i}", @@n10:{c}@@ - 0.15, 0.3, {{ x:60 }});' for i, c in enumerate(['Cable the BUC', 'twenty-four volts', 'green status', 'Then set ten', 'DC injection to LNB'])) + '''
    tl.to("#s09-off", { opacity:0, duration:0.3 }, @@n10:Cable the BUC@@);
    show("#s09-led", @@n10:green status@@ - 0.3, 0.2);
    tl.to("#s09-led", { background:"#5fd07a", boxShadow:"0 0 40px #5fd07a", duration:0.3 }, @@n10:green status@@);
    tl.to(".s09-ptr", { rotation:90, svgOrigin:(i) => i ? "680 170" : "220 170", duration:0.6, ease:"back.out(2)", stagger:0.6 }, @@n10:Then set ten@@);
    show("#s09-g", @@n10:star ground@@ - 0.2, 0.4, { y:60 });''' + OUT('s09'))

    # s10 network
    S['s10'] = wrap('s10', CSS, '@@STEEL:s10@@' + H1('s10', 'Bring up the network', 60) + stepchip('s10-st', 6, 'NETWORK') +
        photo('s10-ph', 192, 190, 820, 580, 'baseband', 'Router modules + PRC-148 batteries') +
        nb('s10-a', 1060, 190, 670, 'Twist at 40°', 'Until the modules are flush', '', 140) +
        nb('s10-b', 1060, 360, 670, '2 × PRC-148 batteries', 'Right side powers both modules', 'b', 140) +
        nb('s10-c', 1060, 530, 670, 'KG-250XS on top', 'Lock it, then power it', 'r', 140) +
        nb('s10-d', 1060, 700, 670, 'Join the network', 'Settings from your SAA', 'g', 140),
        WIPE('s10') + J + '''
    slam("#s10-h", @@n11@@, "#s10-cam", 6, 1.3); pop("#s10-st", @@n11@@ + 0.3);
    show("#s10-ph", @@n11@@ + 0.3, 0.5, { scale:0.85 });''' + kb('s10-ph', '@@n11@@', 12) + '''
    show("#s10-a", @@n11:forty degree@@ - 0.3, 0.4, { x:80, rotation:-8 });
    show("#s10-b", @@n11:batteries@@ - 0.3, 0.4, { x:80 });
    show("#s10-c", @@n11:KG@@ - 0.2, 0.4, { x:80 });
    show("#s10-d", @@n11:join the network@@ - 0.2, 0.4, { x:80 });''' + OUT('s10'))

    # s11 signal flow
    nodes = [('MODEM', 230, '#efe9dc'), ('DCIU', 620, '#e3963e'), ('BUC', 1010, '#ff6a5c'), ('LNB', 1010, '#7cc4f0')]
    S['s11'] = wrap('s11', CSS, '@@STEEL:s11@@' + H1('s11', 'The signal path', 60) +
        svg('s11-sf', 160, 160, 1600, 640,
            '<rect x="1380" y="40" width="140" height="70" fill="#7cc4f0"/><rect x="1290" y="60" width="80" height="30" fill="#3a6f8f"/><rect x="1530" y="60" width="60" height="30" fill="#3a6f8f"/><text x="1450" y="150" text-anchor="middle" font-family="Barlow Semi Condensed" font-weight="700" font-size="32" fill="#7cc4f0">SATELLITE</text>'
            '<g font-family="Alfa Slab One" font-size="40">'
            '<rect x="60" y="390" width="260" height="110" fill="#242427" stroke="#efe9dc" stroke-width="4"/><text x="190" y="460" text-anchor="middle" fill="#efe9dc">MODEM</text>'
            '<rect x="460" y="390" width="260" height="110" fill="#242427" stroke="#e3963e" stroke-width="4"/><text x="590" y="460" text-anchor="middle" fill="#e3963e">DCIU</text>'
            '<rect x="860" y="260" width="240" height="100" fill="#242427" stroke="#ff6a5c" stroke-width="4"/><text x="980" y="325" text-anchor="middle" fill="#ff6a5c">BUC</text>'
            '<rect x="860" y="530" width="240" height="100" fill="#242427" stroke="#7cc4f0" stroke-width="4"/><text x="980" y="595" text-anchor="middle" fill="#7cc4f0">LNB</text></g>'
            '<path id="s11-t1" class="ln r" pathLength="1" d="M320 430 H460" style="stroke-width:8"/><path id="s11-t2" class="ln r" pathLength="1" d="M720 420 L860 310" style="stroke-width:8"/><path id="s11-t3" class="ln r" pathLength="1" d="M1100 300 L1390 110" style="stroke-width:8"/>'
            '<path id="s11-r1" class="ln b" pathLength="1" d="M1450 120 L1100 580" style="stroke-width:8"/><path id="s11-r2" class="ln b" pathLength="1" d="M860 580 L720 480" style="stroke-width:8"/><path id="s11-r3" class="ln b" pathLength="1" d="M460 470 H320" style="stroke-width:8"/>'
            '<text x="1230" y="200" font-family="Barlow Semi Condensed" font-weight="700" font-size="30" fill="#ff6a5c">UP · TX</text><text x="1290" y="420" font-family="Barlow Semi Condensed" font-weight="700" font-size="30" fill="#7cc4f0">DOWN · RX</text>', cls='h') +
        nb('s11-sa', 192, 830, 1540, '📈 Spectrum analyzer on the beacon', 'Peak on the beacon = pointed right', 'g'),
        WIPE('s11') + J + '''
    slam("#s11-h", @@n12@@, "#s11-cam", 6, 1.3);
    show("#s11-sf", @@n12@@ + 0.3, 0.4);
    draw("#s11-t1", @@n12:leaves the modem@@, 0.5); draw("#s11-t2", @@n12:DCIU to the BUC@@, 0.5); draw("#s11-t3", @@n12:shoots it up@@, 0.6);
    draw("#s11-r1", @@n12:Coming down@@, 0.6); draw("#s11-r2", @@n12:LNB catches@@ + 0.4, 0.5); draw("#s11-r3", @@n12:back through@@ + 0.4, 0.5);
    show("#s11-sa", @@n12:spectrum analyzer@@ - 0.2, 0.4, { y:60 });''' + OUT('s11'))

    # s12 mistakes
    mk = [('Sloppy compass read', 'wrong azimuth'), ('Too little ballast', 'ballast'), ('Cable locks locked too early', 'Locking'), ('DCIU knobs still on', 'knobs still on'), ('Truck parked next to the dish', 'truck'), ('No ground', 'no ground')]
    S['s12'] = wrap('s12', CSS + '#s12-stage .drl { font-size:31px; }', '@@STEEL:s12@@' + H1('s12', 'The usual mistakes', 60) +
        ''.join(drl(f's12-m{i}', 192 + (i % 2) * 790, 200 + (i // 2) * 140, 750, '✕', t) for i, (t, _) in enumerate(mk)) +
        '<div class="qt h" id="s12-q" style="left:192px;top:700px;width:1540px;font-size:64px">Every one of them <em>costs you the link.</em></div>',
        WIPE('s12') + J + '''
    slam("#s12-h", @@n13@@, "#s12-cam", 6, 1.3);
    ''' + ''.join(f'show("#s12-m{i}", @@n13:{c}@@ - 0.15, 0.3, {{ x:{-80 if i % 2 == 0 else 80} }});' for i, (_, c) in enumerate(mk)) + '''
    show("#s12-q", @@n13:costs you@@ - 0.2, 0.5, { y:60 });
    shake("#s12-cam", @@n13:costs you@@ + 0.2, 10);''' + OUT('s12'))

    # s13 CHAOS
    pace = [('P', 'Terrestrial network', '#5fd07a'), ('A', 'T2C2 Lite SATCOM', '#e3963e'), ('C', 'Combat net radio', '#7cc4f0'), ('E', 'Runner / LNO', '#ff6a5c')]
    S['s13'] = wrap('s13', CSS + '''
    .pace { position:absolute; left:192px; width:760px; height:100px; display:flex; align-items:center; gap:18px; padding:0 18px; font-family:"Barlow Semi Condensed"; font-weight:700; font-size:36px; color:#efe9dc; background:#242427; border:3px solid #b8893a; }
    .pace b { font-family:"Alfa Slab One"; font-weight:400; font-size:50px; width:50px; }''',
        '@@STEEL:s13@@' + H1('s13', 'How it hits CHAOS', 60) +
        '<div class="lab h" id="s13-pl" style="position:absolute;left:192px;top:180px;font-size:30px">EXAMPLE PACE · BLOS PATH</div>' +
        ''.join(f'<div class="pace h" id="s13-p{i}" style="top:{230 + i * 115}px"><b style="color:{c}">{l}</b>{t}</div>' for i, (l, t, c) in enumerate(pace)) +
        nb('s13-a', 1010, 200, 720, '2 Soldiers · 25 min', 'On the air, day or night', 'g', 150) +
        nb('s13-b', 1010, 380, 720, 'QRG + TM stay with the system', 'TM 11-5895-2063-13&P', 'b', 150) +
        '<div class="qt h" id="s13-q" style="left:1010px;top:600px;width:720px;font-size:54px">When the ground can\'t reach, <em>go to space.</em></div>',
        WIPE('s13') + J + '''
    slam("#s13-h", @@n14@@, "#s13-cam", 6, 1.3);
    show("#s13-pl", @@n14:terrestrial@@ - 0.3, 0.3);
    show("#s13-p0", @@n14:terrestrial@@, 0.3, { x:-60 }); show("#s13-p1", @@n14:beyond line@@ - 0.3, 0.3, { x:-60 });
    show("#s13-p2", @@n14:PACE@@, 0.3, { x:-60 }); show("#s13-p3", @@n14:PACE@@ + 0.4, 0.3, { x:-60 });
    tl.to("#s13-p1", { borderColor:"#e3963e", scale:1.04, duration:0.3, yoyo:true, repeat:1 }, @@n14:PACE plan@@);
    show("#s13-a", @@n14:Train crews@@ - 0.2, 0.4, { x:80 });
    show("#s13-b", @@n14:QRG@@ - 0.3, 0.4, { x:80 });
    show("#s13-q", @@n14:QRG@@ + 1.2, 0.5, { y:60 });''' + OUT('s13'))

    S['s14'] = wrap('s14', CSS + '''
    #s14-logo { position:absolute; left:1240px; top:180px; width:520px; height:508px; }''',
        '@@STEEL:s14@@' + photo('s14-ph', 30, 30, 1860, 1020, 'lite_ant', '') +
        '<img id="s14-logo" class="h" src="assets/img/chaos_logo.png" alt="CHAOS">' +
        '<div class="h" id="s14-p" style="position:absolute;left:150px;top:260px;font-family:Alfa Slab One;font-size:96px;color:#efe9dc;line-height:1.15"><div class="s14-w">Point it.</div><div class="s14-w" style="color:#e3963e">Pump it.</div><div class="s14-w">Plug it in.</div></div>' +
        '<div class="bigq h" id="s14-c" style="left:150px;top:760px;font-size:130px;color:#ff6a5c">That\'s CHAOS!</div>',
        '''
    tl.fromTo("#s14-stage", { clipPath:"circle(0% at 50% 50%)" }, { clipPath:"circle(150% at 50% 50%)", duration:0.55, ease:"power2.inOut" }, 0);
    tl.set("#s14-ph", { opacity:0.14 }, 0);''' + kb('s14-ph', '0', 6, 1.2) + '''
    tl.set("#s14-p", { opacity:1 }, @@n15@@);
    tl.from(".s14-w", { opacity:0, x:-100, duration:0.3, stagger:0.45, ease:"back.out(2)" }, @@n15@@);
    tl.fromTo("#s14-logo", { opacity:0, scale:0.3, rotation:-200 }, { opacity:1, scale:1, rotation:0, duration:0.8, ease:"back.out(1.4)" }, @@n15@@ + 0.2);
    slam("#s14-c", @@n15:That's CHAOS@@, "#s14-cam", 16, 1.7);''')
    return S


def SFX(cue):
    W = ('whoosh.mp3', 0.57, 0.4)
    I = lambda sid, t, v=0.35: (sid, t - 0.07, 'impact-bass-1.mp3', 2.1, v)
    out = [(f's{i:02d}', 0.0) + W for i in range(2, 14)]
    out += [I('s01', 0.4), I('s05', cue('s05', 'n6', 'no picture')), I('s06', cue('s06', 'n7', 'Forty is the limit') + 0.2), I('s09', cue('s09', 'n10', 'to off') + 0.2),
            I('s12', cue('s12', 'n13', 'costs you') + 0.2), ('s14', cue('s14', 'n15', "That's CHAOS") + 0.2 - 1.986, 'impact-bass-2.mp3', 2.59, 0.4)]
    return out
