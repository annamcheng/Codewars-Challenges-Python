"""
Char Code Calculation
https://www.codewars.com/kata/57f75cc397d62fc93d000059/train/python

Given a string, turn each character into its ASCII character code and join them together to create a number - let's call this number total1:

'ABC' --> 'A' = 65, 'B' = 66, 'C' = 67 --> 656667
Then replace any incidence of the number 7 with the number 1, and call this number 'total2':

total1 = 656667
              ^
total2 = 656661
              ^
Then return the difference between the sum of the digits in total1 and total2:

  (6 + 5 + 6 + 6 + 6 + 7)
- (6 + 5 + 6 + 6 + 6 + 1)
-------------------------
                       6
"""

# put ASCII into dict
# iterate through string and add each letters(key) value to an integer/save in variable total1
# save num of total1 and replace any #7 to 1.
# Subtract sum of total1 - sum of total2
def calc(x):
    # your code here
    mydict = {'A': 65, 'B': 66, 'C':67, 'D': 68, 'E': 69, 'F':70, 'G': 71, 'H':72, 'I': 73, 'J': 74, 'K':75, 'L': 76, 'M':77, 'N':78, 'O':79, 'P': 80, 'Q':81, 'R': 82, 'S': 83, 'T': 84, 'U': 85, 'V': 86, 'W': 87, 'X':88, 'Y':89, 'Z': 90, 'a': 97, 'b':98, 'c':99, 'd':100, 'e':101, 'f':102, 'g':103, 'h':104, 'i': 105, 'j':106, 'k':107, 'l':108, 'm':109, 'n':110, 'o':111, 'p':112, 'q':113, 'r':114, 's':115, 't':116, 'u':117, 'v':118, 'w':119, 'x':120, 'y':121, 'z':122 }
    total1 = []
    total2 = []
    # if letter is in list(x), append value in mydict to first variable
    for key, value in mydict.items():
        for letter in x:
            if letter == key:
                # print(letter)
                total1.append(str(value))
                # print(value)
    total1 = ''.join(total1)
    # print(total1)

    # if any num in total1 == 7, replace number to 7 and append second variable
    for index in range(len(total1)):
        if total1[index] in '7':
            total2.append(str(1))
        else:
            total2.append(total1[index])
    # use map() to return new object of integers
    # Syntax: map(function, iterable)
    # map object can be passed to sum() function
    return sum(map(int,total1)) - sum(map(int,total2))

print(calc('ABC'))
# equals to 6
print(calc('aaaaaddddr'))
# equals to 30
print(calc('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
# equals to 96

# CODEWAR SOLUTION
# ord() function accepts a string of unit length as an argument and returns the Unicode equivalence of the passed argument
# def calc(s):
#     total1 = ''.join(map(lambda c: str(ord(c)), s))
#     total2 = total1.replace('7', '1')
#     return sum(map(int, total1)) - sum(map(int, total2))

# def calc(x):
#     return ''.join(str(ord(ch)) for ch in x).count('7') * 6