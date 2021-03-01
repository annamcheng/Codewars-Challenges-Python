"""
Which String Is Worth More?
https://www.codewars.com/kata/5840586b5225616069000001/train/python

You will be given two ASCII strings, a and b. Your task is write a function to determine which one of these strings is "worth" more, and return it.

A string's worth is determined by the sum of its ASCII codepoint indexes. So, for example, the string HELLO has a value of 372: H is codepoint 72, E 69, L 76, and O is 79. The sum of these values is 372.

In the event of a tie, you should return the first string, i.e. a.
"""
# map() function returns a map object(which is an iterator)
# of the results after applying the given function to each item
# of a given iterable (list, tuple etc.)
# Syntax: map(fun, iter)
# Syntax: sum(iterable)

def highest_value(a,b):
    return a if sum(map(ord, a)) >= sum(map(ord, b)) else b

print(highest_value("AaBbCcXxYyZz0189", "KkLlMmNnOoPp4567"))