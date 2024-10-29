for _ in range(int(input())):
    n,a,b=map(int,input().split())
    #using a
    cost1=n*a
    #using b
    cost2=n//2*b+n%2*a
    print(min(cost1,cost2))