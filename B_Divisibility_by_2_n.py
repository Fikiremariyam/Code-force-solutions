for _ in range(int(input())):
    n=int(input())
    array=list(map(int,input().split()))
    product=0
    capacity=[]
    def caculate(i):
        res=0
        while i%2 ==0:
            res+=1
            i//=2
        return res    
    
    
    for i in range(n):
        product+=caculate(array[i])
        capacity.append(caculate(i+1))

    
    times=0
    capacity.sort(reverse=True)

    while product < n and times < n:
        product+= capacity[times]
        times+=1

    if product >= n:
        print (times)
    else:
        print (-1)