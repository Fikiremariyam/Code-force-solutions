string=input() 
n=int(input())

presum=[1] # the list to hold the repitition of the valid indexes

c=1 # temporary counter
for i in range(1,len(string)):
    if string[i]==string[i-1]:
        c+=1
    presum.append(c)
print(presum)

for i in range(n):
    l,r=map(int,input().split())
    print(presum[r-1]-presum[l-1])
