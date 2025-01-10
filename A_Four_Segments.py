for _ in range(int(input())):
    sides=list(map(int,input().split()))
    sides.sort()
    side1=min(sides[0],sides[1])
    side2=min(sides[2],sides[3])
    print(side1*side2)