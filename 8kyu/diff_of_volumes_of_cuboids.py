"""
Difference of Volumes of Cuboids
https://www.codewars.com/kata/58cb43f4256836ed95000f97/train/python

In this simple exercise, you will create a program that will take two lists of integers, a and b. Each list will consist of 3 positive integers above 0, representing the dimensions of cuboids a and b. You must find the difference of the cuboids' volumes regardless of which is bigger.

For example, if the parameters passed are ([2, 2, 3], [5, 4, 1]), the volume of a is 12 and the volume of b is 20. Therefore, the function should return 8.
Your function will be tested with pre-made examples as well as random ones.
"""
# volume - width*height*length
# question - how do you get an index of an element?
#          - how do you loop through the list without hard coding index?
def find_difference(a, b):
    # Your code here!
    first = a[0]*a[1]*a[2]
    second = b[0]*b[1]*b[2]
    sum = (first) - (second)
    if sum <= 0:
        return sum * -1
    else:
        return sum
find_difference([3, -2, 5], [1, 4, 4])

# other solutions:
# def find_difference(a, b):
#     return abs(prod(a) - prod(b))
# https://www.geeksforgeeks.org/abs-in-python/
# abs(num) takes in one argument and returns the absolute value of a number

#from numpy import prod
# prod() multiplies every element inside list