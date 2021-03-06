"""
Remove Unnecessary Characters from Items in List
https://www.codewars.com/kata/586d12f0aa042830910001d1/train/python

You've been given a list that states the daily revenue for each day of the week. Unfortunately, the list has been corrupted and contains extraneous characters. Rather than fix the source of the problem, your boss has asked you to create a program that removes any unneccessary characters and return the corrected list.

The expected characters are digits, ' $ ', and ' . ' All items in the returned list are expected to be strings.

For example:

a1 = ['$5.$6.6x.s4', '{$33ae.5(9', '$29..4e9', '%.$9|4d20', 'A$AA$4r R4.94']
remove_char(a1)
['$56.64', '$33.59', '$29.49', '$94.20', '$44.94']
"""

import re
def remove_char(array):
    result = []
    for i in range(len(array)):
        x = re.findall(r"\$\d+", array[i])
        result.append(x)
    return result
print(remove_char(['$5.$6.6x.s4', '{$33ae.5(9', '$29..4e9', '%.$9|4d20', 'A$AA$4r R4.94']))
#['$56.64', '$33.59', '$29.49', '$94.20', '$44.94']
