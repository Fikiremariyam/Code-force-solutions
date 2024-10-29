def is_possible(array,target,k):
     
    for i in range(0,len(array)//2):
        
        diff=array[len(array)-1-i]-array[i]

        if diff<=target:# if it is max-min already equal the target no need to do anything
            return True
        else:
            need_operation= diff - target
            k-=need_operation

            if k<0:
                return False
        
       
    return True
    
               


item ,k= map(int,input().split())
array = sorted(list(map(int,input().split())))
left=0
right=array[-1] - array[0]


while left<right:
    mid=(left+right)//2

    if is_possible(array,mid,k):
        
        right=mid
    else:
        left=mid+1
print(left )
