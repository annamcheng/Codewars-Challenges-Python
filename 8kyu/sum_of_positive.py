"""
Sum of Positive
https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python

You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.
"""

# use built in sum() function to add all numbers inside of list
# Syntax: sum(iterable, start)
# iterable (list, tuple, dict)
# start (optional): This value is added to sum of iterable items. The default value of start is 0 (if ommitted)
# use list comprehension to create new list of only positive numbers
def positive_sum(arr):
    # Your code here
    return sum([x for x in arr if x >= 0])

positive_sum([1,2,3,4,5])
positive_sum([1,-2,3,4,5])
positive_sum([-1,2,3,4,-5])

#CODEWAR SOLUTIONS
# def positive_sum(arr):
#     return sum(filter(lambda x: x > 0,arr))

# def positive_sum(arr):
#     return sum( max(i, 0) for i in arr )

# positive_sum = lambda a: sum(e for e in a if e > 0)