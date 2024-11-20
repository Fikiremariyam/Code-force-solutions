def max_increasing_subarray_length(arr):
    if not arr:
        return 0
    max_len = 1
    current_len = 1

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            current_len += 1
            max_len = max(max_len, current_len)
        else:
            current_len = 1

    return max_len
n=input()
array=list(map(int,input().split()))
print(max_increasing_subarray_length(array))