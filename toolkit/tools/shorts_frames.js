const {chromium}=require('playwright');const path=require('path');const fs=require('fs');
const [tip,title]=[process.argv[2],process.argv[3]];
(async()=>{const out=path.resolve(`shorts/${tip}`);fs.mkdirSync(out,{recursive:true});
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
for(let i=1;i<=6;i++){
 const img='data:image/png;base64,'+fs.readFileSync(path.resolve(`output/${tip}/${tip}_${i}.png`)).toString('base64');
 await p.setContent(`<html><body style="margin:0;width:1080px;height:1920px;font-family:'Noto Sans CJK KR';background:radial-gradient(ellipse at 50% 45%,#17905F 0%,#0F6B4A 55%,#0A4F36 100%);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:40px">
 <div style="color:#E3A934;font-size:54px;font-weight:900;letter-spacing:-1px">${title}</div>
 <img src="${img}" style="width:1080px;height:1350px;display:block">
 <div style="color:#F1EADF;font-size:44px;font-weight:700;opacity:.9">📌 저장해두고 다시 보기 · 정답은 고정 댓글</div></body></html>`);
 await p.waitForTimeout(150);await p.screenshot({path:`${out}/f${i}.png`});}
await b.close();})();
