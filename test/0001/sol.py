m = 1000
muls = [3, 5]

result = set()
for mul in muls:
    x = 1
    while x * mul < m:
        result.add(x * mul)
        x += 1

print(sum(result))
