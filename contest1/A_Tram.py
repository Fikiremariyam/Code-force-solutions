capacity,max_capacity=0,0

for _ in range (int(input())):
    inout=list(input().split(" "))
    inn=int(inout[0])
    outt=int(inout[1])
    capacity+=(outt-inn)
    max_capacity=max(max_capacity,capacity)

print(max_capacity)
               

