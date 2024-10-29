from collections import Counter
for _ in range(int(input())):
    word=list(map(str,input().strip()))
    final=len(Counter(word))
    if final > 1:
        print('YES')
        print("".join(word[1:]+word[:1]))
    else :
        print('NO')