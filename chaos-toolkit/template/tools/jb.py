"""Shared JBC-P art: photo plates, cards, step tags."""

CSS = '''
    .ph { position:absolute; background:#efe9dc; box-shadow:0 14px 0 rgba(0,0,0,.35); padding:14px; }
    .ph img { width:100%; height:100%; object-fit:contain; display:block; }
    .ph .cap { position:absolute; left:0; bottom:-58px; height:46px; padding:0 18px; background:#d9a63a; font-family:"Oswald"; font-weight:700; font-size:26px; letter-spacing:.1em; color:#1b1d20; text-transform:uppercase; line-height:46px; white-space:nowrap; }
    .ph .num { position:absolute; left:-22px; top:-22px; width:64px; height:64px; background:#b3201b; color:#efe9dc; font-family:"Archivo Black"; font-size:34px; line-height:64px; text-align:center; box-shadow:0 6px 0 rgba(0,0,0,.35); }
    .ok { position:absolute; right:-18px; top:-18px; width:62px; height:62px; border-radius:50%; background:#2e9e45; border:5px solid #efe9dc; }
    .ok::after { content:""; position:absolute; left:15px; top:9px; width:16px; height:28px; border:solid #fff; border-width:0 7px 7px 0; transform:rotate(45deg); }
    .it { position:absolute; width:520px; height:96px; background:#2a2d32; border-left:12px solid #d9a63a; box-shadow:0 8px 0 rgba(0,0,0,.3); padding:0 22px; display:flex; flex-direction:column; justify-content:center; }
    .it b { font-family:"Oswald"; font-weight:700; font-size:40px; color:#efe9dc; text-transform:uppercase; line-height:1; white-space:nowrap; }
    .it i { font-style:normal; font-family:"Oswald"; font-weight:600; font-size:22px; letter-spacing:.14em; color:#b9b29e; text-transform:uppercase; margin-top:8px; white-space:nowrap; }
    .it.r { border-left-color:#d8352c; } .it.g { border-left-color:#2e9e45; }
    .hl { position:absolute; border:6px solid #d9a63a; box-shadow:0 0 0 4px rgba(27,29,32,.5); }
    .stamp { position:absolute; padding:8px 26px; border:8px solid #d8352c; color:#d8352c; font-family:"Archivo Black"; font-size:64px; text-transform:uppercase; transform:rotate(-6deg); white-space:nowrap; background:rgba(27,29,32,.6); }
    .lcd { position:absolute; border:12px solid #111214; border-radius:10px; background:#a6c9a0; box-shadow:0 14px 0 rgba(0,0,0,.35); }
    .lcd img { width:100%; height:100%; object-fit:contain; display:block; }
    .ring { position:absolute; width:96px; height:96px; margin:-48px 0 0 -48px; border-radius:50%; border:8px solid #d9a63a; box-shadow:0 0 0 4px rgba(27,29,32,.6); }
    .tag { position:absolute; padding:6px 16px; background:#d9a63a; color:#1b1d20; font-family:"Oswald"; font-weight:700; font-size:30px; letter-spacing:.06em; text-transform:uppercase; white-space:nowrap; box-shadow:0 6px 0 rgba(0,0,0,.35); }
    .fouo { position:absolute; left:0; width:1920px; top:1040px; text-align:center; font-family:"Oswald"; font-weight:600; font-size:20px; letter-spacing:.3em; color:#8d877b; }
'''

def ph(pid, src, x, y, w, h, cap='', num='', ok=False, cls='h'):
    c = f'<div class="cap">{cap}</div>' if cap else ''
    n = f'<div class="num">{num}</div>' if num else ''
    k = f'<div class="ok h" id="{pid}-ok"></div>' if ok else ''
    return f'<div class="ph {cls}" id="{pid}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><img src="assets/img/{src}" alt="">{c}{n}{k}</div>'

def it(iid, x, y, a, b, kind='', w=520):
    return f'<div class="it {kind} h" id="{iid}" style="left:{x}px;top:{y}px;width:{w}px"><b>{a}</b><i>{b}</i></div>'

FOUO = '<div class="fouo">UNCLASSIFIED // FOR OFFICIAL USE ONLY</div>'

def lcd(lid, src, x, y, w, h, cls='h'):
    return f'<div class="lcd {cls}" id="{lid}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><img src="assets/img/{src}" alt=""></div>'
