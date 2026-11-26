"""Ethics class art: icons, figures, cards. All SVG, centered at 0,0 (~100px box)."""
from jb import CSS as JCSS

CSS = JCSS + '''
    .card { position:absolute; background:#2a2d32; box-shadow:0 12px 0 rgba(0,0,0,.35); border-top:10px solid #d9a63a; padding:22px 26px; }
    .card.r { border-top-color:#d8352c; } .card.g { border-top-color:#2e9e45; } .card.b { border-top-color:#4aa3df; }
    .card h3 { font-family:"Archivo Black"; font-size:46px; color:#efe9dc; text-transform:uppercase; line-height:1; }
    .card p { margin-top:12px; font-family:"Oswald"; font-weight:500; font-size:32px; color:#c9c2b2; line-height:1.25; }
    .card svg.ic { display:block; margin:0 0 14px; }
    .big { position:absolute; left:0; width:1920px; text-align:center; }
    .yr { position:absolute; font-family:"Archivo Black"; font-size:120px; color:#d9a63a; line-height:1; }
'''

def svg(sid, x, y, w, h, inner, vb=None, cls='h', extra=''):
    vb = vb or f'0 0 {w} {h}'
    return f'<svg id="{sid}" class="{cls}" viewBox="{vb}" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px{extra}" data-layout-ignore>{inner}</svg>'

def person(x, y, s=1, c='#efe9dc', gid='', cls=''):
    g = f' id="{gid}"' if gid else ''
    k = f' class="{cls}"' if cls else ''
    return f'<g transform="translate({x} {y}) scale({s})"><g{g}{k}><circle cx="0" cy="-62" r="16" fill="{c}"/><path d="M-22 -40Q0 -48 22 -40L26 0H14L12 40H-12L-14 0H-26Z" fill="{c}"/></g></g>'

def ic(name, c='#d9a63a', s=1):
    P = {
        'house': f'<path d="M-40 0L0 -36L40 0V38H-40Z" fill="none" stroke="{c}" stroke-width="7" stroke-linejoin="round"/><rect x="-10" y="12" width="20" height="26" fill="{c}"/>',
        'heart': f'<path d="M0 36C-50 2 -44 -36 -18 -36C-6 -36 0 -26 0 -20C0 -26 6 -36 18 -36C44 -36 50 2 0 36Z" fill="{c}"/>',
        'town': f'<rect x="-44" y="-10" width="24" height="46" fill="{c}"/><rect x="-14" y="-36" width="28" height="72" fill="{c}"/><rect x="20" y="-20" width="24" height="56" fill="{c}"/>',
        'shield': f'<path d="M0 -44L38 -30V2C38 26 20 40 0 48C-20 40 -38 26 -38 2V-30Z" fill="{c}"/><path d="M-14 2L-2 14L18 -12" fill="none" stroke="#1b1d20" stroke-width="8" stroke-linecap="round"/>',
        'gavel': f'<rect x="-30" y="-36" width="44" height="22" rx="4" transform="rotate(-35)" fill="{c}"/><rect x="-6" y="-14" width="10" height="56" transform="rotate(-35)" fill="{c}"/><rect x="-44" y="34" width="60" height="10" fill="{c}"/>',
        'pulse': f'<path d="M-48 0H-20L-10 -30L4 30L14 -10L20 0H48" fill="none" stroke="{c}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>',
        'crack': f'<path d="M0 36C-50 2 -44 -36 -18 -36C-6 -36 0 -26 0 -20C0 -26 6 -36 18 -36C44 -36 50 2 0 36Z" fill="{c}"/><path d="M0 -20L-8 -2L6 8L-4 30" fill="none" stroke="#1b1d20" stroke-width="6"/>',
        'eye': f'<path d="M-48 0Q0 -40 48 0Q0 40 -48 0Z" fill="none" stroke="{c}" stroke-width="7"/><circle r="14" fill="{c}"/>',
        'cam': f'<rect x="-36" y="-22" width="58" height="44" rx="6" fill="{c}"/><path d="M22 -10L44 -22V22L22 10Z" fill="{c}"/><circle cx="-8" r="10" fill="#1b1d20"/>',
        'q': f'<circle r="40" fill="none" stroke="{c}" stroke-width="7"/><text y="20" text-anchor="middle" font-family="Archivo Black" font-size="56" fill="{c}">?</text>',
        'split': f'<rect x="-40" y="-40" width="40" height="80" fill="#efe9dc"/><rect x="0" y="-40" width="40" height="80" fill="#111214" stroke="#efe9dc" stroke-width="4"/>',
        'scale': f'<path d="M0 -40V40M-30 40H30M-46 -24H46" stroke="{c}" stroke-width="7" stroke-linecap="round"/><path d="M-46 -24L-60 10H-32ZM46 -24L32 10H60Z" fill="{c}"/>',
        'book': f'<path d="M-44 -34H-4Q0 -30 0 -26V40Q-4 34 -10 34H-44Z M44 -34H4Q0 -30 0 -26V40Q4 34 10 34H44Z" fill="{c}"/>',
        'star': f'<path d="M0 -44L12 -14L44 -14L18 6L28 38L0 18L-28 38L-18 6L-44 -14L-12 -14Z" fill="{c}"/>',
        'dove': f'<path d="M-44 6C-20 -6 -6 -30 14 -30C28 -30 36 -20 44 -24C40 -10 30 -6 24 -4C24 20 0 34 -26 30L-12 18C-26 18 -38 14 -44 6Z" fill="{c}"/>',
        'cross': f'<rect x="-8" y="-46" width="16" height="92" fill="{c}"/><rect x="-32" y="-24" width="64" height="16" fill="{c}"/>',
        'phone': f'<rect x="-24" y="-44" width="48" height="88" rx="8" fill="#111214" stroke="{c}" stroke-width="5"/><circle cx="12" cy="-28" r="7" fill="#d8352c"/>',
        'drill': f'<rect x="-40" y="-30" width="80" height="60" rx="6" fill="none" stroke="{c}" stroke-width="7"/><path d="M-26 -8H26M-26 10H12" stroke="{c}" stroke-width="7" stroke-linecap="round"/>',
    }
    return f'<g transform="scale({s})">{P[name]}</g>'

def icsvg(name, c='#d9a63a', size=110, sid='', cls=''):
    i = f' id="{sid}"' if sid else ''
    k = f' class="{cls}"' if cls else ''
    return f'<svg{i}{k} class="ic" width="{size}" height="{size}" viewBox="-60 -60 120 120" data-layout-ignore>{ic(name, c)}</svg>'

def card(cid, x, y, w, h, title, body='', icon=None, kind='', ic_c='#d9a63a'):
    i = icsvg(icon, ic_c, 96) if icon else ''
    b = f'<p>{body}</p>' if body else ''
    return f'<div class="card {kind} h" id="{cid}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">{i}<h3>{title}</h3>{b}</div>'
