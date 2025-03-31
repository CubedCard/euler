import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_max_prime_product(limit):
    max_primes = 0
    best_a = 0
    best_b = 0
    
    for a in range(-limit + 1, limit):
        for b in range(-limit, limit):
            n = 0
            while is_prime(n * n + a * n + b):
                n += 1
            if n > max_primes:
                max_primes = n
                best_a = a
                best_b = b
    
    return best_a * best_b

print(find_max_prime_product(1000))
