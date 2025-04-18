total = set()
for a in range(10**3):
    for b in range(10**4):
        l = [x for x in (str(a) + str(b) + str(a*b))]
        l.sort()
        if ''.join(l) == '123456789':
            total.add(a*b)
print(sum(total))
