""" 
the longest subsequence of an array oof the zero and ones
  1 fined the input and out put 
  2 initate tow pointers
  3 increse right pointer while  the sequnce holds true
  4. then the sequnce holds false caculate the diffrecne between left and right pointer and appoint maximum of result and the diffrence to result varible
  5 set the value  of left equal to the right and start to move the right pointer again 
  6 do this until right  equals the length of the array 
 """

def solution (x):
    if len(x) <= 1:
        return len(x)
    
    left,right =0, 1
    res=0

    while right < len(x) :
        while right < len(x) and x[right] + x[right - 1] ==1 :
            right+=1

        diff=right-left
        res= max(res,diff)

        left=right
        right+=1
        
    return res
print(solution([0,1,0,0,1]))
