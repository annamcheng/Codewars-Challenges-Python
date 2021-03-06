"""
Get the integers between two numbers
https://www.codewars.com/kata/598057c8d95a04f33f00004e/train/python

Build a function that can get all the integers between two given numbers.

Example:

(2,9)

Should give you this output back:

[ 3, 4, 5, 6, 7, 8 ]

If start_num is the same as end_num, return an empty sequence.
"""

def function(start_num, end_num):
    return list(range(start_num+1, end_num))

print(function(2,9))
print(function(6,8))