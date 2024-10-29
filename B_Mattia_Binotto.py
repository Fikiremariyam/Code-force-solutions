n=int(input())
array=list(map(int,input().split()))
array.sort()
n=len(array)

summ=0
satsfied=0
for i in range(n):
    if summ<= array[i]:
        summ+=array[i]
        satsfied+=1

print(satsfied)