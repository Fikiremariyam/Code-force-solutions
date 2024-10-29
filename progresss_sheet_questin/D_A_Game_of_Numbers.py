def check1(bro,sis):
    maxlen=0
    for i in bro:
        left=abs(i-sis[0])
        right=abs(i-sis[-1])
        if left> right:
            maxlen+=left
            sis.pop(0)
        else:
            maxlen+=right
            sis.pop()
    return maxlen
for i in range(int(input())):
    n,m=map(int,input().split())
    bro=list(map(int,input().split()))
    sis=list(map(int,input().split()))
    
    sis2=sorted(sis)
    sis3=sis2+[]
    max1=check1(bro,sis3)
    bro2=sorted(bro)
    max2=check1(bro2,sis2)  
    
    print(max(max1,max2))
    