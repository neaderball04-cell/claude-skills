"""CHAOS class generator: spec -> narration script, HyperFrames scenes, class book, QRG."""
import json, os, re, shutil, subprocess, sys, importlib.util
ROOT = os.environ.get('CHAOS_HOME', os.path.dirname(os.path.abspath(__file__)))
WORK = os.environ.get('CHAOS_WORK', '/home/claude/cls')

TEMPLATE = f'{ROOT}/template'
OUT = os.environ.get('CHAOS_OUT', '/home/claude/out')
MK = 'UNCLASSIFIED · training use'


def load(key):
    spec = importlib.util.spec_from_file_location(key, f'{WORK}/specs/{key}.py')
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


# ------------------------------------------------------------------ project
def setup(S):
    d = f'{WORK}/{S.K}/video'
    if not os.path.exists(d):
        os.makedirs(d)
        for f in os.listdir(TEMPLATE):
            if f in ('work', 'compositions', 'renders'):
                continue
            src = os.path.join(TEMPLATE, f)
            (shutil.copytree if os.path.isdir(src) else shutil.copy)(src, os.path.join(d, f))
        for f in os.listdir(os.path.join(d, 'tools')):
            p = os.path.join(d, 'tools', f)
            if p.endswith('.py'):
                s = open(p).read().replace('/home/claude/t2c2/video', d).replace(TEMPLATE, d).replace('CHAOS T2C2 Lite', 'CHAOS ' + S.BIG)
                open(p, 'w').write(s)
        for f in os.listdir(os.path.join(d, 'assets/voice')):
            os.remove(os.path.join(d, 'assets/voice', f))
        os.makedirs(os.path.join(d, 'compositions'), exist_ok=True)
    for f in os.listdir(f'{ROOT}/img'):
        shutil.copy(f'{ROOT}/img/{f}', f'{d}/assets/img/ph_{f}')
    for f in getattr(S, 'EXTRA_IMG', {}):
        shutil.copy(S.EXTRA_IMG[f], f'{d}/assets/img/ph_{f}.jpg')
    return d


def number_lines(S):
    n = 0
    for sc in S.SCENES:
        sc['ids'] = []
        for _ in sc['lines']:
            n += 1; sc['ids'].append(f'n{n}')


def write_script(S, d):
    number_lines(S)
    p = f'{d}/tools/mk_script.py'; s = open(p).read()
    head, tail = s.split('scenes = [', 1)[0], s.split(']\njson.dump', 1)[1]
    rows = []
    for i, sc in enumerate(S.SCENES):
        items = [f"('{lid}',N,{t!r},{0 if j == 0 else 0.3})" for j, (lid, t) in enumerate(zip(sc['ids'], sc['lines']))]
        rows.append(f" ('s{i+1:02d}',{3.2 if i == 0 else 0.4},0.7,[{','.join(items)}]),\n")
    open(p, 'w').write(head + 'scenes = [\n' + ''.join(rows) + ']\njson.dump' + tail)


def check_cues(S):
    number_lines(S)
    bad = []
    def walk(o, sc):
        if isinstance(o, dict):
            for k, v in o.items():
                if k == 'cue' and v:
                    if not any(v.lower() in l.lower() for l in sc['lines']): bad.append((sc.get('h'), v))
                else: walk(v, sc)
        elif isinstance(o, (list, tuple)):
            for v in o: walk(v, sc)
    for sc in S.SCENES:
        for pn in sc.get('panels', []): walk(pn, sc)
    return bad


# ------------------------------------------------------------------ scenes
SCENE_LIB = r'''
def T(sc, ph, back=0.15):
    """cue token for a phrase anywhere in the scene's lines"""
    for lid, line in zip(sc['ids'], sc['lines']):
        if ph.lower() in line.lower():
            return f'@@{lid}:{ph}@@ - {back}'
    raise SystemExit('cue missing: ' + ph)

def L(sc, i=0): return f'@@{sc["ids"][i]}@@'
COLS = ['#e3963e', '#7cc4f0', '#5fd07a', '#ff6a5c', '#d9b25a', '#c58bff']

def p_intro(sid, sc, pn, pid):
    h = nb(f'{pid}-n', 192, 190, 1540 if not pn.get('photo') else 900, pn['name'][0], pn['name'][1], '', 150)
    js = f'show("#{pid}-n", {T(sc, pn["name"][2])}, 0.45, {{ y:60 }});'
    if pn.get('chips'):
        h += chips(f'{pid}-c', 192, 400, 900 if pn.get('photo') else 1540, [c[0] for c in pn['chips']], '#e3963e', '#1b1d20', 38)
        js += stag(f'{pid}-c', T(sc, pn['chips'][0][1]), pn.get('gap', 0.5))
    if pn.get('photo'):
        im, cap, cu = pn['photo']
        h += photo(f'{pid}-ph', 1130, 190, 600, 700, im, cap)
        js += f'show("#{pid}-ph", {T(sc, cu)}, 0.6, {{ scale:0.4 }});' + kb(f'{pid}-ph', T(sc, cu), 12)
    if pn.get('quote'):
        t, em, cu = pn['quote']
        h += f'<div class="qt h" id="{pid}-q" style="left:192px;top:760px;width:900px;font-size:52px">{t} <em>{em}</em></div>'
        js += f'show("#{pid}-q", {T(sc, cu)}, 0.5, {{ y:60 }});'
    return h, js

def p_specs(sid, sc, pn, pid):
    w = 900 if pn.get('photo') else 1540
    h = f'<div class="h" id="{pid}-tb" style="position:absolute;left:192px;top:190px;width:{w}px">'
    h += ''.join(f'<div class="{pid}-r" style="display:flex;justify-content:space-between;gap:20px;border-bottom:2px solid #3a3a3e;padding:12px 8px;font-family:Barlow Semi Condensed;font-weight:700;font-size:{pn.get("fs",38)}px"><span style="color:#e3963e">{a}</span><span style="color:#efe9dc;text-align:right">{b}</span></div>' for a, b, _ in pn['rows']) + '</div>'
    js = f'tl.set("#{pid}-tb", {{ opacity:1 }}, {T(sc, pn["rows"][0][2], 0.3)});'
    js += ''.join(f'tl.fromTo("#{pid}-tb .{pid}-r:nth-child({i+1})", {{ opacity:0, x:-60 }}, {{ opacity:1, x:0, duration:0.3 }}, {T(sc, cu)});' for i, (_, _, cu) in enumerate(pn['rows']))
    if pn.get('photo'):
        im, cap, cu = pn['photo']
        h += photo(f'{pid}-ph', 1140, 190, 590, 720, im, cap) + f'<style>#{pid}-ph img{{object-fit:contain;background:#fff}}</style>'
        js += f'show("#{pid}-ph", {T(sc, cu)}, 0.6, {{ scale:0.5 }});'
    return h, js

def p_photos(sid, sc, pn, pid):
    it = pn['items']; n = len(it); cols = 3 if n > 4 else (2 if n > 1 else 1); rows = (n + cols - 1) // cols
    W = (1540 - (cols - 1) * 30) // cols; H = (760 - (rows - 1) * 30) // rows
    h = ''.join(photo(f'{pid}-p{i}', 192 + (i % cols) * (W + 30), 190 + (i // cols) * (H + 30), W, H, im, cap) for i, (im, cap, _) in enumerate(it))
    css = ''.join(f'#{pid}-p{i} img{{object-fit:contain;background:#fff}}' for i in range(n))
    js = ''.join(f'show("#{pid}-p{i}", {T(sc, cu)}, 0.4, {{ scale:0.6, rotation:{(-3,2,-2,3,-2,2)[i%6]} }});' for i, (_, _, cu) in enumerate(it))
    return f'<style>{css}</style>' + h, js

def p_steps(sid, sc, pn, pid):
    it = pn['items']; n = len(it); w = 900 if (pn.get('photo') or pn.get('side')) else 1540
    top = 190; avail = 600 if pn.get('note') else 760
    rh = min(140, avail // n); fs = 42 if rh >= 120 else (36 if rh >= 90 else (32 if rh >= 76 else 28))
    h = ''.join(f'<div class="drl h" id="{pid}-s{i}" style="left:192px;top:{top + i * rh}px;width:{w}px;height:{rh - 12}px;font-size:{fs}px;text-transform:none;font-family:Barlow Semi Condensed;font-weight:700"><b style="font-family:Alfa Slab One">{i+1}</b>{t}</div>' for i, (t, _) in enumerate(it))
    js = ''.join(f'show("#{pid}-s{i}", {T(sc, cu)}, 0.35, {{ x:-80 }});' for i, (_, cu) in enumerate(it))
    if pn.get('photo'):
        im, cap, cu = pn['photo']
        h += photo(f'{pid}-ph', 1140, 190, 590, 520, im, cap) + f'<style>#{pid}-ph img{{object-fit:contain;background:#fff}}</style>'
        js += f'show("#{pid}-ph", {T(sc, cu)}, 0.5, {{ scale:0.6 }});'
    if pn.get('side'):
        t, sub, cu, c = pn['side']
        h += nb(f'{pid}-sd', 1140, 740 if pn.get('photo') else 190, 590, t, sub, c, 170)
        js += f'show("#{pid}-sd", {T(sc, cu)}, 0.4, {{ x:80 }});'
        if not pn.get('photo'):
            im = pn.get('img', SPEC['HERO'])
            h += photo(f'{pid}-ph', 1140, 400, 590, 520, im, '') + f'<style>#{pid}-ph img{{object-fit:contain;background:#fff}}</style>'
            js += f'show("#{pid}-ph", {L(sc)} + 0.6, 0.5, {{ scale:0.7 }});'
    if pn.get('note'):
        t, sub, cu, c = pn['note']
        h += nb(f'{pid}-nt', 192, 820, w, t, sub, c, 130)
        js += f'show("#{pid}-nt", {T(sc, cu)}, 0.4, {{ y:60 }});'
    if pn.get('stamp'):
        t, cu = pn['stamp']
        h += f'<div class="stamp h" id="{pid}-st" style="left:{1180 if w < 1500 else 1100}px;top:{760 if pn.get("photo") else 560}px;font-size:46px;background:rgba(244,241,234,.92);transform:rotate(-6deg)">{t}</div>'
        js += f'slam("#{pid}-st", {T(sc, cu, 0)}, "#{sid}-cam", 8, 1.6);'
    return h, js

def p_cards(sid, sc, pn, pid):
    it = pn['items']; n = len(it); W = (1540 - (n - 1) * 35) // n; H = pn.get('hgt', 600)
    h = ''.join(card3(f'{pid}-c{i}', 192 + i * (W + 35), 200, W, H, top, title, body, col) for i, (top, title, body, col, _) in enumerate(it))
    js = ''.join(f'show("#{pid}-c{i}", {T(sc, cu)}, 0.45, {{ y:100, rotation:{(-3,3,-2,2)[i%4]} }});' for i, (*_, cu) in enumerate(it))
    if pn.get('stamp'):
        t, cu = pn['stamp']
        h += f'<div class="chip h" id="{pid}-st" style="left:192px;top:{220 + H}px;font-size:40px;background:#b23a2a;color:#fff">{t}</div>'
        js += f'slam("#{pid}-st", {T(sc, cu, 0)}, "#{sid}-cam", 6, 1.4);'
    return h, js

def p_table(sid, sc, pn, pid):
    a, b = pn['cols']; rows = pn['rows']; n = len(rows); rh = min(96, 640 // (n + 1))
    h = f'<div class="h" id="{pid}-tb" style="position:absolute;left:192px;top:190px;width:1540px">'
    h += f'<div style="display:grid;grid-template-columns:{pn.get("split","1fr 1.6fr")};background:#e3963e;color:#1b1d20;font-family:Barlow Semi Condensed;font-weight:700;font-size:32px;padding:8px 20px"><span>{a}</span><span>{b}</span></div>'
    h += ''.join(f'<div class="{pid}-r" style="display:grid;grid-template-columns:{pn.get("split","1fr 1.6fr")};min-height:{rh}px;align-items:center;padding:4px 20px;border-bottom:2px solid #3a3a3e;font-family:Barlow Semi Condensed;font-weight:700;font-size:{pn.get("fs",34)}px;color:#efe9dc"><span style="color:{pn.get("c1","#e3963e")}">{x}</span><span>{y}</span></div>' for x, y, _ in rows) + '</div>'
    js = f'tl.set("#{pid}-tb", {{ opacity:1 }}, {T(sc, rows[0][2], 0.4)});'
    js += ''.join(f'tl.fromTo("#{pid}-tb .{pid}-r:nth-of-type({i+1})", {{ opacity:0, x:80 }}, {{ opacity:1, x:0, duration:0.3 }}, {T(sc, cu)});' for i, (_, _, cu) in enumerate(rows))
    if pn.get('quote'):
        t, em, cu = pn['quote']
        h += f'<div class="qt h" id="{pid}-q" style="left:192px;top:850px;width:1540px;font-size:50px">{t} <em>{em}</em></div>'
        js += f'show("#{pid}-q", {T(sc, cu)}, 0.5, {{ y:60 }});'
    return h, js

def p_mistakes(sid, sc, pn, pid):
    it = pn['items']
    h = ''.join(drl(f'{pid}-m{i}', 192 + (i % 2) * 790, 200 + (i // 2) * 130, 750, '✕', t) for i, (t, _) in enumerate(it))
    h += f'<style>#{sid}-stage .drl{{font-size:30px}}</style>'
    js = ''.join(f'show("#{pid}-m{i}", {T(sc, cu)}, 0.3, {{ x:{-80 if i % 2 == 0 else 80} }});' for i, (_, cu) in enumerate(it))
    if pn.get('quote'):
        t, em, cu = pn['quote']
        h += f'<div class="qt h" id="{pid}-q" style="left:192px;top:{220 + ((len(it)+1)//2) * 130}px;width:1540px;font-size:60px">{t} <em>{em}</em></div>'
        js += f'show("#{pid}-q", {T(sc, cu)}, 0.5, {{ y:60 }}); shake("#{sid}-cam", {T(sc, cu, -0.4)}, 10);'
    return h, js

def p_chaos(sid, sc, pn, pid):
    h = ''; js = ''
    if pn.get('pace'):
        h += f'<div class="lab h" id="{pid}-pl" style="position:absolute;left:192px;top:180px;font-size:30px">{pn.get("pacelab","EXAMPLE PACE")}</div>'
        js += f'show("#{pid}-pl", {T(sc, pn["pace"][0][3], 0.4)}, 0.3);'
        for i, (l, t, c, cu) in enumerate(pn['pace']):
            h += f'<div class="h" id="{pid}-p{i}" style="position:absolute;left:192px;top:{230 + i * 115}px;width:760px;height:100px;display:flex;align-items:center;gap:18px;padding:0 18px;font-family:Barlow Semi Condensed;font-weight:700;font-size:34px;color:#efe9dc;background:#242427;border:3px solid #b8893a"><b style="font-family:Alfa Slab One;font-weight:400;font-size:50px;width:50px;color:{c}">{l}</b>{t}</div>'
            js += f'show("#{pid}-p{i}", {T(sc, cu)}, 0.3, {{ x:-60 }});'
        x, w = 1010, 720
    else:
        x, w = 192, 1540
    for i, (t, sub, c, cu) in enumerate(pn['items']):
        h += nb(f'{pid}-i{i}', x, 200 + i * 165, w, t, sub, c, 145)
        js += f'show("#{pid}-i{i}", {T(sc, cu)}, 0.4, {{ x:80 }});'
    if pn.get('quote'):
        t, em, cu = pn['quote']
        h += f'<div class="qt h" id="{pid}-q" style="left:{x}px;top:{220 + len(pn["items"]) * 165}px;width:{w}px;font-size:50px">{t} <em>{em}</em></div>'
        js += f'show("#{pid}-q", {T(sc, cu)}, 0.5, {{ y:60 }});'
    return h, js

PANELS = dict(intro=p_intro, specs=p_specs, photos=p_photos, steps=p_steps, cards=p_cards, table=p_table, mistakes=p_mistakes, chaos=p_chaos)

def build(G):
    S = {}; J = JSX
    SC = SPEC['SCENES']; n = len(SC)
    # title
    t = SC[0]
    S['s01'] = wrap('s01', CSS + f"""
    #s01-a {{ left:150px; top:120px; font-size:34px; }}
    #s01-t {{ left:150px; top:180px; font-size:{SPEC['BIGFS']}px; text-align:left; width:1100px; white-space:nowrap; }}
    #s01-box {{ left:150px; top:560px; width:880px; height:200px; text-align:left; }}
    #s01-logo {{ position:absolute; left:1480px; top:640px; width:330px; height:322px; }}
    #s01-ph img {{ object-fit:contain; background:#fff; }}""",
        '@@STEEL:s01@@' +
        '<div class="lab h" id="s01-a" style="position:absolute">Commander\'s class · CHAOS Troop</div>' +
        '<div class="big h" id="s01-t">' + ''.join(f'<span class="ch" style="display:inline-block">{"&nbsp;" if c == " " else c}</span>' for c in SPEC['BIG']) + '</div>' +
        f'<div class="sub h" id="s01-f" style="left:156px;top:400px;font-family:Alfa Slab One;font-size:52px;color:#efe9dc;width:960px;line-height:1.05">{SPEC["SUB"]}</div>' +
        f'<div class="tbox h" id="s01-box"><div style="font-family:Alfa Slab One,serif;font-size:54px;line-height:1.08;color:#e3963e;text-align:left">{SPEC["TAG"]}</div></div>' +
        f'<div class="sub h" id="s01-s" style="left:150px;top:800px;font-size:34px">{SPEC["REFS"]}</div>' +
        photo('s01-ph', 1180, 150, 600, 470, SPEC['HERO'], '') +
        '<img id="s01-logo" class="h" src="assets/img/chaos_logo.png" alt="CHAOS">' +
        '<div class="redbar h" id="s01-bar" style="left:60px;top:1010px;width:1040px"></div>',
        J + """
    show("#s01-a", 0.2, 0.5, { x:-60 });
    tl.set("#s01-t", { opacity:1 }, 0.35);
    tl.from("#s01-t .ch", { opacity:0, y:120, rotationX:-90, duration:0.5, stagger:0.07, ease:"back.out(2)" }, 0.35);
    show("#s01-f", 0.9, 0.5, { x:-80 });
    tl.set("#s01-box", { opacity:1 }, 1.3);
    tl.fromTo("#s01-box", { clipPath:"inset(0 100% 0 0)" }, { clipPath:"inset(0 0% 0 0)", duration:0.6, ease:"power3.inOut" }, 1.3);
    show("#s01-s", 1.8, 0.5, { y:30 });
    tl.set("#s01-ph", { opacity:1 }, 0.8);
    tl.fromTo("#s01-ph", { scale:0.2, opacity:0 }, { scale:1, opacity:1, duration:1.4, ease:"elastic.out(1,0.5)" }, 0.8);
    tl.fromTo("#s01-logo", { opacity:0, scale:0.3, rotation:-200 }, { opacity:1, scale:1, rotation:0, duration:1.0, ease:"back.out(1.4)" }, 1.6);
    tl.set("#s01-bar", { opacity:1 }, 1.9); tl.fromTo("#s01-bar", { scaleX:0, transformOrigin:"0 50%" }, { scaleX:1, duration:0.8, ease:"power3.out" }, 1.9);
    tl.to(["#s01-a","#s01-t","#s01-f","#s01-box","#s01-s","#s01-bar","#s01-ph"], { opacity:0, x:-80, duration:0.4, stagger:0.04, ease:"power2.in" }, @@DUR@@ - 0.5);
    tl.to("#s01-logo", { opacity:0, scale:1.4, duration:0.4 }, @@DUR@@ - 0.45);""")
    for i in range(1, n - 1):
        sc = SC[i]; sid = f's{i+1:02d}'
        body = '@@STEEL:' + sid + '@@' + H1(sid, sc['h'], 60)
        js = f'slam("#{sid}-h", {L(sc)}, "#{sid}-cam", 6, 1.3);'
        if sc.get('step'):
            body += f'<div class="h" id="{sid}-sp" style="position:absolute;left:1420px;top:70px;font-family:Barlow Semi Condensed;font-weight:700;font-size:32px;color:#1b1d20;background:#e3963e;padding:6px 16px;border-radius:4px">{sc["step"]}</div>'
            js += f'pop("#{sid}-sp", {L(sc)} + 0.3);'
        pans = sc['panels']
        for j, pn in enumerate(pans):
            pid = f'{sid}-g{j}'
            ph, pj = PANELS[pn['k']](sid, sc, pn, pid)
            if len(pans) > 1:
                body += f'<div class="h" id="{pid}" style="position:absolute;inset:0">{ph}</div>'
                li = pn.get('line', j)
                js += f'tl.set("#{pid}", {{ opacity:1 }}, {L(sc, li)});'
                if j + 1 < len(pans):
                    js += f'tl.to("#{pid}", {{ opacity:0, duration:0.4 }}, {L(sc, pans[j+1].get("line", j+1))} - 0.3);'
                js += pj
            else:
                body += ph; js += pj
        S[sid] = wrap(sid, CSS, body, WIPE(sid) + J + js + OUT(sid))
    c = SPEC['CLOSE']; lid = SC[-1]['ids'][0]
    sid = f's{n:02d}'
    S[sid] = wrap(sid, CSS + f'#{sid}-logo {{ position:absolute; left:1240px; top:180px; width:520px; height:508px; }}',
        f'@@STEEL:{sid}@@' + photo(f'{sid}-ph', 30, 30, 1860, 1020, SPEC['HERO'], '') +
        f'<img id="{sid}-logo" class="h" src="assets/img/chaos_logo.png" alt="CHAOS">' +
        f'<div class="h" id="{sid}-p" style="position:absolute;left:150px;top:260px;font-family:Alfa Slab One;font-size:92px;color:#efe9dc;line-height:1.15"><div class="{sid}-w">{c[0]}</div><div class="{sid}-w" style="color:#e3963e">{c[1]}</div><div class="{sid}-w">{c[2]}</div></div>' +
        f'<div class="bigq h" id="{sid}-c" style="left:150px;top:760px;font-size:130px;color:#ff6a5c">That\'s CHAOS!</div>',
        f"""
    tl.fromTo("#{sid}-stage", {{ clipPath:"circle(0% at 50% 50%)" }}, {{ clipPath:"circle(150% at 50% 50%)", duration:0.55, ease:"power2.inOut" }}, 0);
    tl.set("#{sid}-ph", {{ opacity:0.12 }}, 0);""" + kb(f'{sid}-ph', '0', 6, 1.2) + f"""
    tl.set("#{sid}-p", {{ opacity:1 }}, @@{lid}@@);
    tl.from(".{sid}-w", {{ opacity:0, x:-100, duration:0.3, stagger:0.45, ease:"back.out(2)" }}, @@{lid}@@);
    tl.fromTo("#{sid}-logo", {{ opacity:0, scale:0.3, rotation:-200 }}, {{ opacity:1, scale:1, rotation:0, duration:0.8, ease:"back.out(1.4)" }}, @@{lid}@@ + 0.2);
    slam("#{sid}-c", @@{lid}:That's CHAOS@@, "#{sid}-cam", 16, 1.7);""")
    return S

def SFX(cue):
    W = ('whoosh.mp3', 0.57, 0.4)
    n = len(SPEC['SCENES'])
    out = [(f's{i:02d}', 0.0) + W for i in range(2, n)]
    lid = SPEC['SCENES'][-1]['ids'][0]
    out += [('s01', 0.33, 'impact-bass-1.mp3', 2.1, 0.35), (f's{n:02d}', cue(f's{n:02d}', lid, "That's CHAOS") + 0.2 - 1.986, 'impact-bass-2.mp3', 2.59, 0.4)]
    return out
'''


def write_scenes(S, d):
    number_lines(S)
    head = open(f'{TEMPLATE}/tools/head5.py').read()
    spec = dict(SCENES=S.SCENES, BIG=S.BIG, SUB=S.SUB, TAG=S.TAG, REFS=S.REFS, HERO=S.HERO, CLOSE=S.CLOSE, BIGFS=getattr(S, 'BIGFS', 180))
    open(f'{d}/tools/scenes.py', 'w').write(head + '\nSPEC = ' + repr(spec) + '\n' + SCENE_LIB)


def run(cmd, cwd, timeout=None):
    r = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    return (r.stdout + r.stderr)[-2000:]


# ------------------------------------------------------------------ book / qrg
BOOK_CSS = open(f'{ROOT}/book/base_css.txt').read() + '''
.mk{position:absolute;left:0;right:0;text-align:center;font-family:C;font-size:8pt;letter-spacing:.08em;color:#fff;background:#3a3a3e;padding:2px 0}
.mk.t{top:0;border-radius:16px 16px 0 0}.mk.b{bottom:0;border-radius:0 0 16px 16px}
.ft{bottom:.32in}.in{padding-top:.5in}
.st{display:flex;gap:10px;margin:4px 0}.st>b{font-family:Slab;color:#1b1d20;background:#e3963e;min-width:26px;height:26px;text-align:center;line-height:26px;border-radius:4px;font-size:12pt;font-weight:400}
.st span{font-size:10.4pt;line-height:1.4}
.ph.w{background:#fff;object-fit:contain}
.cau{border-left:5px solid #ff6a5c;background:#2a2323;padding:6px 10px;font-size:10pt;margin:6px 0}.cau b{font-family:C;color:#ff6a5c}
p,li{font-size:11.4pt}.st span{font-size:11.2pt}table{font-size:10.8pt}td{padding:7px 8px}.lead{font-size:12.6pt}
.q .in{padding:.46in .34in .42in}
.q p,.q li,.q .st span{font-size:var(--qf,10pt);line-height:1.34}
.q h2{font-size:15pt;margin:12px 0 5px}
.q .st{margin:5px 0;gap:8px}.q .st>b{min-width:24px;height:24px;line-height:24px;font-size:11pt}
.q table{font-size:var(--qt,11pt)}.q td{padding:5px 6px}.q th{padding:5px 6px;font-size:var(--qt,11pt)}
.c3{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.box{background:#242427;border:1.5px solid #b8893a;border-radius:6px;padding:6px 8px}
.q .cau{font-size:9.4pt;padding:4px 8px;margin:4px 0}
.q .hd h1{font-size:22pt}
'''


def steps(items):
    return ''.join(f'<div class="st"><b>{i+1}</b><span>{t}</span></div>' for i, t in enumerate(items))


def tbl(rows, head=None):
    h = '<table>' + (('<tr>' + ''.join(f'<th>{x}</th>' for x in head) + '</tr>') if head else '')
    return h + ''.join('<tr>' + ''.join(f'<td>{x}</td>' for x in r) + '</tr>' for r in rows) + '</table>'


def img(f, h='2in', cap=''):
    return f'<img class="ph w" src="{f}.jpg" style="height:{h}">' + (f'<div class="cap">{cap}</div>' if cap else '')


def card(title, body, c='#e3963e'):
    return f'<div class="cd t" style="--c:{c}"><h3>{title}</h3>{body}</div>'


def page(S, n, kicker, title, body):
    MK = getattr(S, 'MK', globals()['MK'])
    return f'''<section class="pg"><div class="in"><div class="mk t">{MK}</div><div class="hd"><div><div class="k">{kicker}</div><h1>{title}</h1></div><div class="r"></div></div>{body}
<div class="ft"><span>CHAOS Troop · 578th SIGCO · {S.BIG} Class</span><span>{n}</span></div><div class="mk b">{MK}</div></div></section>'''


def cover(S):
    MK = getattr(S, 'MK', globals()['MK'])
    return f'''<section class="pg"><div class="in" style="padding:.7in"><div class="mk t">{MK}</div>
<div style="font-family:C;color:#d9b25a;font-size:14pt;letter-spacing:.08em;margin-top:.2in">Commander's class · CHAOS Troop</div>
<div style="font-family:Slab;color:#e3963e;font-size:{getattr(S, 'COVERFS', 80)}pt;line-height:1;margin-top:.1in;white-space:nowrap">{S.BIG}</div>
<div style="font-family:Slab;color:#f1ebdf;font-size:24pt;line-height:1.1;margin-top:.08in;width:4.6in">{S.NAME}</div>
<div style="margin-top:.35in;width:4.3in;border:3px solid #b8893a;background:#26262a;padding:.2in .28in;font-family:Slab;font-size:24pt;line-height:1.1;color:#e3963e">{S.TAG}</div>
<div style="margin-top:.3in;width:4.2in;font-size:12.5pt;line-height:1.45;color:#ddd8cc">{S.BLURB}</div>
<div style="margin-top:.18in;font-family:C;font-size:10.5pt;color:#d9b25a;width:4.4in">{S.REFS}</div>
<img src="{S.HERO}.jpg" style="position:absolute;right:.6in;top:4.6in;width:2.7in;border:4px solid #b8893a;background:#fff">
<img src="chaos_logo.png" style="position:absolute;right:.65in;top:.75in;width:2.1in">
<div style="position:absolute;left:.45in;bottom:.6in;width:4.4in;height:.13in;background:#b23a2a"></div>
<div style="position:absolute;left:.7in;bottom:.95in;font-family:C;font-size:10pt;color:#9d968a">578th Signal Company · RSS · 2d Cavalry Regiment</div>
<div class="mk b">{MK}</div></div></section>'''


def qpage(S, side, body, qf='10pt'):
    MK = getattr(S, 'MK', globals()['MK'])
    return f'''<section class="pg q" style="--qf:{qf}"><div class="in"><div class="mk t">{MK}</div><div class="hd"><div><div class="k">Quick reference guide · side {side} of 2</div><h1>{S.QTITLE}</h1></div><div class="r" style="display:flex;align-items:center;gap:8px"><span>CHAOS Troop · 578th SIGCO<br>{S.TM}</span><img src="chaos_logo.png" style="width:.55in"></div></div>{body}<div class="mk b">{MK}</div></div></section>'''


def build_docs(S):
    d = f'{WORK}/{S.K}/book'; os.makedirs(d, exist_ok=True)
    for f in os.listdir(f'{ROOT}/book'):
        if f.endswith('.woff2') or f == 'chaos_logo.png':
            shutil.copy(f'{ROOT}/book/{f}', d)
    for src in (f'{ROOT}/img',):
        for f in os.listdir(src): shutil.copy(f'{src}/{f}', d)
    for f in getattr(S, 'EXTRA_IMG', {}): shutil.copy(S.EXTRA_IMG[f], f'{d}/{f}.jpg')
    pages = [cover(S)] + [page(S, i + 2, k, t, b) for i, (k, t, b) in enumerate(S.BOOK)]
    open(f'{d}/book.html', 'w').write(f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>{BOOK_CSS}</style></head><body>' + ''.join(pages) + '</body></html>')
    q = [qpage(S, 1, S.QRG[0], getattr(S, 'QF', '12pt')), qpage(S, 2, S.QRG[1], getattr(S, 'QF', '12pt'))]
    open(f'{d}/qrg.html', 'w').write(f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>{BOOK_CSS}</style></head><body>' + ''.join(q) + '</body></html>')
    res = {}
    for nm, fn in (('book', f'CHAOS_{S.FILE}_Class_Book.pdf'), ('qrg', f'CHAOS_{S.FILE}_QRG.pdf')):
        os.makedirs(OUT, exist_ok=True); out = f'{OUT}/{fn}'
        run(f'google-chrome --headless=new --no-sandbox --disable-gpu --no-pdf-header-footer --virtual-time-budget=5000 --print-to-pdf={out} file://{d}/{nm}.html', d)
        res[nm] = run(f'pdfinfo {out} | grep Pages', d).strip()
    return res


if __name__ == '__main__':
    S = load(sys.argv[1]); act = sys.argv[2]
    if act == 'cues':
        print(check_cues(S) or 'cues ok')
    elif act == 'video':
        bad = check_cues(S)
        if bad: print('BAD CUES', bad); sys.exit(1)
        d = setup(S); write_script(S, d)
        print(run('python3 tools/mk_script.py && timeout 2400 python3 tools/tts.py >/dev/null 2>&1; ls work/raw_n*.wav | wc -l; python3 tools/mix.py | tail -1', d, 3000))
    elif act == 'scenes':
        d = f'{WORK}/{S.K}/video'; write_scenes(S, d)
        print(run('python3 tools/build.py 2>&1 | tail -3', d))
    elif act == 'docs':
        print(build_docs(S))
