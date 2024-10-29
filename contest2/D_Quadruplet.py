
a,B=list(map(int,input().split()))

array=list(map(int,input().split()))

from itertools import combinations
lists=[i for i in range(a)]
for combo in combinations(lists, 4):
    a=array[combo[0]]
    b=array[combo[1]]
    c=array[combo[2]]
    d=array[combo[3]]
    if a+b+c+d==B:
        print(combo[0]+1,combo[1]+1,combo[2]+1,combo[3]+1)
        break
       
# the prefect solutionn
    n, target = map(int, input().split())
arr = list(map(int, input().split()))

store = {}

for i, num in enumerate(arr):
  for j in range(i + 1, len(arr)):
    total = arr[i] + arr[j]
    if target - total in store:
      print(*store[target - total], i + 1, j + 1)
      exit()
  for j in range(i):
    total = arr[i] + arr[j]
    store[total] = (i + 1, j + 1)

print("IMPOSSIBLE")
#code by Ananiya