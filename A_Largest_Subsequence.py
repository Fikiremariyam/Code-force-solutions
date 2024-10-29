for _ in range(int(input())):
    n=int(input())
    string=list(map(str,input().strip()))
    print(string)
    
    times=0
    goal=sorted(string.copy())
    while string != goal and times < n:
        print(string,goal)
        string=cycleit(string)
        times+=1
    if string == goal:
        print( times)
    else:
        print(-1)
