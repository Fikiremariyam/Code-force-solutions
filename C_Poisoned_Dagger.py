
for _ in range(int(input())):
    n,h=map(int,input().split())
    hits=sorted(list(map(int,input().split())))
    min_capacity=0
    capacity=[]
    for i in range(n-1):
        capacity.append(hits[i+1]-hits[i])
    capacity.sort()

    power=0
    k=1
    l=0
    while power<h:
        power+=n-l
        k+=1
        while k>capacity[l]:
            l+=1
            
