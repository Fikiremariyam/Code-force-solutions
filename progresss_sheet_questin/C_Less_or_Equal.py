n,k=map(int,input().split())
arr1=list(map(int,input().split()))
arr1.sort()
arr1=[-1]+arr1
if n==k or arr1[k]!=arr1[k+1]:
    print(arr1[k])
else:
    print(-1)