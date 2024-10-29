import heapq
 
n = int(input())
array = list(map(int,input().split()))
 
health = 0
heap = []
final = 0
for i in array:
    heapq.heappush(heap,i)
    health += i
    final += 1
    if health < 0:
        health -= heapq.heappop(heap)
        final -= 1
print(final) #