from itertools import permutations
from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def are_permutations(nums):
    perms = [int(''.join(p)) for p in permutations(str(nums[0]))]
    for num in nums:
        if num not in perms:
            return False
    return True

def f(nums):
    res = []
    for num in nums:
        for x in range(1, 3333):
            a, b, c = num, num + x, num + 2*x
            if c > 9999:
                return res
            if is_prime(a) and is_prime(b) and is_prime(c) and are_permutations([a,b,c]):
                res.append(''.join([str(a), str(b), str(c)]))
    return res 

nums = [x for x in range(1000, 10000)]

print(f(nums)[1])
