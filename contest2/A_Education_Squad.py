
# the solution that was not accepted 
"""
we are going to create 8 arrays  with the eith winniying possibilites 
then use count function to tell how many people can win
"""
from collections import Counter
a=list(input().strip())
b=list(input().strip())
c=list(input().strip())

win1=a #rows 
win2=b
win3=c
win4=[a[0],b[0],c[0]] # colmuns 
win5=[a[1],b[1],c[1]]
win6=[a[2],b[2],c[2]]
win7=[a[0],b[1],c[2]]# diagonals 
win8=[a[2],b[1],c[1]]# diagonals 
winrate=[set(win1),set(win2),set(win3),set(win4),set(win5),set(win6),set(win7),set(win8)]
alone=0
teamup=0

for i in winrate:
    if len(i)==1:
        alone+=1
    elif len(i)==2:
        teamup+=1

print(alone)
print(teamup)

# the peoblem that was  choosed by the a2sv
def ind_wins(player):
    for l in game:
        if len(set(l)) == 1 and player in l:
            return True
    for p in range(3):
        c = [game[j][p] for j in range(3)]
        if len(set(c)) == 1 and player in c[0]:
            return True
    if player == game[0][0] == game[1][1] == game[2][2]:
        return True
    if player == game[0][2] == game[1][1] == game[2][0]:
        return True
    return False
def team_wins(p1, p2):
    for l in game:
        if set(l) == {p1, p2}:
            return True
    for p in range(3):
        c = [game[j][p] for j in range(3)]
        if set(c) == {p1, p2}:
            return True
    d = [[game[0][0], game[1][1], game[2][2]], [game[0][2], game[1][1], game[2][0]]]
    for diag in d:
        if set(diag) == {p1, p2}:
            return True
    return False
game = [list(input()) for _ in range(3)]
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ind_wins_count = sum(ind_wins(player) for player in alphabet)
team_wins_count = sum(team_wins(alphabet[i], alphabet[j]) for i in range(25) for j in range(i+1, 26))

print(ind_wins_count)
print(team_wins_count)
    
    