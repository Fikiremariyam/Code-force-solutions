
for _ in range(int(input())):
    size=int(input())
    s = list(map(int, input().split()))

    #we intally give shoes of size 1-n for all the members 
    answer=[i for i in range(1,size+1)]

    #we iterate through the list and swap the shoes if the sizes are same
    for i in range(size-2,-1,-1):
            if s[i]==s[i+1]:
                answer[i],answer[i+1] =answer[i+1],answer[i]
    #if the ith member has the ith shoe then it is not possible 
    check=0
    for i in range(size):
        if i+1==answer[i]:#this means that there is a member which his shooes size is unique and hasnt been swapped
            check=1
            break
    
    print(" ".join(map(str,answer)) if check==0 else -1)
