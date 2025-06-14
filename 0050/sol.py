import numpy as np

def sieve(limit):
    is_prime = np.ones(limit + 1, dtype=bool)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            is_prime[i * i: limit + 1: i] = False
    return [num for num, prime in enumerate(is_prime) if prime]

primes = sieve(10**6)

prime_set = set(primes)

cumsum = np.cumsum(primes)

def f():
    max_length = 0
    prime_sum = 0
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            prime_sum_candidate = cumsum[j] - (cumsum[i] if i > 0 else 0)
            if prime_sum_candidate > 10**6:
                break
            if prime_sum_candidate in prime_set:
                if j - i > max_length:
                    max_length = j - i
                    prime_sum = prime_sum_candidate
    return prime_sum

print(f())
