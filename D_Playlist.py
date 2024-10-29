import heapq
n,k=map(int,input().split())
musics=[]
heap=[]
final=0
summ=0
for _ in range(n):
    a,b=map(int,input().split())
    musics.append([b,a])
musics.sort(reverse= True)    

for fav,l in musics:
    heapq.heappush(heap,l)
    summ+=l
    while len(heap)>k:
        summ-=heapq.heappop(heap)
    final=max(final,fav*summ)
print(final)