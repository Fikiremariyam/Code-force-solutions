"""
FIKER @A2sv
"""
for i in range(int(input())):
    leng=int(input())-1
    str1=list(map(int,input().strip()))
    check=0
    for i in range(0,leng//2):
        if str1[i]!=str1[leng-1]:
            if check==1:
                check+=1
                break
            check+=1
    if check==2:
        print("No")
    else:
        print("yes")


