""" fiker @a2sv"""""
leng=int(input())
questions=list(map(int,input().split()))
if sum(questions)>0:
    print("HARD")
else:
    print("EASY")
