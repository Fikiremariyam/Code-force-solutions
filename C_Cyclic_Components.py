n,m = map(int,input().split())
edges = [[] for i in range(n+1)]
 
for i in range(m):#creating bi directional graph 
    x,y = map(int, input().split())
    edges[y].append(x)
    edges[x].append(y)
 
s = set(i for i in range(n+1) if len(edges[i])==2) #only a cycle if it consists  2 edges it is a cycle
cycles = 0
 
while s:
    v = s.pop()
    r,l = edges[v]
    while l in s:# we take l beacouse we want to have go through one direction
        s.remove(l)
        v1,v2 = edges[l]
        
        if v1 in s:
            l = v1
        elif v2 in s:
            l = v2
        else:
            break
        
        if l == r:
            cycles+=1
 
print(cycles)