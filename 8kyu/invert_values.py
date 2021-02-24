"""
Invert Values
https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/train/python

Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
You can assume that all values are integers. Do not mutate the input array/list.
"""

# note: if num is positive, multiply by -1
#         if num is negative, multiply by -1
# All integers must by multiplied by -1.
# use list comprehension to print new list with all integers * -1 on expression
def invert(lst):
    print([num * -1 for num in lst])

invert([1, 2, 3, 4, 5])
invert([1, -2, 3, -4, 5])

# CODEWAR SOLUTIONS
# def invert(lst):
#     return [-x for x in lst]

# def invert(lst):
#     return list(map(lambda x: -x, lst));