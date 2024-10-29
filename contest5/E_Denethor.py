for _ in range(int(input())):
    n=int(input())
    array1=list(map(int,input().split()))
    array2=list(map(int,input().split()))
    sum=0
    pointer=n-1
    for i in range(n-1,-1,-1):
      
        if array1[i]!=array2[pointer]:
            sum+=1
        else:
            pointer-=1
    print(sum)

