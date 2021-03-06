"""
Numbers to Objects
https://www.codewars.com/kata/57ced2c1c6fdc22123000316/train/python

You will be given an array of numbers.

For each number in the array you will need to create an object.

The object key will be the number, as a string. The value will be the corresponding character code, as a string.

Return an array of the resulting objects.

All inputs will be arrays of numbers. All character codes are valid lower case letters. The input array will not be empty.
"""
# chr() function accepts a single integer and returns ASCII char code
# How do you convert a list into dict? Use dict comprehension
# How do you split a dict into a list of dicts? Use list comprehension

def num_obj(s):
    chars = []
    for num in s:
        chars.append(chr(num))
    mydict = dict(zip(s, chars))
    return [{str(k): v} for (k, v) in mydict.items()]

def num_obj2(s):
    return [{str(num): chr(num)} for num in s]

# print(num_obj([118,117,120]))
# print(num_obj([113,113,113]))
# [{'113': 'q'}, {'113': 'q'}, {'113': 'q'}]

print(num_obj2([113,113,113]))