# code force 792
for _ in range(int(input())):
    n,k= map(int ,input().split())
    a=list(map(int,input().split()))
#we want 5th lagerst distance from some point x
 #but we dont know x -> it is in the enteval of [l,r]....the worst case senrio [ a[i],a[n] ] ,best case scnrio [a[i], a[i+k]]
 #instead of checking for every x in the intervl lets find the minimum distance betwwwn two points and take the middle of them 

    ans = float("inf")
    final = -1
    for i in range(n - k):      # lets traverse while keeping the the interval a[i] , a[i+k]

        dist = a[i + k] - a[i]
        if dist < ans: # by finding the minimum of the two distance then it makes kth distance minium
            ans=dist
            final=a[i] + dist // 2

    print(final)

"""
lets get it in example 
k = 3 for both 

a =1, 2,3,4,5,7,13,14,15
b=2,44,55,66,77,67,89,95,96

we want 5th lagerst distance from some point x
 but we dont know x -> it is in the enteval of [l,r]....the worst case senrio [ a[i],a[n] ] ,best case scnrio [a[i], a[i+k]]
 instead of checking for every x in the intervl lets find the minimum distance betwwwn two points and take the middle of them 
 
 lets traverse while keeping the the interval a[i] , a[i+k]

 by finding the minimum of the two distance then it makes kth distance minium



"""