n=input()
array=list(map(int,input().split()))

fixed=float("inf")
for i in range(1,len(array)):    
    if array[i]<array[i-1]:
        fixed=array[i]
    if array[i]>array[i-1] and array[i]> fixed:
        array[i]=fixed
print(" ".join(map(str,array)))
    
