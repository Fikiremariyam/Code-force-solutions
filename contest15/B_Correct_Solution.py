n=list(map(int, input().strip()))
ans=list(map(int, input().strip()))
n=sorted(n)
lead=[]
for i in range(len(n)):
    if n[i]>0:
        lead.append(n.pop(i))
        break
n=lead+n
if ans==n:
    print('OK')
else:
    print('WRONG_ANSWER')