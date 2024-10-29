n=int(input())

array=list(map(int,input().split()))
mapping=sorted(array)



while mapping:
    first=mapping.pop(0)
    second=mapping.pop(-1)
    id1=array.index(first)
    array[id1]=-1
    id2=array.index(second)
    array[id2]=-1
    print(str(id1+1),str(id2+1))

