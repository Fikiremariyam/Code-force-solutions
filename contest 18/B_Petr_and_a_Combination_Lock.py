def backTrack(n,i, angles):
    if i==len(angles):
        if n==0 or n% 360 ==0 : 
            return True
        else : return False
    
    return backTrack(n+angles[i],i+1,angles) or backTrack(n-angles[i],i+1,angles)


n = int(input())
angles = []
for _ in range(n):
    angles.append(int(input()))


print('YES' if  backTrack(0,0, angles) else 'NO')