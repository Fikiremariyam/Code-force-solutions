n=int(input())
array=list(map(int,input().split()))
from collections import Counter
array=Counter(array)
import math
print(math.factorial(len(array)))