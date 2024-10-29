for _ in range(int(input())):
    n=int(input())
    nums=list(map(int, input().split()))
    i=0
    j=1
    final=nums[0]

    while j<n:
        if nums[j]*nums[i]>0:
            final-=nums[j-1]
            maxi=nums[j-1]
            while j<n and nums[j]*nums[i]>0 :
                maxi=max(maxi,nums[j])
                j+=1
            final+=maxi
            
            
        else:
            i=j
            final+=nums[j]
            j+=1
    print(final)