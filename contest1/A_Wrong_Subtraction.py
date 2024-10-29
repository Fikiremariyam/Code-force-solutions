numbers = list(map(int, input().split()))
number_1=numbers[0]
number_2=numbers[1]
for i in range(number_2):
    if number_1%10==0:
        number_1=number_1//10
        
    else:
        number_1-=1
    
print(number_1)

