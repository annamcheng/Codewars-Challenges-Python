"""
Square Every Digit
https://www.codewars.com/kata/546e2562b03326a88e000020/train/python

Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
Note: The function accepts an integer and returns an integer
"""

def square_digits(num):
    if num < 10:
        return num**2
    else:
        return int("".join(str(square_digits(num//10)) + str((num % 10) **2)))
               # recursive call square_digits(num//10) + (num%10)**2
                              # square_digits(123)     + 16
                                # square_digits(12)    + 9
                                 # square_digits(1)    + 4
                                   #                   + 1
               # 1 adds to 4, 9, 16 as a string type. String is then converted to int type.

print(square_digits(1234))
# 1234 = 14916

# CODEWARS SOLUTIONS
# def square_digits(num):
#     return int(''.join(str(int(d)**2) for d in str(num)))