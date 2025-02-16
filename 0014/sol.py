import operator 

def collatz(n):
    if n % 2 == 0:
        return n // 2
    return 3 * n + 1

def sequence_length(n, cache):
    original_n = n
    count = 1
    while n != 1:
        if n in cache:
            count += cache[n] - 1
            break
        n = collatz(n)
        count += 1
    cache[original_n] = count
    return count

def solve(limit):
    cache = {1: 1}
    return max(range(1, limit), key=lambda n: sequence_length(n, cache))

print(solve(10**6))
