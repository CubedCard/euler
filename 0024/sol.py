from itertools import permutations

digits = [x for x in range(10)]

for i, perm in enumerate(permutations(digits)):
    if i == 10**6 - 1:
        print(''.join([str(x) for x in perm]))
