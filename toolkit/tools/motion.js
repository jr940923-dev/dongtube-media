const {chromium}=require('playwright');const path=require('path');const fs=require('fs');
(async()=>{const f=path.resolve(process.argv[2]);const fps=30;const out=f.replace('.html','_frames');fs.mkdirSync(out,{recursive:true});
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+f);await p.waitForTimeout(300);
const total=await p.evaluate(()=>TOTAL);fs.writeFileSync(f.replace('.html','_events.json'),JSON.stringify(await p.evaluate(()=>events())));
for(let i=0;i<total*fps;i++){await p.evaluate(t=>render(t),i/fps);await p.screenshot({path:`${out}/${String(i).padStart(4,'0')}.jpg`,type:'jpeg',quality:92});}
await b.close();console.log('frames',total*fps)})();
