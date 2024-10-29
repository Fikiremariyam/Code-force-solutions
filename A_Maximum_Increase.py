n=int(input())
array=list(map(int,input().split()))
def max_increasing_subarray_length(arr):
    if not arr:
        return 0
    
    max_length = 1
    current_length = 1
    
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1
    
    return max_length
print(max_increasing_subarray_length(array))