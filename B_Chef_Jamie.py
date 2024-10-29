n =int(input())
arr =list(map(int,input().split()))
def min_swaps(nums):
    n = len(nums)
    arrpos = [(num, i) for i, num in enumerate(nums)]
    arrpos.sort()

    visited = [False] * n
    swaps = 0

    for i in range(n):
        if visited[i] or arrpos[i][1] == i:
            continue
        
        cycle_size = 0
        x = i
        while not visited[x]:
            visited[x] = True
            x = arrpos[x][1]
            cycle_size += 1
        
        if cycle_size > 1:
            swaps += (cycle_size - 1)
    
    return swaps

print(min_swaps(arr))