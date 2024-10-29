for _ in range(int(input())):
    n,m=map(int,input().split())
    ind=[0 for _ in range(n)]
    for i in range(m):
        a,b=map(int,input().split())
        ind[a-1]+=1
        ind[b-1]+=1
        
    count=0
    for i in range(n):
        if(ind[i]==1):
            count+=1
    x=m-count
    y=count//x
    print(x,y)