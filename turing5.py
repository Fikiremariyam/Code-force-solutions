"""
n permituation 
 ****approach ***
1 fined the input 
2 sort the given array
3 intiate the result varible
4 traverse from 0 to the length of the array 
    while trasforming if the value at array [i] is diffrent from i 
    add the diffrence to the result varible 
5 return the  result


"""
def solution(array):
    array.sort()
    res = 0

    for i in range(len(array)):
        if array[i] != i :
            res+=abs(i +1 - array[i])
    return res


print(solution([2,3,4,5]))

        
