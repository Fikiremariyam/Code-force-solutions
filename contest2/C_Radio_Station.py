
"""
akalewoled @a2sv
"""
time=list(map(int,input().split()))
names=[]

for i in range(time[0]):
    command=list(input().split())
    names.append(command)
links=[]
for j in range(time[1]):
    command=list(input().split())
    links.append(command)

for i in names:
    command=i[0]
    link=i[1]+";"

    for j in links:
        if j[1]==link:
            j.append("#"+command)
for out in links:
    print(" ".join(out))