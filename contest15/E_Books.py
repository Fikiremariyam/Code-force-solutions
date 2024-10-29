n,maxi=map(int,input().split())
array=list(map(int,input().split()))
leng=0
summ=0
l=0
for r in  range(n):
    summ+=array[r]
    while summ>maxi:
        summ-=array[l]
        l+=1
    leng=max(leng,r+1-l)
print(leng)