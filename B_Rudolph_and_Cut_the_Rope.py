for _ in range(int(input())):
    n=int(input())
    ans=0
    for _ in range(n):
        a,b=map(int,input().split())
        if a-b >0: ans+=1
    print(ans)