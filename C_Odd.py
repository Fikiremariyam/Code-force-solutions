from collections import Counter


for _ in range(int(input())):
    n=int(input())
    array=list(map(int,input().split()))
    
    array=Counter(array)
    
    value=set()
    for i in array:
        while i % 2 ==0:
            value.add(i)
            i //=2
    print(len(value))