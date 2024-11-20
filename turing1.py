x , s , y = [1,6,3] , [2,2,5] , [1 ,2 ,3, 4,5,6,7,8,9]

y.sort()
def findLeft(val):
    l , r = 0 , len(y) - 1
    while l <= r:
        mid = (r - l) // 2 + l 

        if y[mid] < val:
            l = mid + 1
        elif y[mid] >= val:
            r = mid - 1
    
    return l

def findRight(val):
    l , r = 0 , len(y) - 1

    while l <= r:
        mid = (r - l) // 2 + l 
        
        if y[mid] <= val:
            l = mid + 1
        elif y[mid] > val:
            r = mid - 1
    return r

res = []
for ind,val in enumerate(x):
    right , left = findRight(val+s[ind]), findLeft(val-s[ind])
    res.append(right - left + 1)
print(res)
