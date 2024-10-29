n, m = map(int, input().split())
degree = [0] * (n+1)
for i in range(m):
    u, v = map(int, input().split())
    
    degree[u] += 1
    degree[v] += 1
 
c1 = degree.count(1)
c2 = degree.count(2)
if c2 == n:
    print("ring topology")
elif c1 == 2 and c2 == n-2:
    print("bus topology")
elif c1 == n - 1:
    print("star topology")
else:
    print("unknown topology")