"""
Even times last
https://www.codewars.com/kata/5a1a9e5032b8b98477000004/train/python

Given a sequence of integers, return the sum of all the integers that have an even index, multiplied by the integer at the last index.

If the sequence is empty, you should return 0.
"""

def even_last(numbers):
    return 0 if numbers == [] else sum([numbers[i] for i in range(len(numbers)) if i%2==0]) * numbers[-1]

print(even_last([2, 3, 4, 5]))
print(even_last([]))
