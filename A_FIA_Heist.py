array=list(input().strip())
stack=[]
i=0

while i < len(array):

    if array[i] =="<":
        if stack:
            stack.pop()
        i+=1
    else:
        stack.append(array[i])
    i+=1
print("".join(stack))
