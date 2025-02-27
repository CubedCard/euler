import inflect

p = inflect.engine()

def number_to_words(number):
    return p.number_to_words(number)

nums = []
for num in range(1, 1001):
    nums.append(number_to_words(num))

one = ''.join(nums).replace(' ', '').replace('-', '')

print(len(one))
