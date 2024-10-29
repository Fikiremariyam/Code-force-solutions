def min_op(a, m):
    minus1 = a-1
    minus2 = a-2
    if a ==0:
        return 1
    if minus2 % m == 0:
        return 1+min_op(minus2, m)
    else:
        return 1+min_op(minus1, m)
    

 
a,m=map(int, input().split())
if a<m:
  print(-1)
else:
  final=min_op(a,m)
  print(final)