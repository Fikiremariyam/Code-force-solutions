for _ in range(int(input())):
    first, second = map(int, input().split())
    print(min(min(first,second), (first+second) // 4))