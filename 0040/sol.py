str_n = []

for x in range(10**6):
    if len(str_n) > 10**6 + 2:
        break
    str_n.append(str(x))
    if x == 0:
        str_n.append('.')

str_n = ''.join(str_n)
result = eval('*'.join([str_n[10**x + 1] for x in range(7)]))

print(result)
