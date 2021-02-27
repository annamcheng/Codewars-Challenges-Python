"""
Recursion 101
https://www.codewars.com/kata/5b752a42b11814b09c00005d/train/python

You are given two positive integers a and b.

Your task will be to apply the following operations:
i) If a = 0 or b = 0, return [a,b]. Otherwise, go to step (ii);
ii) If a ≥ 2*b, set a = a - 2*b, and repeat step (i). Otherwise, go to step (iii);
iii) If b ≥ 2*a, set b = b - 2*a, and repeat step (i). Otherwise, return [a,b].
a and b will both be lower than 10E8.
"""

def solve(a,b):
    if a == 0 or b == 0:
        return [a,b]
    elif a >= (2 * b):
        a = a - (2 * b)
        solve(a-1, b)
    elif b >= (2 * a):
        b = b - (2 * a)
        solve(a, b-1)
    return [a, b]
print(solve(6,19))
# [6,7]
print(solve(2,1))
#[ 0,1]
print(solve(22,5))
# [0,1]