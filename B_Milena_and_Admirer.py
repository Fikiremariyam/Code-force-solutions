for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    last=a[-1]

    totaltimes=0
    for  i in range(n-2,-1,-1):
        if a[i]>last:
            times=a[i]//last

            if a[i]%last:
                times+=1
            
            last=a[i]//times
            totaltimes+=times-1
        else:
            last=a[i]
    print(totaltimes)

