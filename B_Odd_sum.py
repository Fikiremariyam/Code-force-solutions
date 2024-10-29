
n=input()
array=list(map(int ,input().split()))

negatives=float("-inf")
postives=float("inf")
maxsum=sum(array)
for i in array:
    if maxsum-i>=maxsum:
        if i %2:negatives=max(negatives,i)
        maxsum-=i
    else: 
        if i%2 :postives=min(postives,i)
if maxsum%2==0:
    maxsum=max(maxsum-postives,maxsum+negatives)    
print(maxsum)
