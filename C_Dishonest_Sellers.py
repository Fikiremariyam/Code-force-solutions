import heapq
n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

heap=[]
moeny=0

for i in range(n):
    heapq.heappush(heap,(a[i]-b[i],i))
for _ in range(k):
    froma=heapq.heappop(heap)[1]
    moeny+=a[froma]
while heap and  heap[0][0]<=0:
    froma=heapq.heappop(heap)[1]
    moeny+=a[froma]
while heap :
    fromb=heapq.heappop(heap)[1]
    moeny+=b[fromb]
print(moeny)
#@@
