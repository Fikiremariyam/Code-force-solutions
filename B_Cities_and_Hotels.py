n,k = map(int,input().split())
array=list(map(int,input().split()))

final =0
for i in range(n):
    left= array[i]-k
    if i==0 or left > array[i-1]+k:
        final +=1
    right= array[i]+k 
    if i ==n -1 or right <= array [i+1]- k:
        final+=1

print(final)