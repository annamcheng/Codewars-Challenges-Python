"""
Recursive Replication
https://www.codewars.com/kata/57547f9182655569ab0008c4/train/python

You need to design a recursive function called replicate which will receive arguments times and number.
The function should return an array containing repetitions of the number argument.
For instance, replicate(3, 5) should return [5,5,5].
If the times argument is negative,return an empty array.

As tempting as it may seem, do not use loops to solve this problem.
"""
# # FOR LOOP SOLUTION
# def replicate(times, number):
#     result = []
#     if times < 0:
#         return []
#     else:
#         for i in range(times):
#             result.append(number)
#     return result

# RECURSION SOLUTION
def replicate2(times, number):
    if times <= 0:
        return []
    else:
        return [number] + replicate2(times-1, number)
               # 5      + rep2(2, 5)
                        # 5      + rep2(1, 5)
                                 # 5 + rep2(0,5)
# print(replicate(3,5))
# # [5,5,5]
# print(replicate(-1,12))
# # []

print(replicate2(5,1))
# [1, 1, 1, 1, 1]
print(replicate2(3,5))