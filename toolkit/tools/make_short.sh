#!/bin/bash
# usage: make_short.sh 02
cd ~/dongtube
NODE_PATH=$(npm root -g) node tools/motion.js motion/tip$1.html >/dev/null && python3 tools/sfx.py motion/tip$1_events.json motion/tip$1_sfx.wav 25 && \
ffmpeg -y -loglevel error -framerate 30 -i motion/tip$1_frames/%04d.jpg -i motion/tip$1_sfx.wav -c:v libx264 -preset veryfast -crf 19 -pix_fmt yuv420p -c:a aac -b:a 160k -shortest shorts/tip$1_motion.mp4 && tools/add_bgm.sh shorts/tip$1_motion.mp4 shorts/tip$1_bgm.mp4 && rm -rf motion/tip$1_frames && echo done $1
