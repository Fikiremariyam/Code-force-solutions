from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    d = defaultdict(list)
    for _ in range(n):
        x, y = map(int, (input().split()))
        d[x].append(y)

                {2:[2],1:[6,10,13]}
    counter = 0
    for i, j in dicts.items():
        j.sort ( reverse=True)
        counter += sum(j[:i])
    print(counter)