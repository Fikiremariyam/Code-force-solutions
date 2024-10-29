for _ in range(int(input())):
    word=list(map(str,input().strip()))
    a=b=0
    for i in word:
        if i=='A':a+=1
        else:b+=1
    print('A' if a>b else 'B')