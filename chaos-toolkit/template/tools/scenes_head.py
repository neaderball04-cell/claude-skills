"""CHAOS command sponsorship class — s01-s15."""
from base import wrap
from jb import it
from ea import svg, card, person, ic
from kit import CSS as KCSS, li, tile, num, quote, H1, WIPE, OUT, DRIFT

STEPS = ['Eligibility', 'E-EFMP', 'Submit PAR', 'Decision', 'Travel orders', 'Book travel']

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
    .rd i { font-style:normal; font-family:"JetBrains Mono"; font-size:24px; color:#7a756c; display:block; margin-top:12px; }
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


