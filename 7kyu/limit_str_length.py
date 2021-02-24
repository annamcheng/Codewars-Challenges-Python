"""
Limit String Length -1
https://www.codewars.com/kata/5208fc3cb613bc725f000142/train/python
The function must return the truncated version of the given string up to the given limit followed by "..." if the result is shorter than the original. Return the same string if nothing was truncated.

"""
# use string slicing to return the string up to the limit number passed in.
# Syntax: string[start:stop:step]

# def solution(st, limit):
#     if len(st) > limit:
#         return st[:limit] + '...'
#     else:
#         return st

def solution(st, limit):
    return st[:limit] + '...' if len(st) > limit else st

print(solution('Testing String',3))
print(solution('Testing String',8))
print(solution('Test', 4))
print(solution('Test', 10))