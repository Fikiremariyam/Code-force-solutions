def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def nthperfect(n):
    count = 0
    num = 19  
    
    while True:
        if sum_of_digits(num) == 10:
            count += 1
            if count == n:
                return num
        
        num += 9  
        

n=int(input()) 
print(nthperfect(n))