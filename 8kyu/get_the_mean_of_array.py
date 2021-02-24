"""
https://www.codewars.com/kata/563e320cee5dddcf77000158/train/python
Get the mean of an array

It's the academic year's end, fateful moment of your school report. The averages must be calculated. All the students come to you and entreat you to calculate their average for them. Easy ! You just need to write a script.
Return the average of the given array rounded down to its nearest integer.
The array will never be empty.
"""

import math
def get_average(marks):
#     raise NotImplementedError("TODO: get_average")
    result = sum([x for x in marks])/len(marks)
    return math.floor(result)

print(get_average(1, 5, 87, 45, 8, 8))
# how to use dynamic arguments in function *arg **kwarg
# get average
# round down to nearest integer

# normal argument AKA "positional argument" (ie: print())

# NOTE: Diff b/w function v. method
# function is standalone
# method is same as function but is called method when it is binded with a class

#round(number, digits): returns a floating point number that is a rounded version of the specified # with specified # of decimals
# (number is required, digits is optional; default is 0)
#math.floor rounds down to nearest integer
#math.ceil rounds up to its nearest integer

# OTHER SOLUTIONS:
# def get_average(marks):
#     return sum(marks) // len(marks)

# import numpy
# def get_average(marks):
#     return int(numpy.mean(marks))
