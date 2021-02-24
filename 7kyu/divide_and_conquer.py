"""
Divide and Conquer
https://www.codewars.com/kata/57eaec5608fed543d6000021/train/python

Given a mixed array of number and string representations of integers,
add up the string integers and subtract this from the total of the non-string integers.

Return as a number.
"""
# To check if an item is a specified type, use isinstance()
# Syntax: isinstance(object, type) which will return boolean if object matches type.
# Type can be a tuple of data types

# add total of non-string integers
# subtract string integers from non-str ints

# use sum() function to add all integers inside list
# Syntax: sum(iterable, start); iterable list, tuple, dict.

def div_con(x):
    # your code here
    integer = [num for num in x if isinstance(num, int)]
    str_num = [int(char) for char in x if isinstance(char, str)]
    return sum(integer) - sum(str_num)


print(div_con([9, 3, '7', '3']))
print(div_con(['5', '0', 9, 3, 2, 1, '9', 6, 7]))
print(div_con(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0']))

# CODEWAR SOLUTIONS
# def div_con(lst):
#     return sum(n if isinstance(n, int) else -int(n) for n in lst)