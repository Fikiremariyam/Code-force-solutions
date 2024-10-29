"""
akalewoled @a2sv
 the qustion is asking the avarage of the numbers 

"""
times=int(input())
drinks=list(map(int, input().split()))
print( f"{(sum(drinks)/times):0.12f}")
