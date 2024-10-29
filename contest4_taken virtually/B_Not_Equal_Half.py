
i=int(input())
a=list(map(int,input().split()))

a=sorted(a)


if sum(a[:i])==sum(a[i:]):
    print(-1)
else:
    print(" ".join(str(i) for i in a ))

