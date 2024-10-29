ntn=int(input())
nums=list(map(int,input().split()))
postive=[]
zero=[]
negative=[]
for i in nums:
    if i >0:
        postive.append(i)
    elif i==0:
        zero.append(i)
    elif i<0:
        negative.append(i)
if len(postive)==0:
    a=negative.pop()
    b=negative.pop()
    postive.append(a)
    postive.append(b)
if len(negative)%2==0:
    a=negative.pop()
    zero.append(a)

    

print(len(negative)," ".join(map(str ,negative)))
print(len(postive)," ".join(map(str,postive)))
print(len(zero)," ".join(map(str,zero)))


