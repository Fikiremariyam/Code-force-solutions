"""
FIKER @A2sv
"""
for i in range(int(input())):
    leng=int(input())
    nums=list(map(int,input().split()))
    nums_S=sorted(nums)
    res=0
    for i in range(leng):
        if nums[i]%2 != nums_S[i]%2:
            res+=1
            
    print(res//2)
    