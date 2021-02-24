"""
Highest and Lowest
https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python

In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Example:

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes:

All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
"""
# map(function, iterable)
# map: function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple, etc)
#     function: a function map passes on each element of given iterable
#     iterable: iterable that is mapped
# Note: You can pass one or more iterable to the map() function

def high_and_low(numbers):
    #split string into list to make iterable
    #interpolate min and max of list_num and convert to integer
    return f"{max([int(num) for num in numbers.split()])} {min([int(num) for num in numbers.split()])}"

print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))

# def high_and_low(numbers): #z.
#     nn = [int(s) for s in numbers.split(" ")]
#     return "%i %i" % (max(nn),min(nn))

# def high_and_low(numbers):
#     n = map(int, numbers.split(' '))
#     return "{} {}".format(max(n), min(n))

# def high_and_low(numbers):
#   return " ".join(x(numbers.split(), key=int) for x in (max, min))