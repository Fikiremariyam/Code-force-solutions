
s = input()

def backtrack(s):

    i = 0
    while i < len(s):
        if s[i:i+3] == "144":
            i += 3
            
        elif s[i:i+2] == "14":
            i += 2
        elif s[i:i+1] == "1":
            i += 1
        else:
            return "NO"
    return "YES"

print(backtrack(s))