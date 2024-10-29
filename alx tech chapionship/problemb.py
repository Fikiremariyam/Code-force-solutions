row,col=map(int, input().split())
persons=[]
for _ in range(row):
	cur=list(map(int, input().split()))
	persons.append(sum(cur))

minval,minindex=max(persons),0
maxval,maxindex=0,0
print(persons)

for i  in range(len(persons)):
	
	if persons[i] < minval :
		minval=persons[i]
		minindex=i
		
	if persons[i] > maxval :
		maxval=persons[i]
		maxindex=i
	print(minval,maxval)
		
final= str(minindex+1) +" "+ str(maxindex+1)
print(final)
		