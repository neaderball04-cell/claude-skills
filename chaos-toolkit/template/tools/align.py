"""Split the ElevenLabs narration MP3 into per-paragraph raw_n*.wav using long pauses."""
import sys,subprocess,re,json,soundfile as sf,numpy as np
src=sys.argv[1];W='/home/claude/t2c2/video/work'
subprocess.run(['ffmpeg','-y','-v','error','-i',src,'-ac','1','-ar','24000',f'{W}/eleven.wav'],check=True)
x,sr=sf.read(f'{W}/eleven.wav');D=len(x)/sr
o=subprocess.run(['ffmpeg','-i',f'{W}/eleven.wav','-af','silencedetect=noise=-38dB:d=0.25','-f','null','-'],capture_output=True,text=True).stderr
st=[float(v) for v in re.findall(r'silence_start: ([\d.]+)',o)];en=[float(v) for v in re.findall(r'silence_end: ([\d.]+)',o)]
gaps=[(a,b) for a,b in zip(st,en)]
paras=[p.strip() for p in open('/home/claude/csp/script.txt').read().split('\n\n') if p.strip()]
L=np.cumsum([len(p) for p in paras]);exp=L[:-1]/L[-1]*D
cuts=[];used=set()
for e in exp:
    cand=sorted([g for g in gaps if g not in used],key=lambda g:abs((g[0]+g[1])/2-e)-0.8*(g[1]-g[0]))
    g=cand[0];used.add(g);cuts.append(g)
cuts.sort()
bounds=[0]+[ (a+b)/2 for a,b in cuts]+[D]
print('duration',round(D,2),'cuts',[round(c,2) for c in bounds])
for i in range(len(paras)):
    a,b=bounds[i],bounds[i+1];seg=x[int(a*sr):int(b*sr)]
    sf.write(f'{W}/raw_n{i+1}.wav',(seg*32767).astype(np.int16),sr,subtype='PCM_16')
