#brute force
# but it hits tla on test 4
""""
for _ in range(int(input())):
    n=int(input())
    array=list(map(int,input().split()))
    # l********
    l=0
    final=0
    while l<n:
        for r in range(l,n):
            index=r+1-l
            if  array[r]>=index:
                final+=1
            else:
                break
        l+=1
    print(final)
"""
for _ in range(int(input())):
    n=int(input())
    array=list(map(int,input().split()))
    l=0
    r=0
    z=1
    final=0
    while r<n:
        while l<n and z>array[r]:
            l+=1
            z-=1

        final+=r+1-l
        r+=1
        z+=1
    print(final)
