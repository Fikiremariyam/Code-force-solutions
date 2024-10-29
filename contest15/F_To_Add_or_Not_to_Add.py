n,k=map(int, input().split())
array=list(map(int,input().split()))

array.sort()

summ,maxx =0,0

item,i,j=0,0,0

while i<n:
    summ+=array[i]
    while(array[i] * (i-j+1) - summ > k):
        summ-=array[j]
        j+=1
    if maxx < i-j+1:
        maxx=i-j+1
        item=array[i]
    i+=1

print(maxx,item)