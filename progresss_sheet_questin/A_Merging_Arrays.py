n,m =map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a=a+b
a.sort()
print(" ".join(str(i) for i in a))