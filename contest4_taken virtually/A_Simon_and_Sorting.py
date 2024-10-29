final="YES"
for i in range(int(input())):
    indicator=0
    arrays=list(map(str,input().strip()))
    if arrays[0]!='a':
        indicator+=1
    if arrays[1]!='b':
        indicator+=1
    if arrays[2]!='c':
        if indicator ==2:
            print("NO")
            continue
    print("YES")
