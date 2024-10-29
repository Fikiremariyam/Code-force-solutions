n,m=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
greter=[]
final=0
for i in range(m):
    while final<n and arr1[final]<arr2[i] :
        final+=1
    greter.append(final)
for j in greter:
    print(str(j),end=" ")
