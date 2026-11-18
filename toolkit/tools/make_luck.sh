#!/bin/bash
# usage: make_luck.sh 49   (luck/w49.json → shorts/luck_w49.mp4 + story/luck_w49.jpg)
cd ~/dongtube && W=w$1 && python3 tools/luck_build.py luck/$W.json && \
NODE_PATH=$(npm root -g) node tools/motion.js luck/$W.html >/dev/null && python3 tools/sfx.py luck/${W}_events.json luck/${W}_sfx.wav 25 && \
ffmpeg -y -loglevel error -framerate 30 -i luck/${W}_frames/%04d.jpg -i luck/${W}_sfx.wav -c:v libx264 -preset veryfast -crf 19 -pix_fmt yuv420p -c:a aac -b:a 160k -shortest luck/${W}_motion.mp4 && \
tools/add_bgm.sh luck/${W}_motion.mp4 shorts/luck_${W}.mp4 && rm -rf luck/${W}_frames && \
NODE_PATH=$(npm root -g) node -e "const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});await p.goto('file://'+process.env.HOME+'/dongtube/luck/${W}_story.html');await p.waitForTimeout(300);await p.screenshot({path:process.env.HOME+'/dongtube/story/luck_${W}.jpg',type:'jpeg',quality:92});await b.close()})()" && echo done $W
