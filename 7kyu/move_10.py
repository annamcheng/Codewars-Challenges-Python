"""
Move 10
https://www.codewars.com/kata/57cf50a7eca2603de0000090/train/python

Move every letter in the provided string forward 10 letters through the alphabet.

If it goes past 'z', start again at 'a'.

Input will be a string with length > 0.
"""

def move_ten(st):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    result = []
    for i in range(len(st)):
        if st[i] == abc[i]:
            result.append(abc[i+10])
        else:
            result.append(st[i])
        return "".join(result)
print(move_ten("testcase"))
# docdmkco