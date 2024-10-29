def dfs(i, j, cost, k, memo):
    if i > m or j > n:
        return False
    if cost > k:
        return False
    if (i, j, cost) in memo: 
        return memo[(i, j, cost)]
    if i == m and j == n:  
        return cost == k
    
    
    result = dfs(i + 1, j, cost + j, k, memo) or dfs(i, j + 1, cost + i, k, memo)
    
    
    memo[(i, j, cost)] = result
    return result

for _ in range(int(input())):
    n, m, k = map(int, input().split())
    
    
    memo = {}
    if dfs(1, 1, 0, k, memo):
        print('YES')
    else:
        print('NO')
