import asyncio,json,re,glob,os,functools,threading,http.server
from playwright.async_api import async_playwright
ROOT='/home/claude/t2c2/video';FS='/home/claude/smx/pdf/node_modules/@fontsource'
class Q(http.server.SimpleHTTPRequestHandler):
  def log_message(self,*a):pass
srv=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Q,directory='/'));port=srv.server_address[1]
threading.Thread(target=srv.serve_forever,daemon=True).start()
ff=''
for fam,d,ws in [('Archivo Black','archivo-black',[400]),('Oswald','oswald',[400,500,600,700]),('JetBrains Mono','jetbrains-mono',[400,500,600,700])]:
  for w in ws:
    f=f'{FS}/{d}/files/{d}-latin-{w}-normal.woff2'
    if os.path.exists(f):ff+=f'@font-face{{font-family:"{fam}";font-weight:{w};src:url("http://127.0.0.1:{port}{f}")}}'
JS='''(sid)=>{const out={};const R=document.getElementById('root').getBoundingClientRect();
document.querySelectorAll('[id^="'+sid+'-"]').forEach(e=>{if(e.closest('.host')||e.closest('[data-layout-ignore]'))return;const r=e.getBoundingClientRect();
if(r.width&&r.height)out[e.id]=[r.left-R.left,r.top-R.top,r.width,r.height];});return out;}'''
async def main():
  res={}
  async with async_playwright() as p:
    b=await p.chromium.launch();pg=await b.new_page(viewport={'width':1920,'height':1080})
    for fn in sorted(glob.glob(f'{ROOT}/compositions/s*.html')):
      sid=os.path.basename(fn)[:-5];h=open(fn).read()
      h=h.replace('<template>','').replace('</template>','');h=re.sub(r'<script>.*?</script>','',h,flags=re.S)
      h=h.replace('src="assets/',f'src="http://127.0.0.1:{port}{ROOT}/assets/')
      await pg.set_content(f'<html><head><style>{ff} body{{margin:0;width:1920px;height:1080px;position:relative}}</style></head><body>{h}</body></html>')
      await pg.evaluate('document.fonts.ready');await pg.wait_for_timeout(150)
      res[sid]=await pg.evaluate(JS,sid)
    await b.close()
  json.dump(res,open(f'{ROOT}/work/boxes.json','w'))
  print({k:len(v) for k,v in res.items()})
asyncio.run(main())
