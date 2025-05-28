import itertools
from math import sqrt

def pandigital_numbers(n):
    digits = ''.join(str(i) for i in range(0, n + 1))
    return [int(''.join(p)) for p in itertools.permutations(digits)]

def find_interesting():
    interesting = []
    nums = pandigital_numbers(9)
    for num in nums:
        if int(str(num)[1:4]) % 2 == 0 and int(str(num)[2:5]) % 3 == 0 and int(str(num)[3:6]) % 5 == 0 and int(str(num)[4:7]) % 7 == 0 and int(str(num)[5:8]) % 11 == 0 and int(str(num)[6:9]) % 13 == 0 and int(str(num)[7:10]) % 17 == 0:
            interesting.append(num)
    return interesting

print(sum(find_interesting()))
