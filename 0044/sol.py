def P(n): return (1 + (24 * n + 1) ** 0.5) % 6 == 0

def solve():
    i = 1
    while True:
        for j in range(1, i):
            a, b = i * (3 * i - 1) // 2, j * (3 * j - 1) // 2
            if P(a + b) and P(a - b): return abs(a - b)
        i += 1

print(solve())
