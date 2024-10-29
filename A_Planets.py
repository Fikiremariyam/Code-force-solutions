from collections import Counter
for _ in range(int(input())):
    n,c = map(int,input().split())
    array=list(map(int,input().split()))
    a =Counter(array)
    cost=0
    for item in a:
        cost+=min(c,a[item])
    print(cost)
