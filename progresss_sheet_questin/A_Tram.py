capacity,maxcapacity=0,0
for i in range(int(input())):
    a,b=map(int,input().split())
    capacity+=(b-a)
    maxcapacity=max(maxcapacity,capacity)
print(maxcapacity)
