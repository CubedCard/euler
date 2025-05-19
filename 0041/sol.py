import itertools
from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def pandigital_numbers(n):
    digits = ''.join(str(i) for i in range(1, n + 1))
    return [int(''.join(p)) for p in itertools.permutations(digits)]

def find_pandigital_primes():
    pandigital_primes = []
    for n in range(1, 10):
        for num in pandigital_numbers(n):
            if is_prime(num):
                pandigital_primes.append(num)
    return pandigital_primes

print(max(find_pandigital_primes()))
