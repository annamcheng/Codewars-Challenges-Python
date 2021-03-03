"""
Array Deep Count
https://www.codewars.com/kata/596f72bbe7cd7296d1000029/train/python

len(a) will give you the number of top-level elements in the list/array named a.

Your task is to create a function deepCount that returns the number of ALL elements within an array, including any within inner-level arrays.

For example:
deepCount([1, 2, 3]);
//>>>>> 3
deepCount(["x", "y", ["z"]]);
//>>>>> 4
deepCount([1, 2, [3, 4, [5]]]);
//>>>>> 7
The input will always be an array.

"""
# Python extend() method adds all elements of iterable to end of list
# Syntax: list.extend(iterable)

def deep_count(a):
    lst = []
    if not a:
        return 0
    else:
        for el in a:
            if isinstance(el, list):
                lst.extend(deep_count(el))
            else:
                lst.append(el)
        return len(lst)

print(deep_count([]))
# # 0
print(deep_count([1, 2, 3]))
# # 3
print(deep_count(["x", "y", ["z"]]))
# 4
print(deep_count([1, 2, [3, 4, [5]]]))
# 7
# print(deep_count([[[[[[[[[]]]]]]]]]))
# 8