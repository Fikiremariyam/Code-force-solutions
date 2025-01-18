from collections import Counter
for _ in range(int(input())):
    n=int(input())
    arr= list(map(int,input().split()))
    
    count= Counter(arr)
    n_min=0

    while count[n_min] >0 :
        n_min +=1
    res=n_min * (count[0]-1)

    probs = [0] * n_min

    for i in range(1,n_min):
        probs[i] = float("inf")
        for j in range(i):
            curr= i * count[j] + probs[j]
            if curr<probs[i]:
                probs[i]= curr
        res=min(res, probs[i]+n_min * (count[i]-1))
    print(res if res !=float("inf") else 0)