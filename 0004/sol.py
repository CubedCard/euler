def IsPalindrome(n):
    return str(n) == str(n)[::-1]

m = 0
for x in range(999, 100, -1):
    for y in range(999, 100, -1):
        if (IsPalindrome(x * y)):
            m = max(x * y, m)
            break

print(m)
