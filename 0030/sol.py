def f(x):
    total = 0
    for n in str(x):
        total += int(n)**5
    return total


total = 0
for x in range(2, 10**6):
    if x == f(x):
        total += x

print(total)
