n,d=map(int,input().split())
flowers=list(map(int,input().strip()))
pos=0
final=0
while  pos< n:
    
    
    if pos==n-1:
        break

    i=pos+1
    curr=pos
    
    while i<= pos+d  and i<n:
        
        if flowers[i] == 1:
            curr=i
        i+=1

    if curr==pos:
        final=-1
        break
    pos=curr
    final+=1


print(final)

