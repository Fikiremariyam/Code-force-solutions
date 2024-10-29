def winner(n,nazi):
    
    while nazi[0]<=n:
        thisround =0
        for i in nazi:
            if  i <= n:
                thisround+=1
            else: break
        n-= thisround
        
    return n
for _ in range(int(input())):
    query,amount=map(int,input().split())
    nazis=list(map(int,input().split()))
    amounts=list(map(int,input().split()))
    final=[]
    for i in amounts:
        final.append(winner(i,nazis))
    print(" ".join(map(str,final)))

