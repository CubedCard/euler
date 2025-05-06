def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    str_n = str(n)
    
    for i in range(len(str_n)):
        if not is_prime(int(str_n[i:])):
            return False
    
    for i in range(len(str_n)):
        if not is_prime(int(str_n[:len(str_n)-i])):
            return False
    
    return True

def find_truncatable_primes(limit):
    truncatable_primes = []
    num = 11
    
    while len(truncatable_primes) < limit:
        if is_prime(num) and is_truncatable_prime(num):
            truncatable_primes.append(num)
        num += 1
    
    return truncatable_primes

truncatable_primes = find_truncatable_primes(11)
print(sum(truncatable_primes))
