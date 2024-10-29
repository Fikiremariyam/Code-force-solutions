# we can do it on brute forece method but we have to iterate up to 10**9 which will result TLE
#LETS DO IT IN A BINARY SEARCH

for _ in range(int(input())):
    n,w=map(int,input().split())
    cor=list(map(int,input().split()))

    mini=0
    maxi=int(1e12)
    while mini < maxi:
        mid=(mini+maxi+1)//2
        water= sum(max(0, mid - i) for i in cor)
        if water>w:
            maxi=mid-1
        else:
            mini=mid
    print(mini)


    