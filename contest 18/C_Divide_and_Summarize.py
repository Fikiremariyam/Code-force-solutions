
p=[]
def pretty(arr):

    if arr.count(arr[0])==len(arr): # if [5] or [5,5,5,5] 
        p.append(sum(arr))
        return

    arr.sort()

    mid = (arr[0]+arr[-1])//2

    point=0
    for i in range(len(arr)):
        if arr[i]>mid:
            point=i
            break

    left = arr[0:point]
    right = arr[point:]

    p.append(sum(right))
    p.append(sum(left))

    pretty(right)
    pretty(left)


for _ in range(int(input())):
    n,q = map(int,input().split())
    arr =sorted( list(map(int,input().split())))
    
    pretty(arr)
    p.append(sum(arr))
    p=set(p)# to simplify the searching 

    for _ in range(q):
        x=int(input())
        print('Yes' if x in p else 'No')
    
    p=[] #making it free the memory for next test case
 
 
        
