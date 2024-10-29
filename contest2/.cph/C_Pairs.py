n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
lists=[i for i in range(1,n+1)]

from itertools import combinations
for combo in combinations(lists, 2):
    print(combo)
        