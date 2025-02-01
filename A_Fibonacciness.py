for i in range(int(input())):
    array=list(map(int,input().split()))
    final=0
    for i in range(-500,500):
        curr=0
        curr += 1 if array[0]+array[1] ==i else 0
        curr +=1  if array[1]+i == array[2] else 0 
        curr+= 1 if  array[2]+i ==  array[3] else 0
        final=max(final,curr)
    print(final)#