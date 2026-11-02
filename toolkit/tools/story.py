import base64
LOGO=base64.b64encode(open('assets/dongtube_logo.png','rb').read()).decode()
A={1:('폴드','B의 지금 상금 가치 32.8만','콜해서 이기면 41만(+8.2만)<br>지면 3등 20만(−12.8만)','칩으로는 50%면 본전이지만<br>상금으로는 <b>약 61%</b>를 이겨야 본전'),
2:('①번','칩은 BB로 재야 한다','① 40,000 ÷ 400 = <b>100BB</b><br>② 60,000 ÷ 1,000 = 60BB','칩 숫자는 ②가 커도<br><b>①이 훨씬 깊은 대회</b>'),
3:('② 20만 원','바이인 1번 + 리엔트리 3번','5만 × (1 + 3) = <b>20만 원</b>','리엔트리 대회는<br><b>최대 비용까지 예산에</b>'),
4:('② 약 17%','5,000 ÷ 30,000 = 0.167','정시에 앉기만 해도<br>시작 칩 <b>17%</b> 추가','얼리버드는<br><b>가능하면 챙기기</b>'),
5:('② 10~20BB','36,000 ÷ 3,000 = <b>12BB</b>','오픈 or 리스틸 올인 구간','레벨이 한 번만 더 오르면<br><b>10BB 이하</b>로 내려간다'),
6:('올인','8BB 버튼, 앞에서 모두 폴드','A7o는 <b>올인하기 충분한 핸드</b>','둘 다 폴드하면 +2.5BB<br>기다리면 한 바퀴마다 <b>−2.5BB</b>'),
7:('콜','D의 콜 본전 승률 <b>64%</b>','승률 70%면 <b>콜이 이득</b>','같은 승률도 B 자리(본전 74%)면 폴드<br><b>스택마다 본전이 다르다</b>'),
8:('콜','이 콜의 본전 승률 약 <b>51%</b>','승률 60%면 상금 가치<br>17.3만 → <b>17.7만</b>','사다리만 타다<br><b>좋은 스팟을 버리면 손해</b>'),
9:('폴드','X의 지금 시드 확률 96.4%','이겨도 99.6%(+3.2%p)<br>지면 바로 탈락','본전 승률 약 <b>97%</b><br>KK로도 한참 모자란다'),
10:('② 28만 원','최소 상금 20만 + (40만 × 20%)','= <b>28만 원</b>','ICM 기준 28.9만보다 적다<br><b>딜 조율의 근거</b>가 된다')}
for n,(ans,l1,l2,l3) in A.items():
    open(f'story/ans{n:02d}.html','w').write(f'''<!doctype html><html><head><meta charset="utf-8"><style>
*{{box-sizing:border-box;margin:0;padding:0}}body{{width:1080px;height:1920px;font-family:'Noto Sans CJK KR';background:radial-gradient(ellipse at 50% 42%,#17905F 0%,#0F6B4A 55%,#0A4F36 100%);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:46px;padding:0 70px;position:relative}}
body::before{{content:"";position:absolute;inset:30px;border:4px solid rgba(241,234,223,.16);border-radius:48px}}
.t{{color:#E3A934;font-size:52px;font-weight:900;letter-spacing:6px}}.q{{background:#F1EADF;color:#D33B3B;font-size:70px;font-weight:900;padding:8px 28px}}
.a{{font-size:190px;font-weight:900;color:#F1EADF;letter-spacing:-6px;line-height:1.05;text-align:center;text-shadow:0 10px 0 rgba(0,0,0,.2)}}
.c{{width:100%;background:#F1EADF;border-radius:36px;padding:50px;text-align:center;color:#1B2027;box-shadow:0 16px 0 rgba(0,0,0,.2)}}
.c p{{font-size:52px;font-weight:700;line-height:1.5;padding:22px 0;border-top:4px solid #DDD2C0}}.c p:first-child{{border-top:0;padding-top:0}}.c b{{color:#D33B3B}}
.n{{color:#F1EADF;font-size:44px;font-weight:700;opacity:.9}}img{{position:absolute;bottom:80px;width:190px}}</style></head><body>
<div class="t">홀덤 꿀팁 #{n:02d}</div><div class="q">어제 퀴즈 정답</div><div class="a" style="font-size:{190 if len(ans)<=6 else 150}px;white-space:nowrap">{ans}</div>
<div class="c"><p>{l1}</p><p>{l2}</p><p>{l3}</p></div><div class="n">📌 자세한 내용은 게시물에서</div>
<img src="data:image/png;base64,{LOGO}"></body></html>''')
