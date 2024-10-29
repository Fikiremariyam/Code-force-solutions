for _ in range(int(input())):
    leng=int(input())
    array=list(map(int, input().split()))
    array.sort()
    mini=float('inf')
    for i in range(leng-1):
        tempo=abs(array[i]-array[i+1])
        mini=min(mini,tempo)
    print(mini)