nameing={}
for _ in range(int(input())):
    name=input()
    if name in nameing:
        nameing[name]=nameing.get(name)+1
        print(name+str(nameing[name]))

    
    else:
        nameing[name]=0
        print("OK")
