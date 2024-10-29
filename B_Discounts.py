N=input()
bars=list(map(int,input().split()))
bars.sort(reverse=True)
summ=sum(bars)
k=int(input())
coins=list(map(int,input().split()))

for items in coins:
    print(summ-bars[items-1])
    
