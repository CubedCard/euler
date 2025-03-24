fibonacci = []

x, i, m = 1, 0, 4 * 10**1000
while x < m:
    if i - 2 >= 0:
        x = fibonacci[i - 2] + fibonacci[i - 1]
    elif i - 1 >= 0:
        x = fibonacci[i - 1]
    fibonacci.append(x)
    i += 1

print([i for i, x in enumerate(fibonacci) if len(str(x)) == 1000][0] + 1)
