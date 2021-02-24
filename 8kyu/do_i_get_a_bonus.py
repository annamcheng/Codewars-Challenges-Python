"""
Do I Get A Bonus?
https://www.codewars.com/kata/56f6ad906b88de513f000d96/train/python

It's bonus time in the big city! The fatcats are rubbing their paws in anticipation... but who is going to make the most money?
Build a function that takes in two arguments (salary, bonus). Salary will be an integer, and bonus a boolean.
If bonus is true, the salary should be multiplied by 10. If bonus is false, the fatcat did not make enough money and must receive only his stated salary.
Return the total figure the individual will receive as a string prefixed with "£" (= "\u00A3", JS, Go, Java and Julia), "$" (C#, C++, Ruby, Clojure, Elixir, PHP, Python, Haskell and Lua) or "¥" (Rust).
"""

# how to return strings in Python? .format() or f-string
# Syntax for .format: "String here {}".format("insert string")
# Syntax for f-string: (f"String{variable}") introduced in Python 3.6; AKA Literal String
# https://www.w3schools.com/python/python_string_formatting.asp

def bonus_time(salary, bonus):
    #your code here
    if bonus:
        return "${}".format(salary*10)
    else:
        return f"${salary}"

bonus_time(10000, True)
bonus_time(25000, True)
bonus_time(10000, False)
bonus_time(60000, False)