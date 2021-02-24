"""
Double Sort
https://www.codewars.com/kata/57cc79ec484cf991c900018d/train/python

Simple enough this one - you will be given an array. The values in the array will either be numbers or strings, or a mix of both. You will not get an empty array, nor a sparse one.

Your job is to return a single array that has first the numbers sorted in ascending order, followed by the strings sorted in alphabetic order. The values must maintain their original type.

Note that numbers written as strings are strings and must be sorted with the other strings
"""

# use isinstance(object, type) within list comprehension to separate string and number
# sort the separate lists
# add the two lists back together with add operator
def db_sort(arr):
    return sorted([num for num in arr if isinstance(num, int)]) + sorted([word for word in arr if isinstance(word, str)])

print(db_sort(["Banana", "Orange", "Apple", "Mango", 0, 2, 2]))
print(db_sort(["Apple",46,"287",574,"Peach","3","69",78,"Grape","423"]))
