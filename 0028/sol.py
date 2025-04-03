m = 1001 * 1001

total, layer = 0, 1

def f(n):
    return (2*(n) - 1)**2

for x in range(1, m + 1):
    if x == 1 or (x - 1) % (2 * (layer - 1)) == 0:
        total += x
    if f(layer) == x:
        layer += 1

print(total)
