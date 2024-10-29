for _ in range(int(input())):
    n=int(input())
    array=list(map(int, input().split()))
    l=-1
    r=n
    left=0
    right=0

    candy=0
    maxcandy=0

    while l+1<r-1:

        if left+array[l+1]<right+array[r-1]:
            left+=array[l+1]
            l+=1
        elif left+array[l+1]>right+array[r-1]:
            right+=array[r-1]
            r-=1
        else:#if they are equal we add form both end
            candy+=1
            left+=array[l+1]
            l+=1
            right+=array[r-1]
            r-=1
        candy+=1
        
        if left ==right:
            maxcandy=max(maxcandy,candy)
            

    
    print(maxcandy)    