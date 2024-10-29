n=input()
array=list(map(int,input().split()))
from collections import Counter
    final=Counter(array)
    profit=0
    final[0]=0
    while final: 
        maxi=0 
        for i in final:
            if final[i] *i >final[maxi]*maxi:
                maxi=i
        profit+=maxi*final[maxi]
        final.pop(maxi)
        if maxi-1 in final:
            final.pop(maxi-1)
        if maxi+1 in final:
            final.pop(maxi+1)
print(profit)