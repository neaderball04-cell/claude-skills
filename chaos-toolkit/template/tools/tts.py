import json, subprocess, os, sys, concurrent.futures as cf
sys.path.insert(0,'/home/claude/t2c2/video/tools')
from accent import german
os.chdir('/home/claude/t2c2/video')
S=json.load(open('tools/script.json'))
jobs=[]
for sc in S['scenes']:
    for lid,v,text,gap in sc['lines']:
        out=f'work/raw_{lid}.wav'
        if not os.path.exists(out): jobs.append((lid,v,text,out))
def run(j):
    lid,v,text,out=j; vv=S['voices'][v]

    tmp=out.replace('raw_','pre_') if v=='n' else out
    r=subprocess.run(['npx','-y','hyperframes@0.9.58','tts',text,'-v',vv['voice'],'-s',str(vv['speed']),'-o',tmp,'--json'],capture_output=True,text=True)
    if v=='n' and os.path.exists(tmp):
        subprocess.run(['ffmpeg','-y','-loglevel','error','-i',tmp,'-af','highpass=f=80,equalizer=f=3000:t=q:w=1.2:g=2,acompressor=threshold=-20dB:ratio=3:makeup=2,alimiter=limit=0.95',out])
    return lid, r.stdout.strip()[-200:], r.stderr.strip()[-200:] if r.returncode else ''
with cf.ThreadPoolExecutor(2) as ex:
    for lid,o,e in ex.map(run,jobs): print(lid,o,e,flush=True)
