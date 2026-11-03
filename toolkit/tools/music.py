# 밝은 교육용 BGM 합성 (C장조, 100BPM): 플럭 아르페지오 + 마림바 멜로디 + 베이스 + 셰이커 + 소프트 킥
import numpy as np, wave, sys
SR=44100; BPM=100; B=60/BPM; T=float(sys.argv[2]) if len(sys.argv)>2 else 25.0
N=int(T*SR); L=np.zeros(N); R=np.zeros(N)
def f(m): return 440*2**((m-69)/12)
def add(sig,t,pan=0.5,g=1.0):
    i=int(t*SR); j=min(N,i+len(sig))
    if i>=N: return
    L[i:j]+=sig[:j-i]*g*(1-pan); R[i:j]+=sig[:j-i]*g*pan
def pluck(m,dur=0.9):
    n=int(dur*SR); t=np.arange(n)/SR; s=np.zeros(n)
    for k in range(1,8): s+=np.sin(2*np.pi*f(m)*k*t)/k**1.3*np.exp(-t*(3+k*2.2))
    return s*np.minimum(1,t/0.004)
def marimba(m,dur=0.7):
    n=int(dur*SR); t=np.arange(n)/SR
    s=np.sin(2*np.pi*f(m)*t)*np.exp(-t*5)+0.35*np.sin(2*np.pi*f(m)*4*t)*np.exp(-t*18)+0.15*np.sin(2*np.pi*f(m)*10*t)*np.exp(-t*40)
    return s*np.minimum(1,t/0.002)
def bass(m,dur):
    n=int(dur*SR); t=np.arange(n)/SR
    s=(np.sin(2*np.pi*f(m)*t)+0.3*np.sin(2*np.pi*f(m)*2*t))*np.exp(-t*2.2)
    return s*np.minimum(1,t/0.01)*np.minimum(1,(dur-t)/0.05)
def kick():
    n=int(.25*SR); t=np.arange(n)/SR; fr=110*np.exp(-t*25)+48
    return np.sin(2*np.pi*np.cumsum(fr)/SR)*np.exp(-t*14)
rng=np.random.default_rng(3)
def shaker():
    n=int(.08*SR); x=rng.uniform(-1,1,n); x=np.diff(np.concatenate([[0],x]))  # 고역 통과
    return x*np.exp(-np.arange(n)/SR*60)
def pad(ch,dur):
    n=int(dur*SR); t=np.arange(n)/SR; s=np.zeros(n)
    for m in ch: s+=np.sin(2*np.pi*f(m)*t)+0.5*np.sin(2*np.pi*f(m)*2.003*t)
    env=np.minimum(1,t/0.4)*np.minimum(1,(dur-t)/0.4)
    return s*env/len(ch)
# 코드 진행 (마디당 2.4초): C G Am F / C G F G 반복
C=[60,64,67]; G=[55,59,62]; Am=[57,60,64]; F=[53,57,60]
prog=[C,G,Am,F,C,G,F,G,C,G,Am,F]
roots={id(C):36,id(G):43,id(Am):45,id(F):41}
mel=[[76,74,72,74],[74,71,74,79],[72,76,79,76],[77,76,74,72],[76,79,81,79],[79,74,71,74],[72,74,77,76],[74,79,77,74],[76,74,72,74],[74,71,74,79],[72,76,72,69],[72,None,None,None]]
bars=int(np.ceil(T/(4*B)))
for b in range(bars):
    ch=prog[b%len(prog)]; t0=b*4*B
    add(pad([m+12 for m in ch],4*B),t0,0.5,0.08)
    arp=[ch[0],ch[1],ch[2]+0,ch[1],ch[0]+12,ch[1],ch[2],ch[1]]
    for k,m in enumerate(arp): add(pluck(m),t0+k*B/2,0.35 if k%2 else 0.65,0.22)
    if b>=1:
        add(bass(roots[id(ch)],B*1.9),t0,0.5,0.35); add(bass(roots[id(ch)],B*1.9),t0+2*B,0.5,0.3)
        for k in (0,2): add(kick(),t0+k*B,0.5,0.35)
        for k in range(8):
            if k%2: add(shaker(),t0+k*B/2,0.7,0.12)
    if b>=2:
        for k,m in enumerate(mel[b%len(mel)]):
            if m: add(marimba(m),t0+k*B,0.55,0.3)
mix=np.stack([L,R],1)
fade=int(1.5*SR); mix[-fade:]*=np.linspace(1,0,fade)[:,None]
mix[:int(.3*SR)]*=np.linspace(0,1,int(.3*SR))[:,None]
mix/=np.abs(mix).max()+1e-9; mix*=0.9
w=wave.open(sys.argv[1],'w'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix*32767).astype(np.int16).tobytes()); w.close()
