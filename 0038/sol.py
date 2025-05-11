def is_pandigital(num_str):
    return sorted(num_str) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def concatenated_product(number, n):
    return ''.join(str(number * i) for i in range(1, n + 1))

def find_largest_pandigital():
    max_pandigital = 0
    for i in range(2, 10000):
        for n in range(2, 10):
            concatenated = concatenated_product(i, n)
            if len(concatenated) > 9:
                break
            if is_pandigital(concatenated):
                max_pandigital = max(max_pandigital, int(concatenated))
    return max_pandigital

print(find_largest_pandigital())
