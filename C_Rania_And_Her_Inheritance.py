#abs123
from itertools import product
n,m = map(int, input().split())
vl = sorted([ input() for i in range(n)])
cm = {vl[i]:i for i in range(n)}
cl = []
for i in range(m):
    a,b = input().split()
    cl+=[[cm[a],cm[b]]]
ans=[(),0]
for x in list(product([1,0],repeat=n)):
    flag=0
    for c in cl:
        if x[c[0]]==1==x[c[1]]:
            flag=1
            break;
    
    if flag==0 and ans[1]<x.count(1):
        ans=[x,x.count(1)]
        
print(ans[1])
print('\n'.join([vl[i] for i in range(n) if ans[0][i]==1]))