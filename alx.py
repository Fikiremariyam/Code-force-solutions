for _ in range(int(input())):
    occurrence_count = {}
    n=int(input())
    
    for _ in range(10 ** 10):

        if n in occurrence_count:
            occurrence_count[n] += 1
        else:
            occurrence_count[n] = 1
        if n == 1:
            break
        elif n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(max(occurrence_count.values()))
    
    