for _ in range(int(input())):
    n=int(input())
    array=list(map(int,input().split()))
    power=0
    stack=[]
    for i in array:
        if not i and stack:
            stack.sort()
            power+=stack.pop()
        else:
            stack.append(i)
    print(power)