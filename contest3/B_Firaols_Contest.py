n,m=map(int,input().split())
seen={}
questions=list(map(int,input().split()))
final=[]
for i in questions:
    seen[i]=seen.get(i,0)+1
    if len(seen)==n:
        final.append(1)
        remove = [i for i in seen]
        for j in remove:
            seen[j] -= 1
            if seen[j]==0:
                seen.pop(j)
    else:
        final.append(0)
print("".join(map(str,final)))




