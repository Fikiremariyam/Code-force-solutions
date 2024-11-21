""" 
frogs question
*** approach ***

1 fined alll the input 

2. sort the filies list and intitate  the  result list 
3 .iterate over each forgs 
4 .on each iteration fined the  flies that are inside the radious of  the frog tounge 
    i.e postion - tounge size   << ---->>  postion + tounge size
     fined these by using biniary search 
5 ,append: the right boundry - the left boundry +1 to the result array 

time complexity  :    O( n(log n) )

space complextity : O ( n )


"""
def findleft(target,y):
    
    left=0
    right=len(y)-1

    while left <= right:
        mid=(right - left)//2 + left

        if y[mid] <target :
            left=mid+1
        elif y[mid] >= target :

            right =mid -1
    return left
#
def findright(target,y) :
    left=0
    right=len(y)-1

    while left <= right:
        mid= (right - left) //2 +left
        if y[mid] > target :
            right-=1
        elif y[mid] <=target:
            left+=1

    return right




def solution(x,s,y):
    res=[]
    y.sort()
    for i in range(len(s)):
        res.append( (findright(x[i]+s[i],y) - findleft(x[i]-s[i] ,y) ) + 1 )
    return res



x , s , y = [1,6,3] , [2,2,5] , [1 ,2 ,3, 4,5,6,7,8,9]
print(solution(x,s,y))
