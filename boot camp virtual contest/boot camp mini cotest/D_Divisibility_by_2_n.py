def potential(n):# a function to calculate the number of 2s in a number
    count=0
    while n%2==0:
        n=n//2
        count+=1
    return count

for _ in range(int(input())):
    n=int(input())
    nums=list(map(int,input().split()))
    #first check if product of all numbers is divisible by 2^n
    
    count=0
    for i in nums:
        count+=potential(i)
    if count>=n:#if so we are done
        print(0)
        continue

    index_potential=[0]*n       #a list to store the number of 2s in each index from 1 to n
    for i in range(n):
        index_potential[i]+=potential(i+1) 

    index_potential.sort(reverse=True)
    res=0
    for i in range(n):
        count += index_potential[i]
        res+=1
        if count >=n:
            print(res)
            break
    if count<n:
        print(-1)



"""
for _ in range(int(input())):

    n=int(input())
    nums=list(map(int,input().split()))
    product=1

    product2=1

    for i in range(n):
        product*= (i+1)*nums[i]
        product2*= nums[i]
    toN=2**n

    if product2%toN==0:
        print(0)
        continue
   
    final=n

    if product%toN!=0:#the most we can multiply and it is not multiple of 2^n
        print(-1)
    else:
        for i in range(n,0,-1):
            if (product//(i))%toN==0:

                product = product//i
                final-=1
        print(final)

"""	