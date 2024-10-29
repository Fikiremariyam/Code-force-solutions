n,leng=map(int,input().split())

arr=list(map(int,input().split()))
final=1
summ=0
for i in range(n):
    summ+=arr[i]
    if summ<=leng:
        final+=1
    else:
        break
print(final)