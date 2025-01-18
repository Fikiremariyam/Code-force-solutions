n,k = map(int,input().split())
array=list(map(int,input().split()))

maxi=0
l,r = 0,1

if n==1:
    print(1)
else:
    while r < n :
        while r < n  and array[r] != array[r-1]:
            r+=1
        
        maxi=max(r-l,maxi)
        l=r
        r+=1
    print(maxi)


