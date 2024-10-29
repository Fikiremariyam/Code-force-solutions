n=int(input())
finals=0
while n>0:
    if n >=100:
        bills=n//100
        finals+=bills
        n=n-(100*bills)
    elif n >=20:
        bills=n//20
        finals+=bills
        n=n-(20*bills)
    elif n >=10:
        bills=n//10
        finals+=bills
        n=n-(10*bills)
    elif n >=5:
        bills=n//5
        finals+=bills
        n=n-(5*bills)
    else:
        finals+=n
        break
print(finals)  ###############  

    
