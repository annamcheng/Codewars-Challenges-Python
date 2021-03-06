"""
Convert an array of strings to array of numbers
https://www.codewars.com/kata/5783d8f3202c0e486c001d23/train/python

Some really funny web dev gave you a sequence of numbers from his API response as an sequence of strings!

You need to cast the whole array to the correct type.

Create the function that takes as a parameter a sequence of numbers represented as strings and outputs a sequence of numbers.

ie:["1", "2", "3"] to [1, 2, 3]

Note that you can receive floats as well.
"""

def to_float_array(arr):
    return [(float(x)) for x in arr]


print(to_float_array(["1.1", "2.2", "3.3"]))

# def to_float_array(arr):
#     return list(map(float, arr))