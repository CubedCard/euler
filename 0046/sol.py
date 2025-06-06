from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

primes = [x for x in range(2, 10**4) if is_prime(x)]
comps = [x for x in range(2, 10**4) if not is_prime(x) and x % 2 != 0]

for comp in comps:
    d = 1
    n = 1
    while d > 0 and d not in primes:
        d = comp - 2 * n**2
        n += 1
    #if d in primes:
        #print(f"{comp} = {d} + 2 * {n-1}**2")
    if d not in primes:
        print(comp)
        break

