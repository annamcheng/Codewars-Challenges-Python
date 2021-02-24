"""
Rearrange Number to Get Its Maximum
https://www.codewars.com/kata/563700da1ac8be8f1e0000dc/train/python

Create function that takes one positive three digit integer and rearranges its digits to get maximum possible number. Assume that argument is integer. Return null (nil for ruby) if argument is not valid.

maxRedigit(123); // returns 321
"""
# ** NOTE **
# list has sort() and sorted() method. They perform the same, difference is sort() method doesn't return any value and changes the original list
def max_redigit(num):
    if num <= 99 or num >= 1000:
        return None
    # data type passed in is integer
    # convert integer to string of numbers into list
    list_num = [int(x) for x in str(num)]
    # use sort() to sort a list.
    # Syntax: list.sort(reverse=True, key=myFunc)
    # default takes no params; optional param: reverse=True; key=function that serves as a key for the sort comparison
    list_num.sort(reverse=True)
    # convert list back into str to use .join() and convert back to integer
    # .join() method takes all items in an ITERABLE and joins into a string
    # Syntax: "".join(iterable)
    new_list = [str(y) for y in list_num]
    result = int("".join(new_list))
    # make sure data type of result is integer
    # print(type(result))
    return result

print(max_redigit(123))
print(max_redigit(99))
print(max_redigit(1000))

# CODEWARS SOLUTIONS
# def max_redigit(num):
#     return int(''.join(sorted(str(num))[::-1])) if 99 < num <1000 else None

# def max_redigit(num):
#     if isinstance(num, int) and 99 < num < 1000:
#         return int("".join(sorted(str(num), reverse=True)))