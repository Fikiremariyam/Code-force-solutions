m,n=map(int,input().split())  
final="YES"
flag=[]  
def compute():
        
    for _ in range(m):
        input1=list(map(int,input().strip()))
        for i in range(1,n):
            if input1[i]!=input1[i-1]:
                return "NO"
        flag.append(input1)
            
    for i in range(1,m):
        if flag[i]==flag[i-1]:
            return "NO"        
    return "YES"
print(compute())
                
    