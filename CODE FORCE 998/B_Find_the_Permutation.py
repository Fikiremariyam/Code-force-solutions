for _ in range(int(input())):
    
    n=int(input())
    graph={i:[] for i in range(1,n+1)}
    if n==1: 
        input()
        print(1)
        continue

    for i in range(int(n)):
        array=list(map(int,input().strip()))
        for j in range(n):
            if i < j and array[j]==1:
                graph[j+1]= [i+1]+graph.get(j+1,[])
    

    p=[0 for _ in range(n+1)]
    seen=()
    for index in range(n,0,-1):
        
        

        ptr=1
        while ptr <= n and  p[ptr] != 0 : ptr+=1
        for i in graph[index]:
            if 


        ptr+=a
        while ptr <= n and  p[ptr] != 0 : ptr+=1
        p[ptr] = index

        
    print(" ".join(map(str,(p[1:]))))


