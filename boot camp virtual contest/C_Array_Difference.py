for _ in range(int(input())):
    m,n=map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted( list(map(int, input().split())), reverse=True)

    ans = 0
    for i in range(m):
        ans+= max(abs(a[i]-b[i]), abs(a[i-m]- b[i-m]))
    print(ans)
