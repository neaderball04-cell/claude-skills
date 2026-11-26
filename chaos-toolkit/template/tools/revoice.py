"""Swap narrator lines for converted voice, rebuild voice tracks and full soundtrack."""
import json,subprocess,re,os,soundfile as sf
os.chdir('/home/claude/t2c2/video')
run=lambda a:subprocess.run(a,check=True,capture_output=True)
T=json.load(open('work/timing.json'))
SHARP=("aresample=48000,highpass=f=80,equalizer=f=300:t=q:w=1:g=-3,equalizer=f=3000:t=q:w=1.2:g=4,"
       "aexciter=amount=3:drive=8.5:blend=0:freq=3500:ceil=12000,treble=g=4:f=6000,"
       "acompressor=threshold=-20dB:ratio=3:makeup=2,loudnorm=I=-16:TP=-2:LRA=7,aresample=48000")
for sid,sc in T.items():
    if not isinstance(sc,dict):continue
    inputs=[];fc=[]
    for i,(lid,l) in enumerate(sc['lines'].items()):
        src=f'work/cl_bak/cl_{lid}.wav' if l['voice']=='n' else f'work/cl_{lid}.wav'
        if l['voice']=='n':
            d=sf.info(src).duration
            run(['ffmpeg','-y','-v','error','-i',f'/home/claude/voice/conv/cl_{lid}.wav','-af',SHARP+f',apad=whole_dur={d:.4f}','-t',f'{d:.4f}','-ac','2',f'work/cl_{lid}.wav'])
            src=f'work/cl_{lid}.wav'
        inputs+=['-i',src];fc.append(f"[{i}:a]adelay={int(l['start']*1000)}:all=1[a{i}]")
    n=len(inputs)//2
    fcs=';'.join(fc)+';'+''.join(f'[a{i}]' for i in range(n))+f"amix=inputs={n}:duration=longest:normalize=0,apad=whole_dur={sc['dur']}[out]"
    run(['ffmpeg','-y','-v','error']+inputs+['-filter_complex',fcs,'-map','[out]','-t',str(sc['dur']),'-ar','48000','-ac','2',f'assets/voice/{sid}.wav'])
    print(sid,flush=True)
# full soundtrack from index.html audio clips
h=open('index.html').read()
clips=re.findall(r'<audio[^>]*src="([^"]+)"[^>]*data-start="([\d.]+)"[^>]*data-duration="([\d.]+)"[^>]*data-volume="([\d.]+)"',h)
ins=[];fc=[]
for i,(src,st,du,vol) in enumerate(clips):
    ins+=['-i',src];fc.append(f"[{i}:a]atrim=0:{du},aresample=48000,aformat=channel_layouts=stereo,volume={vol},adelay={int(float(st)*1000)}:all=1[c{i}]")
fcs=';'.join(fc)+';'+''.join(f'[c{i}]' for i in range(len(clips)))+f"amix=inputs={len(clips)}:duration=longest:normalize=0[out]"
run(['ffmpeg','-y','-v','error']+ins+['-filter_complex',fcs,'-map','[out]','-t',str(T['_total']),'-ar','48000','-ac','2','work/soundtrack.wav'])
print('soundtrack',len(clips),'clips')
