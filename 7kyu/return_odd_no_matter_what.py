"""
Return Odd No Matter What
https://www.codewars.com/kata/5f882dcc272e7a00287743f5/train/python

Given the integer n return odd numbers as they are, but subtract 1 from even numbers.

Note: Your solution should be 36 or less characters long.
"""
# Question: what is a shorter way to check odd/even numbers?
"""
bitwise 'and' operator if x is odd, x&1 returns true/1
                       if x is even, x&1 returns false/0
                       
If last bit is 1 then number is odd, otherwise always even.                       

 input : 5    // odd
   00000101              
 & 00000001                
--------------                
   00000001       
--------------

input : 8     //even
   00001000              
 & 00000001                 
--------------               
   00000000        
--------------
"""
# Question: Is there a way to return a value without using return keyword?
# Use lambda AKA "anonymous function"
# Syntax: function_name = lambda argument:expression if condition else False
always_odd=lambda n:n if n&1else n-1
# refactor code: always_odd=lambda n: n-1-(n&1)
print(always_odd(2), 1)
print(always_odd(8), 7)

#CODEWARS SOLUTION
# always_odd=lambda n:n-(n%2==0)
# def always_odd(n): return n-(1-n%2)
# def always_odd(n):return n-(not n%2)
# always_odd=lambda n:n-1|1
# always_odd=lambda n:n-~n%2
# always_odd=lambda _:[_-1,_][_%2]
# always_odd=lambda n:n-(n&1<1)

num = lambda x: x&1
print(bool(num(3)))