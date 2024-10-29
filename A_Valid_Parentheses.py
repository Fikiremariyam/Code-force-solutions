array=list(map(str,input().strip()))
final=0
stack=[]
for i  in array:
    if i == "(":
        if len(stack) <1 or stack[-1]=="(":
            stack.append(i)
    else:
        if stack and stack[-1]=="(":
            final+=2
            stack.pop()
print(final)
        