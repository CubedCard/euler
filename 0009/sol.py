def IsTriplet(a, b, c):
    if not (a < b < c):
        return False
    if a**2 + b**2 != c**2:
        return False
    return True

def solve(t, m):
    for a in range(1, m):
        for b in range(2, m):
            for c in range(3, m):
                if a + b + c == t and IsTriplet(a, b, c):
                    print(a * b * c)
                    return

solve(1000, 501)
