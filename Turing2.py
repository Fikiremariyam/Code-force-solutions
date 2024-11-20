''''

Given woods where woods[i] the length of the ith 
plank, you want to have a fence of maximum lenght
 with maximum number of planks. you only use only
same size planks but you can merge two planks to 
make another one and use it with other planks that has 
this length. answer should be the maximum number planks used 
for each test case'''

from collections import Counter

def blend(planks,target):
    left=0
    right=len(planks)-1
    result =0

    while left < right:
        s= planks[left]+planks[right]
        
        if s== target :
            result +=1
            left+=1
            right-=1
        elif s < target :
            left+=1
        else:
            right-=1
    return result


def solve(planks):

    planks=sorted(planks)
    freq=Counter(planks)
    
    for key in freq:
        freq[key] += blend(planks,key)
    
    res1=max(freq.values())

    freq=Counter()

    for i in range(len(planks)):
        for j in range(len(planks)):
            freq[planks[i]+planks[j]]=0

    for key in freq :
        freq[key]+=blend(planks,key)

    return (max(res1,max(freq.values())))


print(solve([22, 12, 13, 22, 22, 22, 14, 22, 17, 22]))
print(solve([8, 13, 7, 13, 5, 13, 4, 13, 6, 13]))