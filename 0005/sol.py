import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

result = 1
for num in range(1, 21):
    result = lcm(result, num)

print(result)
