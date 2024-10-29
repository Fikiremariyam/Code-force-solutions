for _ in range(int(input())):
    ropes=0
    for _ in range(int(input())):
        pos,rope=map(int,input().split())
        if pos>rope:
            ropes+=1
    print(ropes)
