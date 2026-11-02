import json,sys,wave,numpy as np
ev=json.load(open(sys.argv[1])); T=float(sys.argv[3]); SR=44100
out=np.zeros(int(T*SR)+SR)
def env(n,a=0.003,d=0.1):
    t=np.arange(n)/SR; return np.minimum(1,t/a)*np.exp(-t/d)
def snd(k):
    if k=='pop':
        n=int(.18*SR);t=np.arange(n)/SR;f=520*np.exp(-t*18)+260;return .5*np.sin(2*np.pi*np.cumsum(f)/SR)*env(n,.002,.05)
    if k=='tick':
        n=int(.06*SR);return .25*np.random.uniform(-1,1,n)*env(n,.001,.008)
    if k=='count':
        n=int(.04*SR);t=np.arange(n)/SR;return .12*np.sin(2*np.pi*1800*t)*env(n,.001,.01)
    if k=='ding':
        n=int(.7*SR);t=np.arange(n)/SR;return .3*(np.sin(2*np.pi*1320*t)+.5*np.sin(2*np.pi*1980*t))*env(n,.002,.18)
    if k=='beep':
        n=int(.15*SR);t=np.arange(n)/SR;return .25*np.sin(2*np.pi*880*t)*env(n,.002,.06)
    if k=='whoosh':
        n=int(.35*SR);x=np.random.uniform(-1,1,n);
        y=np.convolve(x,np.ones(30)/30,'same');t=np.arange(n)/SR;return .5*y*np.sin(np.pi*t/(n/SR))
for k,at in ev:
    s=snd(k);i=int(at*SR);out[i:i+len(s)]+=s
out=np.clip(out[:int(T*SR)],-1,1)
w=wave.open(sys.argv[2],'w');w.setnchannels(1);w.setsampwidth(2);w.setframerate(SR);w.writeframes((out*32767).astype(np.int16).tobytes());w.close()
