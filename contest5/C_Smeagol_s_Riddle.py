for _ in range(int(input())):
    word=list(map(str,input().strip()))
    final=0
    leng=len(word)
    for i in range(leng//2):

        if word[i]!=word[(leng-1)-i]:
            final+=1
    print(final)