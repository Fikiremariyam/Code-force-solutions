
for i in range(int(input())):
    n=input()
    nums=list(map(str,input().strip()))
    final={'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    for i in nums:
        final[i.lower()]=1+final.get(i.lower(),0)
    res,count=0,1
    for i in final:
        #print(i,count,res)
        if final[i]>=count:
            res+=1
        count+=1
    print(res)





def func(num):
    cnt = 0

    while num % 2 == 0:
        num //= 2
        cnt += 1

    return cnt

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    total = 0
    indices = [0] * n

    for num in nums:
        total += func(num)

    if total >= n:
        print(0)
        continue
    
    for i in range(1, n + 1):
        indices[i - 1] += func(i)
    
    indices.sort(reverse=True)
    op = 0

    for i in range(n):
        total += indices[i]
        op += 1
        if total >= n:
            print(op)
            break
    
    if total < n:
        print(-1)