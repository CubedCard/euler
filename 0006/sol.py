nums = [x + 1 for x in range(100)]
squares_sum = sum([x**2 for x in nums])
sum_square = sum(nums)**2

print(abs(squares_sum - sum_square))
