def count_divisors(n):
    divisors = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors += 2
            if i == n // i:
                divisors -= 1
    return divisors

def find_highly_divisible_triangular_number(min_divisors):
    n = 1
    triangular_number = 0
    while True:
        triangular_number = n * (n + 1) // 2
        divisors = count_divisors(triangular_number)
        
        if divisors >= min_divisors:
            return triangular_number
        n += 1

result = find_highly_divisible_triangular_number(500)
print(result)
