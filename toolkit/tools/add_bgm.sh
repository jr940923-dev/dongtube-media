#!/bin/bash
# usage: add_bgm.sh in.mp4 out.mp4  (효과음 위에 BGM을 깔아 다시 저장, 영상은 재인코딩 없음)
BGM=${BGM:-$HOME/dongtube/assets/bgm_edu.wav}; VOL=${VOL:-0.32}
ffmpeg -y -loglevel error -i "$1" -i "$BGM" -filter_complex "[1:a]volume=${VOL}[b];[0:a][b]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k "$2"
