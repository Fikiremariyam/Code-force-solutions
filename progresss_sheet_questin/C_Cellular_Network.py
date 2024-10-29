n,m=map(int,input().split())
cities=list(map(int,input().split()))
laterns=list(map(int,input().split()))
final=0
last=0
for i in range(n):
    ct=cities[i]
    min_leng=abs(ct-laterns[last])
    for j in range(last,len(laterns)):
         tempo=abs(ct-laterns[j])
         if tempo<= min_leng:
              min_leng=tempo
              last=j
         else:
             break
    final=max(final,min_leng)
print(final)
