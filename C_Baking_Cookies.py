n, k = map(int, input().split())  
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def canCook(x, a, b, k, n):
    required_magic = 0
    for i in range(n):
        total_required = a[i] * x
        if total_required > b[i]:
            required_magic += total_required - b[i]
        
        if required_magic > k:
            return False

    return required_magic <= k


left, right = 0, 10**9

while left < right:
    mid = (left + right + 1) // 2
    
    if canCook(mid, a, b, k, n):
        left = mid  
    else:
        right = mid - 1

print(left)