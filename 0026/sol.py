import re
import decimal

max_digits = 10000

m = (0, 0)

def find_repeating_decimal_cycle(s, max_digits=100):
    if len(s) < 2:
        return None
    decimal_part = s.split('.')[1][:max_digits]
    
    for length in range(1, len(decimal_part)//2 + 1):
        pattern = decimal_part[:length]
        repeated = pattern * (len(decimal_part) // length)
        
        if decimal_part.startswith(repeated):
            return pattern
    return None

decimal.getcontext().prec = max_digits

for x in range(1, 1000):
    s = str(decimal.Decimal(1) / decimal.Decimal(x))
    l = len(str(find_repeating_decimal_cycle(s, max_digits)))
    if l > m[1]:
        m = (x, l)

print(m)
