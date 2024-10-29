for _ in range(int(input())):
    n=int(input())
    array=list(map(int,input().split()))
    
    comparsion=sorted(array)
    memo={}
    for i in range(n):
        diminish=sum(comparsion[:i+1]) 
        power=i
        for j in range(i+1,n):
            if  diminish >= comparsion[j]:
                    diminish+=comparsion[j]
                    power+=1
            else:break
        memo[comparsion[i]]=power
    final=" ".join(map(str,[memo[i]  for i in array]))
    print(final)
##     
'''''  
for _ in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    comparsion = sorted(array)

    pref = [0] * n
    pref[0] = comparsion[0]
    for i in range(1, n):
        pref[i] += comparsion[i] + pref[i - 1]

    ref = dict()
    ref[comparsion[-1]] = n - 1

    for i in range(n - 2, -1, -1):
        if pref[i] >= comparsion[i + 1]:
            ref[comparsion[i]] = ref[comparsion[i + 1]]
        else:
            ref[comparsion[i]] = i
    
    print(" ".join(map(str,[ref[array[i]] for i in range(n)]))) 
'''