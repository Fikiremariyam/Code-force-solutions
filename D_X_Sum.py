from collections import defaultdict
for _ in range(int(input())):
    m,n =map(int,input().split())

    grid=[]
    for _ in range(m):
        row=list(map(int,input().split()))
        grid.append(row)

    maximum_sum=0

    def calculate(i,j):
        north=south=east=west=0
        #calculate north
        a,b=i-1,j-1
        while a>=0 and b >=0:
            north+=grid[a][b]
            a-=1
            b-=1
        #calculate south
        a,b=i+1,j+1
        while a<m and b <n:
            south+=grid[a][b]
            a+=1
            b+=1
        #calculate east
        a,b=i-1,j+1
        while a>=0 and b <n:
            east+=grid[a][b]
            a-=1
            b+=1
        #calculate west
        a,b=i+1,j-1
        while a <m and b>=0:
            west+=grid[a][b]
            a+=1
            b-=1
        return east+west+south+north
            
    for i in range(m):
        for j in range(n):
            curr_sum=grid[i][j]+calculate(i,j)
            maximum_sum=max(maximum_sum,curr_sum)
    print(maximum_sum)
