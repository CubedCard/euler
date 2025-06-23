import math

def count_combinations(limit):
    count = 0
    for n in range(23, 101):
        for r in range(1, n):
            if math.comb(n, r) > limit:
                count += 1
    return count

limit = 1000000
result = count_combinations(limit)
print(result)
