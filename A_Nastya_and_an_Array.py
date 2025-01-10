from collections import Counter
length=int(input())
array=list(map(int, input().split() ))
array= sorted(Counter(array))
if 0 in array:
    array.pop(0)
print(len(array))
