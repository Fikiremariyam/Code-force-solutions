
#intiutuve : genrating all the prime numbers up to n 
#              loop through evry prime if it devises the  current number 
                #if the total divisors equal to to count that number as perfect 
                #do this for every number up to n
n = int(input())
is_prime = [True] * (n + 1)
primes = []

for i in range(2, n + 1):
    if is_prime[i]:
        primes.append(i)
        for multiple in range(i * 2, n + 1, i):
            is_prime[multiple] = False

distinct_prime_factors_count = [0] * (n + 1)

for prime in primes:
    for multiple in range(prime, n + 1, prime):
        distinct_prime_factors_count[multiple] += 1
        
print(distinct_prime_factors_count)
almost_prime_count = sum(1 for count in distinct_prime_factors_count if count == 2)

print(almost_prime_count)
