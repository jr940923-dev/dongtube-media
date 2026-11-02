from itertools import permutations
def icm(stacks, prizes):
    n=len(stacks); ev=[0.0]*n
    for perm in permutations(range(n), min(n,len(prizes))):
        p=1.0; rem=sum(stacks)
        for i in perm: p*=stacks[i]/rem; rem-=stacks[i]
        for k,i in enumerate(perm): ev[i]+=p*prizes[k]
    return ev
