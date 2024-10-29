array=[]
for i in range(int(input())):
   print(array)
   command=list(input().split())
   if command[0] == 'insert':
        a=int(command[1])
        b=int(command[2])

        index=-1
        try:
         rev=array[::-1]
         index =  len(array)-1-rev.index(b)
        except ValueError:
            index=-1
        
        if  index == -1 or index ==len(array) -1 :
            array=array+[a]
        else:
            array=array[:index+1]+[a]+array[index+1:]
   else:
        b=int(command[1])
        index=-1
        try:
            index =  array.index(b)
        except ValueError:
            index=-1
        if index == len(array)-1:
            array=array[:index]
        else:
            if  index != -1:
                array=array[:index]+array[index+1:]
final=" ".join(map(str,array))
print(final)

