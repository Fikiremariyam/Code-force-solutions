
n=int(input())
road={ i:[] for i in range(1,n+1)}
for i in range(n):
    input1=list(map(int,input().split()))

    for j in range(n):
        if input1[j]==1:
            road[i+1].append(j+1)

for i in road:
    print(len(road[i]),end=" ")
    print(*road[i])
