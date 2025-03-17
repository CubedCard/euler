def sum_of_divisors(n):
    divisors = [1]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sum(divisors)

def find_abundant_numbers(limit):
    abundant_numbers = []
    for i in range(12, limit):
        if sum_of_divisors(i) > i:
            abundant_numbers.append(i)
    return abundant_numbers

def solve():
    limit = 28123
    abundant_numbers = find_abundant_numbers(limit)
    can_be_written_as_sum = [False] * (limit + 1)
    
    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            abundant_sum = abundant_numbers[i] + abundant_numbers[j]
            if abundant_sum <= limit:
                can_be_written_as_sum[abundant_sum] = True
    
    result = sum(i for i in range(1, limit + 1) if not can_be_written_as_sum[i])
    return result

print(solve())
