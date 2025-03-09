def d(n):
    return sum([x for x in range(1, int(n / 2 + 1)) if n % x == 0])

divs = [(n, d(n)) for n in range(10**4)]

total = sum([sum([x for x, y in divs if x == d and y == n and n != x]) for n, d in divs])

print(total)
