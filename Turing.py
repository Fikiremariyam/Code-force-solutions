x , s , y = [1,6,3] , [2,2,5] , [1 ,2 ,3, 4,5,6,7,8,9]

y.sort() 

def max_left(dist):
    left ,right = 0 , len(y)-1
    while left <=  right:
        mid= (right -left) //2 + left

        if  y[mid] < dist:
            left = mid +1
        elif y[mid] >= dist :
            right= mid -1
    return left

def max_right(dist):
    left,right = 0,len(y)-1

    while left<= right:
        mid= (right - left)//2 +left
        
        if y[mid] <=dist:
            left= mid +1
        elif y[mid] >dist:
            right = mid -1
    return right



res=[]
for i,val in enumerate(x):
    leftrange ,rightrange=max_left(x[i]-s[i]),max_right(x[i]+s[i])
    res.append( (rightrange-leftrange) +1)
print(res)



''''
approach  
sort the distances of the frog for better optimazation

find the flies a frog can eat using its tounge from the left side by caculating its left most boundry 
find the flies a frog can eat ising its taunge from the right side 

deduct the left boundry from the  total eating capability of the frog 
append the result in a final array 

'''




""" 
using brute force approach  
x , s , y = [1,6,3] , [2,2,5] , [1 ,2 ,3, 4,5,6,7,8,9]

y.sort()
final=[]
for i in range(len(x)):
    flies=0
    for j in y:
        if  abs(x[i]- j ) <= s[i]:
            flies+=1
    final.append(flies)

print(final)

"""
