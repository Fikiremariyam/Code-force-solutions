smoke=list(map(str,input().strip()))
max_count = 0
current_count = 0
for smok in smoke:
    if smok == 'O':
         current_count += 1
    else:
        max_count = max(max_count, current_count)
        current_count = 0

if smok[-1]=='O':
    max_count = max(max_count, current_count)
print(max_count)
