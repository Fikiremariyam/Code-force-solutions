
def checkfunc(array,n,k):
    final=0
    mini=min(array)

    for i in array:
        change=i-mini
        if change %k != 0:
            return -1
        
        final+= change //k
        
    return final



n,k=map(int,input().split())
shares=list(map(int,input().split()))
if n<=1:
    print(0)
else:
    print(int(checkfunc(shares,n,k)))