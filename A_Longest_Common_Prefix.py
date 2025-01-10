final= None
for _ in range(int(input())):
    curr=input().strip()
    if not final:
        final=curr
    else:
        index=0
        while index <len(final):
            if curr[index]!=final[index]:break
            index+=1
        final=final[:index+1]
print(final[-1])

