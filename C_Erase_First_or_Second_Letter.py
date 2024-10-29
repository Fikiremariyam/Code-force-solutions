for t in range(int(input())):
    n=int(input())
    s=input()
    st = set()
    ans=0
    for ch in s:


        st.add(ch)
        ans += len(st)
 
    print(ans)