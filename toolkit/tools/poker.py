import random, itertools
from collections import Counter
R='23456789TJQKA'
def rank5(cs):
    v=sorted([R.index(c[0]) for c in cs],reverse=True); s=[c[1] for c in cs]
    fl=len(set(s))==1; u=sorted(set(v),reverse=True)
    st=None
    if len(u)==5 and u[0]-u[4]==4: st=u[0]
    if u==[12,3,2,1,0]: st=3
    cnt=Counter(v); grp=sorted(cnt.items(),key=lambda x:(-x[1],-x[0])); shape=[g[1] for g in grp]; ks=[g[0] for g in grp]
    if st is not None and fl: return (8,st)
    if shape==[4,1]: return (7,*ks)
    if shape==[3,2]: return (6,*ks)
    if fl: return (5,*v)
    if st is not None: return (4,st)
    if shape==[3,1,1]: return (3,*ks)
    if shape==[2,2,1]: return (2,*ks)
    if shape==[2,1,1,1]: return (1,*ks)
    return (0,*v)
def best(cs): return max(rank5(c) for c in itertools.combinations(cs,5))
DECK=[r+s for r in R for s in 'shdc']
def equity(hands,board=(),n=20000,seed=7):
    random.seed(seed); used=set(sum(hands,[]))|set(board); d=[c for c in DECK if c not in used]; win=[0.0]*len(hands)
    for _ in range(n):
        b=list(board)+random.sample(d,5-len(board)); sc=[best(h+b) for h in hands]; m=max(sc); ws=[i for i,x in enumerate(sc) if x==m]
        for i in ws: win[i]+=1/len(ws)
    return [round(w/n*100,1) for w in win]
