"""Shared wrap/CSS."""

def wrap(sid, css, body, js):
    return f'''<template>
  <style>@@CSS@@{EXTRA_CSS}{css}
  </style>
  <div id="root" data-composition-id="{sid}" data-width="1920" data-height="1080">
    <div class="stage" id="{sid}-stage"><div class="cam" id="{sid}-cam">
{body}
    </div></div>
  </div>
  <script>
  (() => {{@@JS@@
{js}
    window.__timelines["{sid}"] = tl;
  }})();
  </script>
</template>
'''

EXTRA_CSS = '''
    .row { position:absolute; left:192px; width:1536px; height:150px; background:#2a2d32; box-shadow:0 10px 0 rgba(0,0,0,.3); }
    .row b { position:absolute; left:0; top:0; width:160px; height:150px; background:#d9a63a; color:#1b1d20; font-family:"Archivo Black"; font-size:88px; line-height:150px; text-align:center; }
    .row i { position:absolute; left:200px; top:26px; font-style:normal; font-family:"Oswald"; font-weight:600; font-size:30px; letter-spacing:.2em; color:#b9b29e; text-transform:uppercase; white-space:nowrap; }
    .row span { position:absolute; left:200px; top:66px; font-family:"Oswald"; font-weight:600; font-size:52px; color:#efe9dc; text-transform:uppercase; letter-spacing:.02em; white-space:nowrap; }
    .row.red b { background:#d8352c; color:#fff; }
    .badge { position:absolute; background:#d8352c; color:#fff; font-family:"Oswald"; font-weight:700; font-size:40px; letter-spacing:.14em; padding:12px 24px; text-transform:uppercase; white-space:nowrap; line-height:1; }
    .h1 { position:absolute; left:192px; top:118px; font-size:96px; color:#efe9dc; }
'''

