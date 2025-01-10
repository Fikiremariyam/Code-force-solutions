sets,pow = map(int,input().split())

array=list(map(int,input().split()))

import heapq
carry=[]

for i in range(sets):
    if -1*array[i] >0:
        heapq.heappush(carry,-1*array[i])
    while len(carry) > pow:
        heapq.heappop(carry)
print(sum(carry))