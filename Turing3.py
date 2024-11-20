
from collections import Counter


def helper(woods, target):
    left = 0
    right = len(woods) - 1
    result = 0

    while left < right:
        s = woods[left] + woods[right]

        if s == target:
            result += 1
            left += 1
            right -= 1
        elif s < target:
            left += 1
        else:
            right -= 1

    return result


def solve(woods):
    woods = sorted(woods)
    freq = Counter(woods)

    for key in freq.keys():
        freq[key] += helper(woods, key)

    result = max(freq.values())

    
    freq = Counter()

    for i in range(len(woods)):
        for j in range(len(woods)):
            freq[woods[i] + woods[j]] = 0
        

    for key in freq.keys():
        freq[key] += helper(woods, key)

    
    return max(result, max(freq.values()))


print(solve([22, 12, 13, 22, 22, 22, 14, 22, 17, 22]))
print(solve([8, 13, 7, 13, 5, 13, 4, 13, 6, 13]))
