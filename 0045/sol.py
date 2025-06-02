import math

def T(n):
    return n*(n + 1) // 2

def reverse_P(Pn):
    return (1 + math.sqrt(1 + 24*Pn)) / 6

def reverse_H(Hn):
    return (1 + math.sqrt(1 + 8*Hn)) / 4

ts = [T(n) for n in range(10**6)]

for t in ts:
    if t > 40755:
        if reverse_P(t).is_integer() and reverse_H(t).is_integer():
            print(t)
            break
