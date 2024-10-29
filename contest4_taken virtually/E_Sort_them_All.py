for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    final=[]
    for i in range(n):
        mini=i
        for j in range(i+1,n):
            if a[j]<a[mini]:
                mini=j
        if mini!=i:
            a[i],a[mini]=a[mini],a[i]
            b[i],b[mini]=b[mini],b[i]
            final.append([mini+1,i+1])
    c=sorted(b)

    if b==c:
        print(len(final))
        for i in final:
            print(i[0],i[1])
    else:
        print(-1)


