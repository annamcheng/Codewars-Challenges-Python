"""
Elevator Distance
https://www.codewars.com/kata/59f061773e532d0c87000d16/train/python

Imagine you start on the 5th floor of a building, then travel down to the 2nd floor, then back up to the 8th floor. You have travelled a total of 3 + 6 = 9 floors of distance.

Given an array representing a series of floors you must reach by elevator, return an integer representing the total distance travelled for visiting each floor in the array in order.

// simple examples
elevatorDistance([5,2,8]) = 9
elevatorDistance([1,2,3]) = 2
elevatorDistance([7,1,7,1]) = 18

// if two consecutive floors are the same,
//distance travelled between them is 0
elevatorDistance([3,3]) = 0
Array will always contain at least 2 floors. Random tests will contain 2-20 elements in array, and floor values between 0 and 30.
"""
# start on 5th fl - (3fls) travel down to 2nd + (6 fl) go back to 8th
# 3+6 = 9

def elevator_distance(*args):


print(elevator_distance([5,2,8]))