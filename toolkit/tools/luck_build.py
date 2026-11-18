# 주간 홀덤 금전운: 쇼츠 HTML + 스토리 HTML 생성
import re,sys,json
import os
SRC=open(os.path.expanduser('~/dongtube/motion/tip01.html')).read()
D=json.load(open(sys.argv[1]))
OUT=os.path.splitext(sys.argv[1])[0]
HEAD=SRC.split('</style>')[0]
LOGO=re.search(r'<img[^>]*class="logo"[^>]*>',SRC) or re.search(r'<img[^>]*src="data:image[^>]*>',SRC)
LOGO=LOGO.group(0)
WEEK=D['week']
Z=[tuple(z) for z in D['zodiac']]  # [띠, 한자, 별1~5, 행운의 핸드, 한마디]
def hand(h):
    return ' '.join(f'<span class="{"rd" if s in "♥♦" else ""}">{c}{s}</span>' for c,s in (x[:-1].replace('T','10') and (x[:-1].replace('T','10'),x[-1]) for x in h.split()))
def stars(n): return '<span class="st">'+'★'*n+'<i>'+'★'*(5-n)+'</i></span>'
CSS='''
.zc{width:100%;background:var(--cream);border-radius:30px;padding:26px 34px;box-shadow:0 12px 0 rgba(0,0,0,.2);display:flex;flex-direction:column;gap:10px}
.zt{display:flex;align-items:center;gap:22px;font-size:62px;font-weight:900;color:var(--ink);letter-spacing:-2px}
.zt .hz{flex:0 0 92px;height:92px;border-radius:50%;background:var(--red);color:var(--cream);display:flex;align-items:center;justify-content:center;font-size:54px}
.zt .nm{flex:1}
.st{color:var(--gold);font-size:56px;letter-spacing:2px}.st i{font-style:normal;color:#D8CDBB}
.zl{display:flex;justify-content:space-between;align-items:center;font-size:44px;font-weight:700;color:var(--sub)}
.zl b{color:var(--ink);font-size:50px;font-weight:900;letter-spacing:1px}.rd{color:var(--red)}
.zm{font-size:46px;font-weight:700;color:var(--ink);letter-spacing:-1px}
.disc{font-size:38px;color:rgba(241,234,223,.75);text-align:center;line-height:1.5}
'''
def zcard(z,at):
    n,hz,s,h,m=z
    return (f'<div class="zc" data-in="{at}" data-a="left"><div class="zt"><div class="hz">{hz}</div><div class="nm">{n}띠</div>{stars(s)}</div>'
            f'<div class="zl">행운의 핸드 <b>{hand(h)}</b></div><div class="zm">{m}</div></div>')
SC=[0,2.6,7.0,11.4,15.8,20.2,25]
best=[z for z in Z if z[2]==5]
body=f'''<div class="top">홀덤 금전운 · {WEEK["no"]}</div><div class="prog"><i id="pb"></i></div>
<div class="sc" data-s="0" data-e="2.6"><div class="big" data-in="0.05" data-a="pop">이번 주</div><div class="big" data-in="0.6" data-a="pop"><b>홀덤 금전운</b></div><div class="hl r" data-in="1.3" data-a="up">{WEEK["rng"]} · 띠별 확인</div></div>
'''
for i in range(4):
    grp=Z[i*3:i*3+3]
    body+=f'<div class="sc" data-s="{SC[i+1]}" data-e="{SC[i+2]}" style="gap:30px">'+''.join(zcard(z,0.1+k*0.35) for k,z in enumerate(grp))+'</div>\n'
body+=(f'<div class="sc" data-s="20.2" data-e="25" style="gap:36px"><div class="hl" data-in="0.05" data-a="left">이번 주 최고 운</div>'
       f'<div class="big" style="font-size:120px" data-in="0.4" data-a="pop"><b>{" · ".join(z[0]+"띠" for z in best)}</b></div>'
       f'<div class="note" data-in="1.2" data-a="up">매주 월요일 업데이트<br><b>저장</b>해두고 대회 전에 보기</div>'
       f'<div class="disc" data-in="2.0" data-a="up">재미로 보는 운세예요 · 바이인은 감당할 수 있는 만큼</div></div>\n')
JS=SRC[SRC.index('<script>'):SRC.index('</script>')+9]
JS=re.sub(r"\n const q=t-20\.2.*?\n","\n",JS)
JS=re.sub(r"\n for\(let k=0;k<3;k\+\+\)ev\.push\(\['beep'.*?;return ev\}","return ev}",JS)
open(OUT+'.html','w').write(HEAD+CSS+'</style></head><body>\n'+body+LOGO+'\n'+JS+'</body></html>')
# 스토리 (1080x1920)
rows=''.join(f'<div class="r"><div class="hz">{z[1]}</div><div class="nm">{z[0]}</div>{stars(z[2])}<b>{hand(z[3])}</b></div>' for z in Z)
story=HEAD+CSS+'''
.st{font-size:46px}.sw{position:absolute;inset:110px 70px 330px;display:flex;flex-direction:column;gap:22px}
.sh{text-align:center;color:var(--cream);font-size:86px;font-weight:900;letter-spacing:-3px}.sh b{color:var(--gold)}
.ss{text-align:center;color:var(--cream);font-size:42px;font-weight:700;opacity:.85;margin-bottom:10px}
.tb{background:var(--cream);border-radius:34px;padding:16px 34px;box-shadow:0 14px 0 rgba(0,0,0,.2)}
.r{display:flex;align-items:center;gap:20px;padding:9px 0;border-top:3px solid var(--line);font-size:50px;font-weight:900;color:var(--ink)}
.r:first-child{border-top:0}.r .hz{flex:0 0 70px;height:70px;border-radius:50%;background:var(--red);color:var(--cream);display:flex;align-items:center;justify-content:center;font-size:40px}
.r .nm{flex:0 0 170px}.r b{flex:1;text-align:right;font-size:44px;letter-spacing:1px}
</style></head><body><div class="sw"><div class="sh">이번 주 <b>홀덤 금전운</b></div><div class="ss">'''+WEEK['rng']+''' · 별점 · 행운의 핸드</div><div class="tb">'''+rows+'''</div>
<div class="disc">재미로 보는 운세예요 · 바이인은 감당할 수 있는 만큼</div></div>'''+LOGO+'</body></html>'
open(OUT+'_story.html','w').write(story)
print('ok')
