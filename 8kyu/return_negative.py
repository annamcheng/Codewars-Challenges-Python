"""
Return Negative
https://www.codewars.com/kata/55685cd7ad70877c23000102/train/python
In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

Example:

make_negative(1);  # return -1
make_negative(-5); # return -5
make_negative(0);  # return 0

Notes:
The number can be negative already, in which case no change is required.
Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.
"""

# edge case: if number is 0, return 0 as -0 is considered falsy
# a number is positive if > 0 and negative if < 0
# make a positive number negative by multiply by -1

def make_negative( number ):
    # ...
    if number == 0:
        return 0
    elif number > 0:
        return number * -1
    else:
        return number

make_negative(42)
make_negative(-9)
make_negative(0)

