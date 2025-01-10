from collections import Counter
for _  in range(int(input())):
    length,power=map(int,input().split())
    array=list(map(str,input().strip()))
    array=Counter(array)
    brules=0
    seen=set()
    for letter in array:

        if letter in seen :
            continue

        if letter ==letter.lower():
            lowerval=array[letter]
            seen.add(letter)
            upperval=array.get(letter.upper(),0)
            seen.add(letter.upper())
        else:
            upperval=array[letter]
            seen.add(letter)
            lowerval=array.get(letter.lower(),0)
            seen.add(letter.lower())
        
        brules+=min(lowerval,upperval)

        if  power >=0:
            
            diff=abs(lowerval-upperval)//2
            if power >= diff:
                
                power-=diff
                brules+=diff
               
            else:
                brules+=power
                power=0
    print(brules)
