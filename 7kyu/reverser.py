"""
Reverser
https://www.codewars.com/kata/search/python?q=recursion&&beta=false

Impliment the reverse function, which takes in input n and reverses it. For instance, reverse(123) should return 321. You should do this without converting the inputted number into a string.

# Please do not use anything from the following list:
['encode','decode','join','zfill','codecs','chr','bytes','ascii',
'substitute','template','bin', 'os','sys','re', '"', "'", 'str','repr', '%s',
'format', 'type', '__', '.keys','eval','exec','subprocess']
"""
def digit_num(x):
    if x < 10:
        return 1
    else:
        return 1+digit_num(x//10)

def reverse(n):
    if n < 10:
        return n
    else:
        return (n%10)*(10 **(digit_num(n)-1)) + reverse(n//10)
print(reverse(1234))
print(reverse(10987))


# CODEWARS SOLUTION
# def reverse(n):
#     m = 0
#     while n > 0:
#         n, m = n // 10, m * 10 + n % 10
#     return m

# def reverse(n, acc = 0):
#     return acc if n == 0 else reverse(n//10, acc*10 + n%10)

# def reverse(n, r=0):
#     return reverse(n // 10, r * 10 + n % 10) if n else r