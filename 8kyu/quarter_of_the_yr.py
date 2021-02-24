"""
Quarter of The Year
https://www.codewars.com/kata/5ce9c1000bab0b001134f5af/train/python

Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.
For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.
"""

# break down the months (as numbers) into quarters & save inside variable
# if argument passed in matches number inside quarter, return quarter
def quarter_of(month):
# if month == any number inside quarter, return that quarter
# save breakdown of months and quarters inside dictionary
# quarters = {quarter (keys): month (values)}
    quarters = {1:[1,2,3], 2:[4,5,6], 3:[7,8,9], 4:[10,11,12]}


quarter_of(3)
quarter_of(8)
quarter_of(11)