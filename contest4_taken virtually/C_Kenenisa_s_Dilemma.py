n=int(input())
a=list(map(int,input().split()))
swaps=[]
for i in range(n):
    mini=i
    for j in range(i+1,n):
        if a[j]<a[mini]:
            mini=j
    if mini!=i:
        a[i],a[mini]=a[mini],a[i]
        swaps.append([i,mini])
if len(swaps)>0:
    print(len(swaps))
    for i in swaps:
        print(i[0],i[1])
else:
    print(0)

