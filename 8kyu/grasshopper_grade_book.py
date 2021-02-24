"""
Grasshopper- Grade book
https://www.codewars.com/kata/55cbd4ba903825f7970000f5/train/python

Complete the function so that it finds the mean of the three scores passed to it and returns the letter value associated with that grade.

Numerical Score	Letter Grade
90 <= score <= 100	'A'
80 <= score < 90	'B'
70 <= score < 80	'C'
60 <= score < 70	'D'
0 <= score < 60	'F'
Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.
"""

#round takes a number, required and an optional second argument digits/decimals to return
#round(number, digits)

#mean() functoion is used to calculate mean/avg from a LIST of numbers
import statistics
def get_grade(s1, s2, s3):
    # Code here
    # first solution using round
    # score = round((s1 + s2 + s3)/3,2)

    #second solution using mean() from statistics
    score_list = [s1,s2,s3]
    score = statistics.mean(score_list)
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'

def get_grade2(s1,s2,s3):
    score_list = [s1,s2,s3]
    score = statistics.mean(score_list)
    return 'A' if 90 <= score <= 100 else 'B' if 80 <= score < 90 else 'C' if 70 <= score < 80 else 'D' if 60 <= score < 70 else 'F'

print(get_grade(95, 90, 93)) #A
print(get_grade(100, 85, 96)) #A

print(get_grade2(95, 90, 93)) #A
print(get_grade2(100, 85, 96)) #A

# CODEWAR SOLUTIONS
# def get_grade(s1, s2, s3):
#     return {6:'D', 7:'C', 8:'B', 9:'A', 10:'A'}.get((s1 + s2 + s3) / 30, 'F')
# The get() method returns the value of the item with the specified key from a dictionary
# keyname is required; value is optionl
# Syntax: dictionary.get(key, value)

# def get_grade(*s):
#     return 'FFFFFFDCBAA'[sum(s)//30]

# def get_grade(*args):
#     mean = sum(args) / len(args)
#     return scores.get(mean // 10, 'F')