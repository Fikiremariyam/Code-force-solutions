for _ in range(int(input())):
    n=int(input())
    final=n
    multi=1
    for i in range(2,n):
        x=n//i 
        if x  > multi:
            multi=x
            final=i
    print(final)


    
