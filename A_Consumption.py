k= input()
remaining=list(map(int,input().split()))
capacity=list(map(int,input().split()))
capacity.sort()

if sum(remaining) <= capacity[-1]+capacity[-2]:
    print("YES")
else:
    print("NO")

