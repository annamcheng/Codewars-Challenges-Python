"""
Reduce My Fraction
https://www.codewars.com/kata/576400f2f716ca816d001614/train/python

Write a function which reduces fractions to their simplest form! Fractions will be presented as an array/tuple (depending on the language), and the reduced fraction must be returned as an array/tuple:

input:   [numerator, denominator]
output:  [newNumerator, newDenominator]
example: [45, 120] --> [3, 8]
All numerators and denominators will be positive integers.

"""
# Python built-in function "greatest common divisor"
# Syntax: gcd(x,y) where x and y are positive integers

import math
def reduce_fraction(fraction):
    num, denom = fraction
    d = math.gcd(num, denom)
    return num//d, denom//d

print(reduce_fraction((60, 20)))
print(reduce_fraction((80, 120)))

print(math.gcd)