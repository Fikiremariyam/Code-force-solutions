b=list(map(int,input().split()))
ar=list(map(int,input().split()))
n=b[0]
t=b[1]
ar.sort()
for i in range (t):
    query=list(map(int,input().split()))
    q2=-1*query[0]
    q3=query[1]
    p=ar[q2:]
    r=p[:q3]
    print(sum(r))
