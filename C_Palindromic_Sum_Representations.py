def monotonic(i,num,val,memo):
    if i==num:
        return  1+val

for i in range(int(input())):
    number=int(input())
    print( monotonic(1,number,{}))

