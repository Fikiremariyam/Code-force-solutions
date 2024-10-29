for _ in range(int(input())):
    n=int(input())
    array=list(map(int,input().split()))
    array1=sorted(array)
    res='YES'
    for i in range(n):
        if array[i]%2 != array1[i]%2:
            res='NO'
            break
    print(res)