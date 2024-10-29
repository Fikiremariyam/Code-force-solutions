for _ in range(int(input())):
    n,m=map(int,input().split())
    array1=list(map(int,input().split()))
    array2=list(map(int,input().split()))
    array1.sort(reverse=True)
    array2.sort()
    i,l=0,0
    j=n-1
    r=m-1
    maxi=0
    while i<=j :
        a=abs(array1[i]-array2[l])
        b=abs(array1[j]-array2[r])
        if a>b:
            maxi+=a
            i+=1
            l+=1
        else:
            maxi+=b
            j-=1
            r-=1
    print(maxi)

