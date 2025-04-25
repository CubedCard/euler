import math

print(sum(x for x in range(3, 10**6) if sum(math.factorial(int(c)) for c in str(x)) == x))
