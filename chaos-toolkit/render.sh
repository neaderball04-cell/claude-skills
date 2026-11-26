#!/bin/bash
# usage: render.sh <key> <FILE>   (env: CHAOS_WORK, CHAOS_OUT)
W=${CHAOS_WORK:-/home/claude/cls}; O=${CHAOS_OUT:-/home/claude/out}
K=$1; F=$2; D=$W/$K/video
cd $D && mkdir -p renders && rm -f renders/c_*.mp4
TOT=$(python3 -c "import json;t=json.load(open('work/timing.json'));print(t['total'] if 'total' in t else max(v['start']+v['dur'] for v in t.values() if isinstance(v,dict) and 'dur' in v))")
Q=$(python3 -c "print(round($TOT/4,2))")
for i in 0 1 2 3; do S=$(python3 -c "print(round($i*$Q,2))"); E=$(python3 -c "print(round(min(($i+1)*$Q,$TOT),2))"); npx -y hyperframes@0.9.58 render --start $S --end $E --crf 27 -o renders/c_$i.mp4 --quiet > renders/log_$i.txt 2>&1 & done; wait
printf "file c_0.mp4\nfile c_1.mp4\nfile c_2.mp4\nfile c_3.mp4\n" > renders/l.txt
mkdir -p $O && cd renders && ffmpeg -y -v error -f concat -safe 0 -i l.txt -c copy $O/CHAOS_${F}_Class.mp4 && echo "DONE $K $(ffprobe -v error -show_entries format=duration -of csv=p=0 $O/CHAOS_${F}_Class.mp4)" >> $W/render.log
