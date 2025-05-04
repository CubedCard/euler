def isPalindrome(s):
    return s == s[::-1]

palindromes = [x for x in range(1, 10**6) if isPalindrome(str(x))]

total = sum([p for p in palindromes if isPalindrome(str(bin(p)[2:]))])

print(total)
