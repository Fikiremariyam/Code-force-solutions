men,elf,daw,orc,wolf=map(int,input().split())
menp,elfp,dawp,orcp,wolfp=map(int,input().split())
left=men*menp+elf*elfp+daw*dawp
right=orc*orcp+wolf*wolfp
if left>right:
    print("WIN")
elif right>left:
    print("LOSE")
else:
    print("DRAW")