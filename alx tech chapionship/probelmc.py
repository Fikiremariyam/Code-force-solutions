cities, messages= map(int, input().split())
persons=[]
totalm=[[0] * (cities + 1)
concert=[0] * (cities + 1)

for _ in range(messages):
	message, city= map(str, input().split())
	city=int(city)
	totalm[city]+=1
	if message=="D":
		concert[city]=1
	else :
		concert[city]=0

		
nonmessage=-1

for i in totalm:
	if i==0:
		nonmessage+=1

welaway=max(totalm)
 
cconcert=[]
for city,val in enumerate(concert):
	if val==1:
		cconcert.append(city-1)

cconcert=" ".join(map(str,cconcert))		


print(cconcert )
print(str(welaway) )
print(str(nonmessage) )