import json, subprocess, os
os.chdir('/home/claude/t2c2/video')
S=json.load(open('tools/script.json'))
def run(args):
    r=subprocess.run(args,capture_output=True,text=True)
    if r.returncode: raise SystemExit(r.stderr[-1500:])
    return r
def dur(p):
    return float(run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p]).stdout.strip())
TRIM="silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.03,areverse,silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.06,areverse"
timing={}
t_global=0.0
for sc in S['scenes']:
    sid=sc['id']; t=sc['lead']; inputs=[]; fc=[]; lines={}
    for i,(lid,v,text,gap) in enumerate(sc['lines']):
        raw=f'work/raw_{lid}.wav'; clean=f'work/cl_{lid}.wav'
        if v in ('n','l','m','c','f','v'):
            run(['ffmpeg','-y','-v','error','-i',raw,'-af',TRIM+',loudnorm=I=-16:TP=-2:LRA=7,aresample=48000','-ac','2',clean])
        else:
            tmp=f'work/tr_{lid}.wav'
            run(['ffmpeg','-y','-v','error','-i',raw,'-af',TRIM+',aresample=48000',tmp])
            d=dur(tmp)
            run(['ffmpeg','-y','-v','error','-i',tmp,
                 '-f','lavfi','-t',f'{d+0.30:.3f}','-i','anoisesrc=c=pink:r=48000:a=0.06:seed=7',
                 '-f','lavfi','-t','0.10','-i','anoisesrc=c=white:r=48000:a=0.5:seed=11',
                 '-filter_complex',
                 f"[0:a]highpass=f=450,lowpass=f=2800,acrusher=bits=9:mode=log:mix=0.35,acompressor=threshold=-22dB:ratio=8:attack=5:release=60:makeup=5,adelay=120:all=1[v];"
                 f"[1:a]highpass=f=700,lowpass=f=3000[nz];"
                 f"[2:a]highpass=f=900,lowpass=f=3200,afade=t=out:st=0.02:d=0.08,adelay={int((d+0.14)*1000)}:all=1[sq];"
                 f"[v][nz][sq]amix=inputs=3:duration=longest:normalize=0,loudnorm=I=-17:TP=-2:LRA=7,aresample=48000[out]",
                 '-map','[out]','-ac','2',clean])
        d=dur(clean)
        t+=gap
        lines[lid]={'start':round(t,3),'end':round(t+d,3),'voice':v,'text':text}
        inputs+=['-i',clean]; fc.append(f"[{i}:a]adelay={int(t*1000)}:all=1[a{i}]")
        t+=d
    total=round(t+sc['tail'],2)
    n=len(sc['lines'])
    fcs=';'.join(fc)+';'+''.join(f'[a{i}]' for i in range(n))+f"amix=inputs={n}:duration=longest:normalize=0,apad=whole_dur={total}[out]"
    run(['ffmpeg','-y','-v','error']+inputs+['-filter_complex',fcs,'-map','[out]','-t',str(total),'-ar','48000','-ac','2',f'assets/voice/{sid}.wav'])
    timing[sid]={'start':round(t_global,2),'dur':total,'lines':lines}
    t_global+=total
timing['_total']=round(t_global,2)
json.dump(timing,open('work/timing.json','w'),indent=1)
for k,v in timing.items():
    if k[0]=='s': print(k,v['start'],v['dur'],{a:(b['start'],b['end']) for a,b in v['lines'].items()})
print('TOTAL',timing['_total'])
