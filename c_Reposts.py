
reposted={"polycarp":1}

for _ in range(int(input())):
    name1,repost,name2=input().split()
    reposted[name1.lower()] = 1+ reposted[name2.lower()]
print(max(reposted.values()))