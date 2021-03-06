"""
Separate Basic Types
https://www.codewars.com/kata/60113ded99cef9000e309be3/train/python

Given: a sequence of different type of values (number, string, boolean). You should return an object with a separate properties for each of types presented in input. Each property should contain an array of corresponding values.

keep order of values like in input array
if type is not presented in input, no corresponding property are expected
So, for this input:

['a', 1, 2, False, 'b']
expected output is:

{
  int: [1, 2],
  str: ['a', 'b'],
  bool: [False]
}
"""
def separate_types(seq):
    myset = {}
    for x in seq:
        if isinstance(seq, str):
            myset.append(seq)
    return myset
print(separate_types(['a', 1, 2, False, 'b']))