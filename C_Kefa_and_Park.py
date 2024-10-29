n,m=map(int,input().split())

cat=list(map(int,input().split()))

d = {i:[] for i in range(1,n+1)}#our graph of direction 

for i in range(n-1):
    a,b=map(int,input().split())
    d[a].append(b)
    d[b].append(a)
#current,cats on the way ,ansector
    
q=[[1,0,0]]
ans=0

while q:
    k,c,parent= q.pop()

    c=cat[k-1]*(c+1) #multiply the 

    if c>m:# if we have collected the amount of the cats he can bear 
        continue

    if len(d[k])==1 and k!=1:# we have reached the node which have one nebhiour and it is not the first node
        ans+=1
        continue

    for i in d[k]:
        if i!=parent:# to prevent loop bbeacouse a->b and a<-a in our graoh formation 
            q.append([i,c,k])
print(ans)
 