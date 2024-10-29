n=int(input())
stack=[]
arrange=0
next=1
for i in range(2*n):
    command=list(input().split())
    if command[0]=='add':stack.append(int(command[1]))
    else:
        if stack and stack[-1]==next:
            stack.pop()
        else:
            if stack:
                arrange+=1
            stack=[]
        next+=1
print(arrange)