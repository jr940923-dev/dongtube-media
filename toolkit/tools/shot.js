const {chromium}=require('playwright');const path=require('path');const fs=require('fs');
(async()=>{const f=path.resolve(process.argv[2]);const base=path.basename(f,'.html');
const out=path.join(__dirname,'..','output',base);fs.mkdirSync(out,{recursive:true});
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
await p.goto('file://'+f);await p.waitForTimeout(300);
const s=await p.$$('.s');for(let i=0;i<s.length;i++) await s[i].screenshot({path:`${out}/${base}_${i+1}.png`});
await b.close();console.log(`${s.length}장 → ${out}`)})();
