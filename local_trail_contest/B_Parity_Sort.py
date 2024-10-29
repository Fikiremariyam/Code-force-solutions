"""
FIKER @A2sv
"""
for i in range(int(input())):
    leng=int(input())
    nums=list(map(int,input().split()))
    nums_S=sorted(nums)
    res="YES"
    
    for i in range(leng):
        if nums[i]%2 != nums_S[i]%2:
            res="NO"
            break
    print(res)
    