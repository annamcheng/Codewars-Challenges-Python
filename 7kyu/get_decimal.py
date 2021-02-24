"""
Get Decimal Part of the Given Number
https://www.codewars.com/kata/586e4c61aa0428f04e000069/train/python

Write a function that returns only the decimal part of the given number.

You only have to handle valid numbers, not Infinity, NaN, or similar. Always return a positive decimal part.

Examples
get_decimal(2.4)  # 0.4
get_decimal(-0.2) # 0.2
"""
# math.modf(x) returns a tuple with the fraction and integer parts of x.
# math.modf(1.5) returns (0.5, 1.0)
import math
def get_decimal(n):
    return abs(math.modf(n)[0])

print(get_decimal(10))
print(get_decimal(-1.2))
print(get_decimal(1.99))