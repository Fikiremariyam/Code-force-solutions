def check(array):
    for i in range(0,len(array)-1):
        if (abs(array[i]-array[i+1]))>1:
            return False
    return True

for _ in range(int(input())):
    leng=input()
    a=list(map(int,input().split()))
    if check(sorted(a)):print('YES')
    else: print('NO')
