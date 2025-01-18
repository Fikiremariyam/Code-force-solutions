

a,c = map(int,input().split())
a_tenary=[]
c_ternary=[]
while a> 0:
    a_tenary.append(a%3)
    a//=3
while c> 0:
    c_ternary.append(c%3)
    c//=3
a_tenary=a_tenary[::-1]
c_ternary=c_ternary[::-1]

max_len=max(len(a_tenary),len(c_ternary))

a_tenary =[0] * (max_len -len(a_tenary))+ a_tenary
c_ternary = [0] * (max_len-len(c_ternary))+c_ternary

b_ternary=[]
for i in range(len(a_tenary)):
    b_digit=(c_ternary[i] - a_tenary[i])%3
    b_ternary.append(b_digit)
b=0
for digit in b_ternary:
    b= b*3 + digit
print(b)