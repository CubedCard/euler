names = [name.replace("\"", "") for name in open('input').read().strip().split(',')]
names.sort()

total = 0
for i, name in enumerate(names):
    subtotal = 0
    for char in name:
        subtotal += ord(char) - 64
    total += subtotal * (i + 1)

print(total)
