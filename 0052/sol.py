def f(x, r):
    l = [[int(i) for i in str(x*y)] for y in range(1, r + 1)]
    [i.sort() for i in l]
    distinct_values = set(tuple(i) for i in l)
    return len(distinct_values) == 1

for x in range(1, 10**6):
    if f(x, 6):
        print(x)
        break
