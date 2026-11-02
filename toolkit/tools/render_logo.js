const {chromium}=require('playwright');const path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1000,height:1000}});
await p.goto('file://'+path.resolve('assets/logo.svg'));
await p.screenshot({path:'assets/dongtube_logo.png',omitBackground:true});await b.close();})();
