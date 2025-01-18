for _ in range(int(input())):
    permiter=0
    operations,n=map(int,input().split())
    x,y = map(int,input().split())
    permiter+= 2*n+2*n
    for _ in range(operations-1):
        x,y = map(int,input().split())
      #  print(x,y,permiter)
        permiter+= 2 * n
        permiter+= x + y 

        permiter-= n-x 
        permiter-=n-y
    print(permiter)
    #print("=========================")


