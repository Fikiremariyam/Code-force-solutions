
a,b=map(int,(input().split()))
import math
from functools import reduce

def gcf_of_interval(start, end):
    current_gcf = start
    for num in range(start + 1, end + 1):
        current_gcf = math.gcd(current_gcf, num)
        if current_gcf == 1:  # Early exit if GCF reaches 1
            return 1
    return current_gcf

print(gcf_of_interval(a, b))  # Output: 1
