def prime_factors(n):
    factors = set()
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            factors.add(d)
            n //= d
        d += 1
    if n > 1:
        factors.add(n)
    return factors

def find_consecutive_numbers_with_four_prime_factors():
    consecutive = 0
    num = 2
    while True:
        if len(prime_factors(num)) == 4:
            consecutive += 1
            if consecutive == 4:
                return num - 3
        else:
            consecutive = 0
        num += 1

print(find_consecutive_numbers_with_four_prime_factors())
