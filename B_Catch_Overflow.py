
def soln():
    stack=[1]
    final=0
    k=(2**32) 
    for _ in range(int(input())):
        command=list(input().split())
        if command[0]=='for':
            stack.append(min(k,int(command[1])*stack[-1]))
        elif command[0]=='add' :
            final+=stack[-1]
        else:
            stack.pop()
    if final>=k:
        return "OVERFLOW!!!"
        
    return final
print(soln())