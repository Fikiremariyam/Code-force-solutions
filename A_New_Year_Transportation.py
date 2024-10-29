a,b=map(int,input().split())
road=list(map(int,input().split()))
i=1
final='NO'
while i <a:
    
    i+=road[i-1]
    if i==b:
        final='YES'
        break
    
print(final)
