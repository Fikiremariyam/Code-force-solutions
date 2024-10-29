n=int(input())
arr1=list(map(int,input().split()))
arr1.sort()
final=[]
l,r=0,n-1
check=0
while l<=r:
    if check==0:
        final.append(arr1[l])
        l+=1
        check=1
    else:
        final.append(arr1[r])
        r-=1
        check=0
print(*final)

    