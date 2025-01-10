A,b=input().split(" ")
length = int(input())

for _ in range(length):
    killed,replacer= input().split(" ")
    print(A,b)
    if killed == A:
        A =replacer
    else:
        b = replacer
print(A,b)