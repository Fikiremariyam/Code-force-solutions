N,Q = input().split()
array= list(input().split())
compare=list(input().split())
D = []

def find_dividers(n):
    dividers=[]
    for i in range(1,n+1):
        if n % i ==0:dividers.append(i)    
    return(dividers)

for i in array:
    D+= find_dividers(int(i))
D.sort()

final=[]
for ele in compare:
    final.append(D[int(ele)-1])

for i in final:
    print(i,end=" ")