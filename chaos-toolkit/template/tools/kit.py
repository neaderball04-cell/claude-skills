"""CHAOS SHARP class — scenes s01-s14."""
from base import wrap
from jb import it
from ea import CSS as ECSS, svg, person, ic, icsvg, card

CSS = ECSS + '''
    .phone { position:absolute; width:540px; height:900px; background:#0d0e10; border:14px solid #34383e; border-radius:58px; box-shadow:0 20px 0 rgba(0,0,0,.4); overflow:hidden; }
    .phone .hd { position:absolute; left:0; top:0; width:100%; height:120px; background:#1f2226; border-bottom:3px solid #d9a63a; }
    .phone .hd b { position:absolute; left:34px; top:22px; font-family:"Oswald"; font-weight:700; font-size:38px; color:#efe9dc; letter-spacing:.06em; }
    .phone .hd i { position:absolute; left:34px; top:76px; font-style:normal; font-family:"Oswald"; font-size:28px; color:#8d877b; letter-spacing:.12em; }
    .bub { position:absolute; max-width:400px; padding:16px 24px; border-radius:28px; font-family:"Oswald"; font-weight:500; font-size:32px; line-height:1.2; }
    .bub.l { left:26px; background:#2f3338; color:#efe9dc; border-bottom-left-radius:6px; }
    .bub.r { right:26px; background:#d9a63a; color:#1b1d20; border-bottom-right-radius:6px; }
    .bub small { display:block; font-size:20px; letter-spacing:.12em; color:#8d877b; text-transform:uppercase; margin-bottom:4px; }
    .bub.img { width:300px; height:200px; padding:0; background:repeating-linear-gradient(45deg,#3a3e45 0 18px,#2f3338 18px 36px); }
    .bub.img::after { content:"PHOTO"; position:absolute; inset:0; display:flex; align-items:center; justify-content:center; font-family:"Oswald"; font-weight:700; font-size:34px; letter-spacing:.3em; color:#8d877b; }
    .react { position:absolute; padding:6px 14px; background:#1f2226; border:3px solid #d9a63a; border-radius:30px; font-family:"Oswald"; font-weight:700; font-size:26px; color:#d9a63a; }
    .quote { position:absolute; background:#efe9dc; color:#1b1d20; font-family:"Oswald"; font-weight:600; font-size:54px; line-height:1.15; padding:34px 46px; border-radius:22px; box-shadow:0 14px 0 rgba(0,0,0,.35); }
    .quote::after { content:""; position:absolute; left:80px; bottom:-40px; border:22px solid transparent; border-top:22px solid #efe9dc; border-left:22px solid #efe9dc; }
    .quote .who { position:absolute; left:46px; top:-44px; height:44px; padding:0 18px; background:#d8352c; color:#fff; font-size:26px; letter-spacing:.16em; line-height:44px; text-transform:uppercase; }
    .node { position:absolute; background:#2a2d32; border-left:12px solid #d9a63a; box-shadow:0 10px 0 rgba(0,0,0,.3); padding:18px 24px; }
    .node b { display:block; font-family:"Oswald"; font-weight:700; font-size:40px; color:#efe9dc; text-transform:uppercase; line-height:1.05; }
    .node i { display:block; font-style:normal; font-family:"Oswald"; font-weight:500; font-size:28px; color:#b9b29e; margin-top:8px; line-height:1.2; }
    .node.r { border-left-color:#d8352c; } .node.g { border-left-color:#2e9e45; } .node.b { border-left-color:#4aa3df; }
    .ln { fill:none; stroke:#d9a63a; stroke-width:7; stroke-dasharray:1; stroke-linecap:round; }
    .li { position:absolute; display:flex; align-items:center; gap:22px; font-family:"Oswald"; font-weight:600; font-size:42px; color:#efe9dc; text-transform:uppercase; white-space:nowrap; }
    .li em { font-style:normal; display:inline-block; width:56px; height:56px; border-radius:50%; text-align:center; line-height:56px; font-family:"Archivo Black"; font-size:30px; }
    .li em.y { background:#2e9e45; color:#fff; } .li em.n { background:#d8352c; color:#fff; } .li em.g { background:#d9a63a; color:#1b1d20; }
    .tile { position:absolute; width:400px; height:200px; background:#2a2d32; border-top:10px solid #d9a63a; box-shadow:0 10px 0 rgba(0,0,0,.3); padding:22px 24px; }
    .tile b { display:block; font-family:"Archivo Black"; font-size:34px; color:#efe9dc; text-transform:uppercase; line-height:1.05; }
    .tile i { display:block; font-style:normal; font-family:"Oswald"; font-weight:500; font-size:27px; color:#b9b29e; margin-top:10px; line-height:1.2; }
    .doc { position:absolute; background:#fff; padding:10px; box-shadow:0 16px 0 rgba(0,0,0,.4); }
    .doc img { width:100%; height:100%; object-fit:contain; display:block; }
    .num { position:absolute; background:#1b1d20; border:5px solid #d9a63a; box-shadow:0 12px 0 rgba(0,0,0,.35); padding:22px 30px; }
    .num i { display:block; font-style:normal; font-family:"Oswald"; font-weight:700; font-size:28px; letter-spacing:.16em; color:#d9a63a; text-transform:uppercase; }
    .num b { display:block; font-family:"JetBrains Mono"; font-weight:800; font-size:64px; color:#efe9dc; line-height:1.1; margin-top:8px; white-space:nowrap; }
    .num s { display:block; text-decoration:none; font-family:"JetBrains Mono"; font-weight:700; font-size:32px; color:#b9b29e; margin-top:6px; white-space:nowrap; }
    .num.r { border-color:#d8352c; } .num.r i { color:#ff6b5e; }
    .bar { position:absolute; height:70px; background:#2a2d32; }
    .bar u { position:absolute; left:0; top:0; height:100%; width:100%; background:#d9a63a; transform-origin:0 50%; text-decoration:none; }
    .bar b { position:absolute; left:24px; top:12px; font-family:"Oswald"; font-weight:700; font-size:38px; color:#efe9dc; text-shadow:0 2px 0 #000, 0 0 8px #000; text-transform:uppercase; letter-spacing:.06em; z-index:2; }
    .x { position:absolute; width:120px; height:120px; }
    .it i { font-size:28px; } .bub small { font-size:28px; } .quote .who { font-size:30px; } .tile i { font-size:30px; }
'''

def phone(pid, x, y, title, sub, inner):
    return f'<div class="phone h" id="{pid}" style="left:{x}px;top:{y}px"><div class="hd"><b>{title}</b><i>{sub}</i></div>{inner}</div>'

def bub(bid, side, top, text, who=''):
    w = f'<small>{who}</small>' if who else ''
    return f'<div class="bub {side} h" id="{bid}" style="top:{top}px">{w}{text}</div>'

def node(nid, x, y, w, a, b='', kind=''):
    i = f'<i>{b}</i>' if b else ''
    return f'<div class="node {kind} h" id="{nid}" style="left:{x}px;top:{y}px;width:{w}px"><b>{a}</b>{i}</div>'

def li(lid, x, y, mark, text, kind='y', size=42):
    return f'<div class="li h" id="{lid}" style="left:{x}px;top:{y}px;font-size:{size}px"><em class="{kind}">{mark}</em>{text}</div>'

def tile(tid, x, y, a, b, kind='', w=400, h=200):
    col = {'r': '#d8352c', 'g': '#2e9e45', 'b': '#4aa3df'}.get(kind)
    st = f';border-top-color:{col}' if col else ''
    return f'<div class="tile h" id="{tid}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px{st}"><b>{a}</b><i>{b}</i></div>'

def doc(did, src, x, y, w, h, rot=0):
    return f'<div class="doc h" id="{did}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({rot}deg)"><img src="assets/img/{src}" alt=""></div>'

def num(nid, x, y, label, big, small='', kind=''):
    s = f'<s>{small}</s>' if small else ''
    return f'<div class="num {kind} h" id="{nid}" style="left:{x}px;top:{y}px"><i>{label}</i><b>{big}</b>{s}</div>'

def quote(qid, x, y, w, who, text):
    return f'<div class="quote h" id="{qid}" style="left:{x}px;top:{y}px;width:{w}px"><div class="who">{who}</div>{text}</div>'

def xmark(xid, x, y, size=120):
    return f'<svg id="{xid}" class="x h" viewBox="-60 -60 120 120" style="left:{x}px;top:{y}px;width:{size}px;height:{size}px" data-layout-ignore><circle r="54" fill="#d8352c"/><path d="M-24 -24L24 24M24 -24L-24 24" stroke="#fff" stroke-width="14" stroke-linecap="round"/></svg>'

def chk(xid, x, y, size=120):
    return f'<svg id="{xid}" class="x h" viewBox="-60 -60 120 120" style="left:{x}px;top:{y}px;width:{size}px;height:{size}px" data-layout-ignore><circle r="54" fill="#2e9e45"/><path d="M-26 2L-8 20L26 -18" fill="none" stroke="#fff" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/></svg>'

H1 = lambda sid, txt, top=70: f'<div class="disp h1 h" id="{sid}-h" style="top:{top}px;font-size:84px">{txt}</div>'
WIPE = lambda sid: f'tl.fromTo("#{sid}-stage", {{ clipPath:"inset(0% 100% 0% 0%)" }}, {{ clipPath:"inset(0% 0% 0% 0%)", duration:0.45, ease:"power2.inOut" }}, 0);'
DRIFT = lambda sid: f'tl.fromTo("#{sid}-stage", {{ scale:1 }}, {{ scale:1.045, duration:@@DUR@@, ease:"none" }}, 0);'
OUT = lambda sid: DRIFT(sid) + f'tl.to("#{sid}-cam > *:not(svg.full)", {{ opacity:0, y:-40, duration:0.3, stagger:0.01, ease:"power2.in" }}, @@DUR@@ - 0.4);'


def build(G):
    S = {}

    # ------------------------------------------------------------ s01 hook: group chat
    chat = (bub('s01-b1', 'l', 160, 'Who\'s going to the Volksfest tmrw?', 'PFC Diaz') +
            bub('s01-b2', 'l', 300, '', 'SPC Ward') +
            '<div class="bub l img h" id="s01-img" style="top:350px"></div>' +
            bub('s01-b3', 'l', 580, 'lol look at her 😂😂', 'SPC Ward') +
            '<div class="react h" id="s01-r1" style="left:300px;top:660px">😂 4</div>' +
            '<div class="react h" id="s01-r2" style="left:390px;top:660px">👁 12 SEEN</div>')
    S['s01'] = wrap('s01', CSS + '''
    #s01-t { left:140px; top:120px; }
    #s01-big1 { position:absolute; left:140px; top:330px; font-size:120px; color:#efe9dc; }
    #s01-big2 { position:absolute; left:140px; top:470px; font-size:120px; color:#d8352c; }
    #s01-sub { position:absolute; left:144px; top:640px; font-size:44px; color:#d9a63a; width:900px; white-space:normal; }
    #s01-cnt { position:absolute; left:140px; top:330px; font-size:140px; color:#d9a63a; }
    #s01-cntl { position:absolute; left:146px; top:530px; font-size:40px; color:#b9b29e; }''',
        '@@STEEL:s01@@' + '<div class="chip h" id="s01-t">Fri 2300 · Rose Barracks</div>' +
        phone('s01-ph', 1220, 90, '1ST PLT 🔥', '14 MEMBERS', chat) +
        '<div class="disp h" id="s01-cnt">12 seen</div><div class="lab h" id="s01-cntl">4 laughed · 0 said a word</div>' +
        '<div class="disp h" id="s01-big1">Silence</div><div class="disp h" id="s01-big2">is where it starts</div>' +
        '<div class="lab h" id="s01-sub">And where we stop it.</div>',
        '''
    show("#s01-t", @@n1@@, 0.4, { x:-80 });
    show("#s01-ph", @@n1@@ + 0.2, 0.6, { y:200 });
    pop("#s01-b1", @@n1:Rose Barracks@@);
    pop("#s01-b2", @@n1:drops@@); pop("#s01-img", @@n1:photo@@);
    pop("#s01-b3", @@n1:crude@@);
    show("#s01-cnt", @@n2@@, 0.4, { x:-60 });
    pop("#s01-r2", @@n2:see it@@); pop("#s01-r1", @@n2:Four laugh@@);
    show("#s01-cntl", @@n2:Nobody@@, 0.35, { y:30 });
    hide(["#s01-cnt", "#s01-cntl", "#s01-t"], @@n3@@ + 0.3, 0.25, { y:-50 });
    slam("#s01-big1", @@n3:silence@@ + 0.3, "#s01-cam", 10, 1.5);
    slam("#s01-big2", @@n3:sexual harassment@@, "#s01-cam", 12, 1.5);
    show("#s01-sub", @@n3:stop it@@ - 0.1, 0.4, { x:-60 });
    tl.to("#s01-ph", { x:700, opacity:0, duration:0.5, ease:"power2.in" }, @@n3@@);''' + DRIFT('s01'))

    # ------------------------------------------------------------ s02 title
    S['s02'] = wrap('s02', CSS + '''
    #s02-logo { position:absolute; left:120px; top:250px; width:560px; height:547px; }
    #s02-w1 { position:absolute; left:760px; top:210px; font-size:230px; color:#d8352c; }
    #s02-w2 { position:absolute; left:770px; top:450px; font-size:54px; color:#efe9dc; }
    #s02-tags { position:absolute; left:770px; top:560px; }''',
        '@@STEEL:s02@@' + '''
      <img id="s02-logo" class="h" src="assets/img/chaos_logo.png" alt="CHAOS Troop">
      <div class="disp h" id="s02-w1">SHARP</div>
      <div class="disp h" id="s02-w2">Know it · Report it · Stop it</div>''' +
        it('s02-i1', 770, 580, 'USAREUR-AF Cmd Memo 2025-013', 'SHARP policy · 21 JUL 25', w=920) +
        it('s02-i2', 770, 700, '7th ATC Command Policy Letter 2', 'SHARP & responsibilities · 9 APR 26', 'r', w=920) +
        it('s02-i3', 770, 820, 'Options · rights · who to call', 'DoD SAPR flyers · hotlines', 'g', w=920),
        '''
    tl.fromTo("#s02-stage", { clipPath:"circle(0% at 50% 50%)" }, { clipPath:"circle(150% at 50% 50%)", duration:0.55, ease:"power2.inOut" }, 0);
    tl.fromTo("#s02-logo", { opacity:0, scale:2.3, rotation:-16 }, { opacity:1, scale:1, rotation:0, duration:0.24, ease:"power4.in" }, 0.32);
    shake("#s02-cam", 0.56, 16);
    slam("#s02-w1", @@n4:SHARP training@@, "#s02-cam", 10, 1.6);
    show("#s02-w2", @@n4:Sexual Harassment@@, 0.45, { x:80 });
    show("#s02-i1", @@n5:USAREUR-AF@@ - 0.1, 0.4, { x:120 });
    show("#s02-i2", @@n5:Seventh Army@@ - 0.1, 0.4, { x:120 });
    show("#s02-i3", @@n5:reporting options@@ - 0.1, 0.4, { x:120 });
    ''' + OUT('s02'))

    # ------------------------------------------------------------ s03 commander's intent
    bars = ''.join(f'<div class="bar h" id="s03-bar{i}" style="left:1000px;top:{330 + i * 110}px;width:760px"><u id="s03-u{i}"></u><b>{t}</b></div>' for i, t in enumerate(['Teamwork', 'Unit cohesion', 'Combat readiness']))
    ppl = ''.join(f'<div class="h" id="s03-p{i}" style="position:absolute;left:{1000 + i * 260}px;top:760px;width:240px;text-align:center">{svg("s03-ps" + str(i), 0, 0, 240, 150, person(120, 140, 1.3, c), cls="", extra=";position:relative")}<div class="lab" style="font-size:34px;color:#d9a63a;margin-top:8px">{t}</div></div>' for i, (t, c) in enumerate([('Soldiers', '#efe9dc'), ('Army Civilians', '#d9a63a'), ('Family', '#b9b29e')]))
    S['s03'] = wrap('s03', CSS + '''
    #s03-q { position:absolute; left:140px; top:240px; width:760px; font-family:"Oswald"; font-weight:600; font-size:56px; line-height:1.18; color:#efe9dc; white-space:normal; }
    #s03-q em { font-style:normal; color:#d8352c; }
    #s03-src { position:absolute; left:140px; top:660px; font-size:30px; color:#8d877b; }
    #s03-zero { left:140px; top:780px; font-size:72px; padding:14px 34px; }''',
        '@@STEEL:s03@@' + H1('s03', "Commander's intent") +
        '<div class="h" id="s03-q">Sexual harassment, sexual assault &amp; retaliation are <em>incompatible with Army values.</em></div>' +
        '<div class="lab h" id="s03-src">GEN Donahue · AEA Cmd Memo 2025-013</div>' + bars + ppl +
        '<div class="stamp h" id="s03-zero">Not tolerated</div>',
        WIPE('s03') + '''
    slam("#s03-h", @@n6@@, "#s03-cam", 6, 1.3);
    show("#s03-q", @@n6:sexual harassment@@ - 0.2, 0.5, { y:40 });
    show("#s03-src", @@n6:incompatible@@, 0.4);
    [0,1,2].forEach(i => show("#s03-bar" + i, @@n7@@ - 0.2 + i * 0.08, 0.3, { x:80 }));
    tl.to("#s03-u0", { scaleX:0.18, background:"#d8352c", duration:0.5, ease:"power3.in" }, @@n7:destroy@@);
    tl.to("#s03-u1", { scaleX:0.22, background:"#d8352c", duration:0.5, ease:"power3.in" }, @@n7:wreck@@);
    tl.to("#s03-u2", { scaleX:0.12, background:"#d8352c", duration:0.5, ease:"power3.in" }, @@n7:degrade@@);
    shake("#s03-cam", @@n7:degrade@@ + 0.5, 8);
    slam("#s03-zero", @@n8:not tolerated@@, "#s03-cam", 12, 1.8);
    pop("#s03-p0", @@n8:every Soldier@@); pop("#s03-p1", @@n8:Army Civilian@@); pop("#s03-p2", @@n8:Family@@);
    ''' + OUT('s03'))

    # ------------------------------------------------------------ s04 sexual harassment: 3 ways
    S['s04'] = wrap('s04', CSS + '''
    .row { height:130px; } .row b { height:130px; line-height:130px; width:130px; font-size:72px; } .row i { left:160px; top:20px; } .row span { left:160px; top:58px; font-size:44px; }
    #s04-tag1 { left:1260px; top:860px; } #s04-tag2 { left:1260px; top:950px; background:#d8352c; color:#fff; }''',
        '@@STEEL:s04@@' + H1('s04', 'Sexual harassment · AR 600-52') +
        '<div class="row h" id="s04-r1" style="top:230px;width:1100px"><b>1</b><i>Quid pro quo</i><span>Sex tied to job · pay · career</span></div>' +
        quote('s04-c1', 1320, 210, 480, 'SGT · to a PFC', '"Be nicer to me &amp; that 4-day pass is yours."') +
        '<div class="stamp h" id="s04-qp" style="left:1340px;top:470px;font-size:52px">Quid pro quo</div>' +
        '<div class="row red h" id="s04-r2" style="top:420px;width:1100px"><b>2</b><i>Hostile environment</i><span>Severe or pervasive · reasonable person</span></div>' +
        '<div class="chip h" id="s04-mp" style="left:1310px;top:610px;background:#2a2d32;color:#efe9dc;font-size:34px">Daily body comments · motor pool bay</div>' +
        '<div class="row h" id="s04-r3" style="top:610px;width:1100px"><b>3</b><i>Anyone · any rank</i><span>Deliberate / repeated unwelcome remarks</span></div>' +
        tile('s04-t1', 192, 820, 'No harm required', 'No proof of psychological damage needed', 'r', 520, 180) +
        tile('s04-t2', 740, 820, 'Online counts', 'Group chats · Snapchat · DMs · social media', 'b', 520, 180) +
        f'<div class="h" id="s04-ph" style="position:absolute;left:1360px;top:780px">{icsvg("phone", "#4aa3df", 220)}</div>',
        WIPE('s04') + '''
    slam("#s04-h", @@n9@@, "#s04-cam", 6, 1.3);
    show("#s04-r1", @@n10@@ - 0.1, 0.45, { x:-120 });
    show("#s04-c1", @@c1@@ - 0.15, 0.45, { scale:0.6, y:40 });
    slam("#s04-qp", @@n11:quid pro quo@@, "#s04-cam", 8, 1.6);
    hide(["#s04-c1", "#s04-qp"], @@n12@@ - 0.3, 0.25);
    show("#s04-r2", @@n12@@ - 0.1, 0.45, { x:-120 });
    show("#s04-mp", @@n12:daily comments@@ - 0.1, 0.4, { x:60 });
    show("#s04-r3", @@n13@@ - 0.1, 0.45, { x:-120 });
    hide("#s04-mp", @@n14@@ - 0.3, 0.25);
    show("#s04-t1", @@n14:psychological harm@@ - 0.2, 0.4, { y:60 });
    show("#s04-t2", @@n14:online@@ - 0.1, 0.4, { y:60 });
    pop("#s04-ph", @@n14:Group chats@@);
    tl.to("#s04-ph", { rotation:8, duration:0.08, yoyo:true, repeat:9, ease:"none" }, @@n14:Group chats@@ + 0.35);
    ''' + OUT('s04'))

    # ------------------------------------------------------------ s05 sexual assault + consent
    offs = ['Rape', 'Sexual assault', 'Aggravated sexual contact', 'Abusive sexual contact', 'Forcible sodomy', 'Attempts']
    offl = ''.join(f'<div class="chip h" id="s05-o{i}" style="left:{192 + (i % 3) * 520}px;top:{470 + (i // 3) * 90}px;background:#2a2d32;color:#efe9dc;font-size:34px">{t}</div>' for i, t in enumerate(offs))
    nots = [('Didn\'t fight back', 'n0'), ('Asleep', 'n1'), ('Unconscious', 'n2'), ('Too drunk to stand', 'n3')]
    notl = ''.join(li(f's05-{k}', 240 + (i % 2) * 760, 760 + (i // 2) * 100, '✕', t, 'n', 46) for i, (t, k) in enumerate(nots))
    S['s05'] = wrap('s05', CSS + '''
    #s05-def { position:absolute; left:192px; top:200px; width:1536px; font-family:"Oswald"; font-weight:600; font-size:46px; line-height:1.25; color:#efe9dc; white-space:normal; }
    #s05-def em { font-style:normal; color:#d9a63a; }
    #s05-nc { left:1240px; top:636px; font-size:56px; }
    #s05-any { left:192px; top:960px; font-size:38px; }''',
        '@@STEEL:s05@@' + H1('s05', 'Sexual assault &amp; consent') +
        '<div class="h" id="s05-def">Intentional sexual contact by <em>force, threats, intimidation or abuse of authority</em>, or when the victim <em>does not or cannot consent.</em></div>' +
        offl + '<div class="disp h" id="s05-ch" style="position:absolute;left:192px;top:670px;font-size:54px;color:#d9a63a">Consent ≠</div>' + notl +
        '<div class="stamp h" id="s05-nc">No consent</div>' +
        '<div class="chip h" id="s05-any">Any sex · any rank · even in marriage</div>',
        WIPE('s05') + '''
    slam("#s05-h", @@n15@@, "#s05-cam", 6, 1.3);
    show("#s05-def", @@n15:intentional@@, 0.5, { y:40 });
    ''' + ''.join(f'pop("#s05-o{i}", @@n16:{p}@@);' for i, p in enumerate(['rape', 'sexual assault', 'aggravated', 'abusive', 'forcible', 'attempts'])) + '''
    tl.to(["#s05-def"], { opacity:0.35, duration:0.3 }, @@n17@@);
    show("#s05-ch", @@n17:consent@@ - 0.1, 0.35, { x:-60 });
    show("#s05-n0", @@n17:Not fighting@@, 0.35, { x:-60 });
    show("#s05-n1", @@n17:asleep@@ - 0.1, 0.35, { x:-60 });
    show("#s05-n2", @@n17:unconscious@@ - 0.1, 0.35, { x:-60 });
    show("#s05-n3", @@n17:too drunk@@ - 0.1, 0.35, { x:-60 });
    tl.to(["#s05-n0","#s05-n1","#s05-n2","#s05-n3"], { opacity:0.25, duration:0.2 }, @@n17:Period@@ - 0.25);
    slam("#s05-nc", @@n17:Period@@ - 0.1, "#s05-cam", 14, 1.8);
    show("#s05-any", @@n18@@, 0.4, { y:40 });
    ''' + OUT('s05'))

    # ------------------------------------------------------------ s06 SH reporting options
    cols = [('Anonymous', 'Hotline / in writing · no name · investigated if who-what-when-where', '', 'eye'),
            ('Confidential', 'SARC or VA · support & services · no command, no investigation', 'b', 'shield'),
            ('Formal', 'DA Form 7746 with SARC · command notified · investigated · timelines', 'r', 'gavel')]
    colh = ''.join(card(f's06-k{i}', 192 + i * 520, 200, 490, 470, t, b, ico, k, {'': '#d9a63a', 'b': '#4aa3df', 'r': '#d8352c'}[k]) for i, (t, b, k, ico) in enumerate(cols))
    S['s06'] = wrap('s06', CSS + '''
    #s06-di { position:absolute; left:192px; top:720px; width:1536px; height:280px; background:#1b1d20; border:5px dashed #2e9e45; padding:24px 30px; }
    #s06-di h3 { font-family:"Archivo Black"; font-size:44px; color:#2e9e45; text-transform:uppercase; }
    #s06-di p { font-family:"Oswald"; font-weight:500; font-size:32px; color:#c9c2b2; margin-top:10px; }
    #s06-say { left:1060px; top:735px; font-size:36px; padding:16px 26px; }''',
        '@@STEEL:s06@@' + H1('s06', 'Harassment · 3 ways to report') + colh +
        '<div class="h" id="s06-di"><h3>+ Direct intervention</h3><p>A peer pulls them aside: "Knock it off." Low-level behavior only.</p></div>' +
        quote('s06-say', 1180, 745, 480, 'Peer', '"Knock it off."') +
        ''.join(li(f's06-x{i}', 230 + i * 470, 895, '✕', t, 'n', 40) for i, t in enumerate(['Touching', 'Quid pro quo', 'Boss → subordinate'])),
        WIPE('s06') + '''
    slam("#s06-h", @@n19@@, "#s06-cam", 6, 1.3);
    show("#s06-k0", @@n20@@ - 0.15, 0.45, { y:80 });
    show("#s06-k1", @@n21@@ - 0.15, 0.45, { y:80 });
    show("#s06-k2", @@n22@@ - 0.15, 0.45, { y:80 });
    tl.to(["#s06-k0","#s06-k1","#s06-k2"], { y:-30, scale:0.92, duration:0.4 }, @@n23@@ - 0.3);
    show("#s06-di", @@n23@@, 0.45, { y:60 });
    pop("#s06-say", @@n23:knock it off@@ - 0.2);
    hide("#s06-say", @@n23:low-level@@, 0.2);
    pop("#s06-x0", @@n23:touching@@); pop("#s06-x1", @@n23:quid pro quo@@); pop("#s06-x2", @@n23:a boss@@);
    ''' + OUT('s06'))

    # ------------------------------------------------------------ s07 investigation flow
    flow = '''<path id="s07-a1" class="ln" pathLength="1" d="M560 300H660"/><path id="s07-a2" class="ln" pathLength="1" d="M1180 300H1260"/>
      <path id="s07-a3" class="ln" pathLength="1" d="M1520 410V520H1000V600"/><path id="s07-a4" class="ln" pathLength="1" d="M1520 410V600" style="stroke:#d8352c"/>'''
    S['s07'] = wrap('s07', CSS + '''
    #s07-eeo { left:192px; top:950px; font-size:34px; background:#4aa3df; color:#0d1014; }''',
        '@@STEEL:s07@@' + H1('s07', 'After a formal complaint') +
        svg('s07-fl', 0, 0, 1920, 1080, flow, cls='') +
        node('s07-n1', 192, 220, 360, 'Formal complaint', 'DA Form 7746') +
        node('s07-n2', 670, 220, 500, 'SHIO appointed', 'From outside the subject\'s battalion', 'b') +
        node('s07-n3', 1270, 220, 460, 'AR 15-6 investigation', '1LT / GS-12+ · SHIC trained') +
        node('s07-n4', 680, 610, 600, 'Minor → rehabilitate', 'Refresher training · corrective counseling · monitoring', 'g') +
        node('s07-n5', 1330, 610, 400, 'Non-minor', 'Quid pro quo · superior touching subordinate · repeat offender', 'r') +
        '<div class="stamp h" id="s07-sep" style="left:1170px;top:880px;font-size:48px">Separation initiated</div>' +
        '<div class="chip h" id="s07-eeo">DA Civilians → EEO within 45 days</div>',
        WIPE('s07') + '''
    slam("#s07-h", @@n24@@, "#s07-cam", 6, 1.3);
    show("#s07-n1", @@n24:formal complaint@@ - 0.1, 0.4, { x:-60 });
    draw("#s07-a1", @@n24:appoints@@ - 0.3, 0.3);
    show("#s07-n2", @@n24:appoints@@, 0.4, { x:-60 });
    tl.fromTo("#s07-n2", { boxShadow:"0 0 0 0 #4aa3df" }, { boxShadow:"0 0 0 14px rgba(74,163,223,0)", duration:0.8, repeat:1 }, @@n24:outside@@);
    draw("#s07-a2", @@n25@@ - 0.3, 0.3);
    show("#s07-n3", @@n25@@, 0.4, { x:-60 });
    draw("#s07-a4", @@n26:non-minor@@ - 0.2, 0.4);
    show("#s07-n5", @@n26:non-minor@@ + 0.1, 0.4, { y:60 });
    slam("#s07-sep", @@n26:involuntary separation@@ - 0.1, "#s07-cam", 12, 1.7);
    draw("#s07-a3", @@n27@@ - 0.3, 0.5);
    show("#s07-n4", @@n27@@ + 0.1, 0.4, { y:60 });
    show("#s07-eeo", @@n28@@, 0.4, { x:-80 });
    ''' + OUT('s07'))

    # ------------------------------------------------------------ s08 restricted vs unrestricted
    rl = ['Medical care & SAFE exam', 'Advocate & counseling', 'Special Victims\' Counsel', 'No investigation · no ID to command']
    ul = ['Everything restricted gets', 'CID investigation', 'Command notified', 'MPO · expedited transfer']
    S['s08'] = wrap('s08', CSS + '''
    .door { position:absolute; top:200px; width:720px; height:560px; background:#2a2d32; box-shadow:0 14px 0 rgba(0,0,0,.35); border-top:14px solid #4aa3df; padding:28px 34px; }
    .door h3 { font-family:"Archivo Black"; font-size:62px; text-transform:uppercase; color:#efe9dc; }
    .door h4 { font-family:"Oswald"; font-weight:600; font-size:30px; letter-spacing:.14em; color:#4aa3df; text-transform:uppercase; margin-top:6px; }
    #s08-u { border-top-color:#d8352c; } #s08-u h4 { color:#ff6b5e; }
    #s08-who { left:192px; top:790px; font-size:34px; }
    #s08-sw { position:absolute; left:930px; top:420px; width:60px; }
    #s08-first { left:520px; top:900px; font-size:56px; padding:20px 40px; background:#2e9e45; color:#fff; }''',
        '@@STEEL:s08@@' + H1('s08', 'Sexual assault · 2 options') +
        '<div class="door h" id="s08-r" style="left:192px"><h3>Restricted</h3><h4>Confidential</h4></div>' +
        '<div class="door h" id="s08-u" style="left:1008px"><h3>Unrestricted</h3><h4>Investigation</h4></div>' +
        ''.join(li(f's08-r{i}', 230, 380 + i * 90, '✓', t, 'y', 34) for i, t in enumerate(rl)) +
        ''.join(li(f's08-u{i}', 1046, 380 + i * 90, '✓', t, 'y' if i else 'g', 34) for i, t in enumerate(ul)) +
        '<div class="chip h" id="s08-who">Only a SARC · VA · healthcare can take a restricted report</div>' +
        svg('s08-arr', 900, 270, 120, 120, '<path d="M10 60H100M70 30L104 60L70 90" fill="none" stroke="#2e9e45" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>') +
        svg('s08-arr2', 900, 600, 120, 120, '<path d="M110 60H20M50 30L16 60L50 90" fill="none" stroke="#d8352c" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/><path d="M30 20L90 100M90 20L30 100" stroke="#d8352c" stroke-width="10"/>') +
        '<div class="chip h" id="s08-first">1st call: SARC / VA</div>',
        WIPE('s08') + '''
    slam("#s08-h", @@n29@@, "#s08-cam", 6, 1.3);
    show("#s08-r", @@n30@@ - 0.15, 0.45, { x:-100 });
    ''' + ''.join(f'show("#s08-r{i}", @@n30:{p}@@ - 0.1, 0.3, {{ x:-40 }});' for i, p in enumerate(['medical care', 'counseling', 'a lawyer', 'No investigation'])) + '''
    show("#s08-who", @@n31@@, 0.4, { y:40 });
    show("#s08-u", @@n32@@ - 0.15, 0.45, { x:100 });
    ''' + ''.join(f'show("#s08-u{i}", @@n32:{p}@@ - 0.1, 0.3, {{ x:40 }});' for i, p in enumerate(['unrestricted', 'CID', 'notifies', 'justice'])) + '''
    hide("#s08-who", @@n33@@ - 0.2, 0.2);
    pop("#s08-arr", @@n33:switch@@); pop("#s08-arr2", @@n33:can't go back@@);
    shake("#s08-cam", @@n33:can't go back@@ + 0.3, 8);
    slam("#s08-first", @@n34:SARC@@ - 0.1, "#s08-cam", 10, 1.6);
    ''' + OUT('s08'))

    # ------------------------------------------------------------ s09 still eligible? + connect to care
    S['s09'] = wrap('s09', CSS + '''
    #s09-yes { left:192px; top:470px; font-size:40px; background:#2e9e45; color:#fff; }
    #s09-no { left:1010px; top:470px; font-size:40px; background:#d8352c; color:#fff; }
    #s09-c2c { left:192px; top:960px; font-size:40px; }''',
        '@@STEEL:s09@@' +
        quote('s09-f1', 300, 150, 1320, 'Soldier', '"I told my squad leader. Is it too late to keep it restricted?"') +
        '<div class="chip h" id="s09-yes">Still can file restricted</div>' +
        li('s09-y0', 200, 560, '✓', 'Command found out', 'y', 36) + li('s09-y1', 200, 640, '✓', 'Someone else called police', 'y', 36) +
        '<div class="chip h" id="s09-no">Not restricted if</div>' +
        li('s09-n0', 1018, 560, '✕', 'You reported to police / CID', 'n', 36) + li('s09-n1', 1018, 640, '✕', 'You signed unrestricted', 'n', 36) +
        svg('s09-fl', 0, 0, 1920, 1080, '<path id="s09-a1" class="ln" pathLength="1" d="M560 820H700"/><path id="s09-a2" class="ln" pathLength="1" d="M1100 820H1240"/>', cls='') +
        node('s09-m1', 192, 760, 360, 'Soldier tells you', 'Any leader') +
        node('s09-m2', 710, 760, 380, 'Notify CID', 'Commander\'s duty', 'r') +
        node('s09-m3', 1250, 760, 480, 'Walk them to SARC', 'Direct, personal handoff', 'g') +
        '<div class="chip h" id="s09-c2c">Connect to Care · not just a phone number</div>',
        WIPE('s09') + '''
    show("#s09-f1", @@f1@@ - 0.15, 0.45, { scale:0.7, y:40 });
    show("#s09-yes", @@n35@@, 0.35, { x:-60 });
    show("#s09-y0", @@n35:command found out@@ - 0.1, 0.3, { x:-40 });
    show("#s09-y1", @@n35:called police@@ - 0.2, 0.3, { x:-40 });
    show("#s09-no", @@n36@@, 0.35, { x:60 });
    show("#s09-n0", @@n36:personally@@, 0.3, { x:40 });
    show("#s09-n1", @@n36:signed@@, 0.3, { x:40 });
    show("#s09-m1", @@n37:If a Soldier@@ - 0.1, 0.4, { y:50 });
    draw("#s09-a1", @@n37:notify CID@@ - 0.3, 0.3);
    show("#s09-m2", @@n37:notify CID@@, 0.4, { y:50 });
    draw("#s09-a2", @@n37:walk them@@ - 0.3, 0.3);
    show("#s09-m3", @@n37:walk them@@, 0.4, { y:50 });
    slam("#s09-c2c", @@n37:Connect to Care@@, "#s09-cam", 8, 1.5);
    ''' + OUT('s09'))

    # ------------------------------------------------------------ s10 rights + protections
    rights = [('Protected', 'from the accused'), ('Notice', 'of hearings'), ('Be present', '& be heard'), ('Confer', 'with prosecutor'),
              ('Restitution', 'per law'), ('No delay', 'unreasonable'), ('Dignity', 'fairness & privacy'), ('Your views', 'on disposition')]
    rt = ''.join(tile(f's10-t{i}', 192 + (i % 4) * 392, 190 + (i // 4) * 170, a, b, '', 370, 150) for i, (a, b) in enumerate(rights))
    S['s10'] = wrap('s10', CSS + '''
    .tile b { font-size:32px; } #s10-svc { left:192px; top:560px; }''',
        '@@STEEL:s10@@' + H1('s10', 'Your rights &amp; protections', 60) + rt +
        it('s10-svc', 192, 560, 'Special Victims\' Counsel', 'Free · your own military lawyer · confidential', 'b', 760) +
        num('s10-n1', 192, 700, 'Expedited transfer', '5 DAYS', 'Command answers') +
        num('s10-n2', 690, 700, 'Military protective order', '6 HRS', 'O-6 · once warranted', 'r') +
        tile('s10-catch', 1250, 700, 'CATCH program', 'Anonymously submit suspect info · stop serial offenders', 'g', 540, 220),
        WIPE('s10') + '''
    slam("#s10-h", @@n38@@, "#s10-cam", 6, 1.3);
    ''' + ''.join(f'pop("#s10-t{i}", @@{l}:{p}@@ - 0.05);' for i, (l, p) in enumerate([('n38', 'protected'), ('n38', 'notice'), ('n38', 'present'), ('n39', 'prosecutor'), ('n39', 'restitution'), ('n39', 'delay'), ('n39', 'dignity'), ('n39', 'privacy')])) + '''
    show("#s10-svc", @@n40@@ - 0.1, 0.4, { x:-80 });
    show("#s10-n1", @@n41:expedited transfer@@ - 0.1, 0.4, { y:60 });
    show("#s10-n2", @@n41:military protective order@@ - 0.1, 0.4, { y:60 });
    tl.fromTo("#s10-n2 b", { scale:1.4 }, { scale:1, duration:0.3, ease:"back.out(3)" }, @@n41:six hours@@);
    show("#s10-catch", @@n42@@ - 0.1, 0.4, { y:60 });
    ''' + OUT('s10'))

    # ------------------------------------------------------------ s11 safe to report
    exc = ['"I was drinking underage"', '"I was out past curfew"', '"I\'ll get in trouble"']
    mins = ['Underage drinking', 'Unprofessional relationship', 'Curfew / off-limits location', 'Barracks policy violation']
    S['s11'] = wrap('s11', CSS + '''
    #s11-sh { position:absolute; left:1150px; top:190px; }
    #s11-st { left:1100px; top:430px; font-size:90px; color:#2e9e45; border-color:#2e9e45; }''',
        '@@STEEL:s11@@' + H1('s11', 'Safe to Report') +
        ''.join(quote(f's11-e{i}', 192, 250 + i * 200, 660, 'Excuse', t) for i, t in enumerate(exc)) +
        ''.join(xmark(f's11-x{i}', 950, 250 + i * 200, 110) for i in range(3)) +
        f'<div class="h" id="s11-sh">{icsvg("shield", "#2e9e45", 220)}</div>' +
        '<div class="stamp h" id="s11-st">Protected</div>' +
        ''.join(li(f's11-m{i}', 1100, 610 + i * 92, '✓', t, 'y', 34) for i, t in enumerate(mins)) +
        doc('s11-doc', 'enc07.png', 1650, 130, 220, 285, 4),
        WIPE('s11') + '''
    slam("#s11-h", @@n43@@, "#s11-cam", 6, 1.3);
    show("#s11-e0", @@n43:underage@@ - 0.3, 0.35, { x:-60 });
    show("#s11-e1", @@n43:curfew@@ - 0.3, 0.35, { x:-60 });
    show("#s11-e2", @@n43:in trouble@@ - 0.3, 0.35, { x:-60 });
    slam("#s11-x0", @@n44:says no@@ - 0.1, null); slam("#s11-x1", @@n44:says no@@ + 0.1, null); slam("#s11-x2", @@n44:says no@@ + 0.3, "#s11-cam", 10);
    pop("#s11-sh", @@n44:Minor@@);
    slam("#s11-st", @@n44:will not be punished@@, "#s11-cam", 8, 1.6);
    ''' + ''.join(f'show("#s11-m{i}", @@n45:{p}@@ - 0.1, 0.3, {{ x:60 }});' for i, p in enumerate(['Underage', 'unprofessional', 'curfew', 'barracks'])) + '''
    show("#s11-doc", @@n45:Report anyway@@ - 0.3, 0.5, { y:120, rotation:-10 });
    ''' + OUT('s11'))

    # ------------------------------------------------------------ s12 retaliation
    chat = (bub('s12-b1', 'l', 160, 'Great. Now we\'ve got a snitch in the platoon.', 'SGT —') +
            bub('s12-b2', 'r', 340, 'SPC Lee was removed from the group', '') +
            bub('s12-b3', 'l', 480, 'Lee\'s off the promotion board list', 'SGT —'))
    S['s12'] = wrap('s12', CSS + '''
    #s12-art { position:absolute; left:780px; top:200px; font-size:120px; color:#d8352c; }
    #s12-def { position:absolute; left:780px; top:350px; width:960px; font-family:"Oswald"; font-weight:600; font-size:40px; line-height:1.25; color:#efe9dc; white-space:normal; }''',
        '@@STEEL:s12@@' + phone('s12-ph', 150, 110, '2ND PLT', '22 MEMBERS', chat) +
        '<div class="disp h" id="s12-art">Art. 132</div>' +
        '<div class="h" id="s12-def">Threatening or taking adverse action, or withholding a good one, to discourage a report.</div>' +
        li('s12-l0', 790, 560, '!', 'Pulled from promotion board', 'n', 36) +
        li('s12-l1', 790, 640, '!', 'Kicked out of the group chat', 'n', 36) +
        li('s12-l2', 790, 720, '!', 'Cold-shouldered at formation', 'n', 36) +
        it('s12-ig', 790, 840, 'Inspector General', 'Military reprisal', 'r', 460) +
        it('s12-osc', 1280, 840, 'Office of Special Counsel', 'Civilians · 5 USC 2302(b)(8)', 'b', 470),
        WIPE('s12') + '''
    show("#s12-ph", 0.2, 0.5, { y:150 });
    pop("#s12-b1", @@c2@@);
    slam("#s12-art", @@n46:Article 132@@ - 0.2, "#s12-cam", 12, 1.7);
    show("#s12-def", @@n47@@, 0.45, { y:40 });
    pop("#s12-b3", @@n47:promotion board@@ - 0.3);
    show("#s12-l0", @@n47:promotion board@@, 0.3, { x:60 });
    pop("#s12-b2", @@n48:Kicking@@);
    show("#s12-l1", @@n48:Kicking@@, 0.3, { x:60 });
    show("#s12-l2", @@n48:Cold-shouldering@@, 0.3, { x:60 });
    show("#s12-ig", @@n49:Inspector General@@ - 0.1, 0.4, { y:60 });
    show("#s12-osc", @@n49:Civilians@@, 0.4, { y:60 });
    ''' + OUT('s12'))

    # ------------------------------------------------------------ s13 numbers
    S['s13'] = wrap('s13', CSS + '''
    #s13-111 { left:1340px; top:820px; }''',
        '@@STEEL:s13@@' + H1('s13', 'Save these numbers now', 60) +
        num('s13-a', 192, 190, '7th ATC 24/7 hotline · Vilseck · Graf · Hohenfels', 'DSN 314-569-4567', '+49 9641-70-569-4567', 'r') +
        num('s13-b', 192, 450, 'USAREUR-AF 24/7 SHARP helpline', 'DSN 314-537-4277', '53-SHARP') +
        num('s13-c', 192, 690, 'DoD Safe Helpline · 24/7/365', '877-995-5247', 'DSN 314-537-7233 · safehelpline.org · app') +
        num('s13-d', 1340, 450, 'Emergency', '112', 'Police · ambulance', 'r') +
        doc('s13-doc', 'enc06.png', 1360, 140, 220, 285, 5),
        WIPE('s13') + '''
    slam("#s13-h", @@n50@@, "#s13-cam", 6, 1.3);
    show("#s13-a", @@n50:Seventh ATC@@ - 0.2, 0.45, { x:-100 });
    show("#s13-doc", @@n50:Commercial@@, 0.5, { y:100, rotation:-8 });
    show("#s13-b", @@n51@@ - 0.1, 0.45, { x:-100 });
    tl.fromTo("#s13-b s", { color:"#b9b29e" }, { color:"#d9a63a", duration:0.3 }, @@n51:53-SHARP@@);
    show("#s13-c", @@n52@@ - 0.1, 0.45, { x:-100 });
    slam("#s13-d", @@n52:emergency@@, "#s13-cam", 10, 1.6);
    ''' + OUT('s13'))

    # ------------------------------------------------------------ s14 close
    chat = (bub('s14-b3', 'l', 160, 'lol look at her 😂😂', 'SPC Ward') +
            bub('s14-b4', 'r', 300, 'Not cool. Delete it. Now.', 'You') +
            bub('s14-b5', 'l', 470, 'Ward, my office. 0800.', 'SSG Ruiz') +
            bub('s14-b6', 'l', 620, 'deleted. my bad.', 'SPC Ward'))
    S['s14'] = wrap('s14', CSS + '''
    #s14-logo { position:absolute; left:1570px; top:670px; width:300px; height:293px; }
    #s14-w { position:absolute; left:130px; top:250px; font-size:96px; color:#efe9dc; line-height:1.1; }
    #s14-w em { font-style:normal; color:#d9a63a; }
    #s14-c { position:absolute; left:130px; top:720px; font-size:160px; color:#d8352c; }''',
        '@@STEEL:s14@@' + phone('s14-ph', 1220, 90, '1ST PLT 🔥', '14 MEMBERS', chat) +
        '<img id="s14-logo" class="h" src="assets/img/chaos_logo.png" alt="CHAOS">' +
        '<div class="disp h" id="s14-w">Know the policy.<br>Know the <em>options.</em><br>Have each other\'s backs.</div>' +
        '<div class="disp h" id="s14-c">That\'s CHAOS.</div>',
        '''
    tl.fromTo("#s14-stage", { clipPath:"circle(0% at 50% 50%)" }, { clipPath:"circle(150% at 50% 50%)", duration:0.55, ease:"power2.inOut" }, 0);
    show("#s14-ph", 0.2, 0.5, { y:150 });
    pop("#s14-b3", 0.5);
    pop("#s14-b4", @@n53:not cool@@ - 0.1);
    pop("#s14-b5", @@n53:One leader@@);
    pop("#s14-b6", @@n53:stepped in@@ + 0.4);
    hide("#s14-ph", @@n54@@ - 0.3, 0.3, { x:200 });
    show("#s14-w", @@n54@@, 0.5, { x:-80 });
    tl.fromTo("#s14-logo", { opacity:0, scale:2.3, rotation:-16 }, { opacity:1, scale:1, rotation:0, duration:0.24, ease:"power4.in" }, @@n54:CHAOS@@ - 0.3);
    slam("#s14-c", @@n54:That's CHAOS@@, "#s14-cam", 16, 1.7);''' + DRIFT('s14'))
    return S


def SFX(cue):
    W = ('whoosh.mp3', 0.57, 0.4)
    P = lambda sid, lid, ph, off=0: (sid, cue(sid, lid, ph) + off - 0.12, 'pop.mp3', 0.5, 0.3)
    I = lambda sid, t: (sid, t - 0.07, 'impact-bass-1.mp3', 2.1, 0.35)
    out = [(f's{i:02d}', 0.0) + W for i in range(3, 14)]
    out += [
        P('s01', 'n1', 'photo'), P('s01', 'n1', 'crude'), P('s01', 'n2', 'Four laugh'),
        I('s01', cue('s01', 'n3', 'silence') + 0.2), I('s01', cue('s01', 'n3', 'sexual harassment') + 0.2),
        I('s02', 0.56), I('s02', cue('s02', 'n4', 'SHARP training') + 0.2),
        I('s03', cue('s03', 'n8', 'not tolerated') + 0.2),
        I('s04', cue('s04', 'n11', 'quid pro quo') + 0.2),
        I('s05', cue('s05', 'n17', 'Period') + 0.1),
        P('s06', 'n23', 'touching'), P('s06', 'n23', 'quid pro quo'), P('s06', 'n23', 'a boss'),
        I('s07', cue('s07', 'n26', 'involuntary separation') + 0.1),
        I('s08', cue('s08', 'n34', 'SARC') + 0.1),
        I('s09', cue('s09', 'n37', 'Connect to Care') + 0.2),
        I('s11', cue('s11', 'n44', 'will not be punished') + 0.2),
        I('s12', cue('s12', 'n46', 'Article 132')),
        I('s13', cue('s13', 'n52', 'emergency') + 0.2),
        P('s14', 'n53', 'not cool', -0.1),
        ('s14', cue('s14', 'n54', "That's CHAOS") + 0.2 - 1.986, 'impact-bass-2.mp3', 2.59, 0.4),
    ]
    return out
