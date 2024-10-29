n=int(input())
array=[i for i in range(1,n+1)]
def sorting(n,arr):
    if n==1:
        return arr
    arr= sorting(n - 1 , arr)
    arr[n - 1 ],arr[n - 2]= arr[n - 2 ], arr[ n - 1]
    return arr
final=sorting(n, array)
print(" ".join(map(str, final)))