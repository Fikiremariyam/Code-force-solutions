for _ in range(int(input())):
	n=int(input())
	array=list(map(int,input().split()))
	array.sort()
	if array[0]!=1:
		print("NO")
		continue
	
	summ=1
	final="YES"
	for x in array[1:]:
		if x>summ:
			final="NO"
			break
		summ+=x
	print(final)
	