for _ in range(int(input())):
    array=list(map(int, input().split()))
    if sum(array)-min(array)>=10:
        print("YES")
    else:
        print("NO")