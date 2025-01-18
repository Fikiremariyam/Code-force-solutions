import heapq
n,k = map(int,input().split())
array=list(map(int,input().split()))

heap=[]

for i in range(n):    heapq.heappush(heap,(i+1,array[i]))
    
maxitem=0
mincost=float("inf")

for i in range(1,n+1):#number of items
    cost=0
    item=0
    heap1=heap

    while cost<=k and heap1 and item < i:
        cur = heapq.heappop(heap1)
        cost+= cur[0]*i +cur[1]
        item+=1
    print(i,item,cost)
    if item == i  :
        if maxitem<= i  and cost<=mincost:
            maxitem=i
            mincost =cost
print(maxitem,mincost)

