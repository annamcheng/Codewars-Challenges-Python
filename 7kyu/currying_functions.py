"""
Currying functions: multiply all elements in an array
https://www.codewars.com/kata/586909e4c66d18dd1800009b/train/python
To complete this Kata you need to make a function multiplyAll/multiply_all which takes an array of integers as an argument. This function must return another function, which takes a single integer as an argument and returns a new array.

The returned array should consist of each of the elements from the first array multiplied by the integer.

Example:

multiply_all([1, 2, 3])(2); // => [2, 4, 6]
You must not mutate the original array.
"""

def multiply_all(arr):


print(multiply_all([1, 2, 3])(2))