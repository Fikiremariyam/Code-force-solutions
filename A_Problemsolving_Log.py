from collections import Counter
for _ in range(int(input())):
    n=int(input())
    array=list(map(str,input().strip()))
    array=Counter(array)
    solved=0
    for i in array:
        if array[i] >ord(i)-ord('A'):
            solved+=1
            
    print(solved) 
