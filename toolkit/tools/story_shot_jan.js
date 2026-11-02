const {chromium}=require('playwright');const path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
for(const n of [15,16,17,18,19,20]){const f=String(n).padStart(2,'0');await p.goto('file://'+path.resolve(`story/ans${f}.html`));await p.waitForTimeout(150);await p.screenshot({path:`story/ans${f}.jpg`,type:'jpeg',quality:92});}
await b.close();})();
