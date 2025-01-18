s = input().strip()
t = input().strip()

n= int(input())
INF=float("inf")
dist=[[INF] *26 for _ in range(26)]


for i in range(26):
    dist[i][i] = 0

for _ in range(n):
    a,b,w =input().split()
    a=ord(a)-ord('a')
    b= ord(b) - ord('a')
    w= int(w)
    dist[a][b]= min(dist[a][b],w)

for k in range(26):
    for i in range(26):
        for j in range(26):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
total=0
for i in range(min(len(t),len(s))):
    si=ord(s[i])- ord('a')
    ti= ord(t[i]) - ord('a')
    total+=dist[si][ti]
print(total)
