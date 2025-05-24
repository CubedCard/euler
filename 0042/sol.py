words = [word.replace('"', '') for word in open('input').read().strip().split(',')]

def t(n):
    return (int)(0.5*n*(n + 1))

ts = [t(n) for n in range(100)]

triangles = 0
for word in words:
    total = 0
    for char in word:
        total += ord(char) - 64
    if total in ts:
        triangles += 1

print(triangles)
