s=input()
stack,res,k=[],[],[0]*26

for c in s:
    k[ord(c)-97]+=1

for c in s:
    stack.append(c)

    k[ord(c)-97]-=1

    while stack and sum( k[:(ord(stack[-1])-97) ] )==0:
        res.append(stack.pop())
print("".join(res))