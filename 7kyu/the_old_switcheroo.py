"""
The Old Switcheroo
https://www.codewars.com/kata/55d410c492e6ed767000004f/train/python

Write a function vowel_2_index
that takes in a string and replaces all the vowels [a,e,i,o,u] with their respective positions within that string.
E.g:

vowel_2_index('this is my string') == 'th3s 6s my str15ng'
vowel_2_index('Codewars is the best site in the world') == 'C2d4w6rs 10s th15 b18st s23t25 27n th32 w35rld'
vowel_2_index('') == ''

Your function should be case insensitive to the vowels.
"""

"""
enumerate() function assigns an index to each item in an iterable object that can be used to reference
the item later
Syntax: enumerate(iterable, start=0)
"""

"""
index() function searched for a given element from start of LIST and returns the lowest index where element appears
Syntax: list_name.index(element, start, end)
        element - element whose lowest index will be returned
        start (optional) - position where search begins
        end (optional) - position where search ends
"""

def vowel_2_index(string):
    result = []
    for index in range(len(string)):
        if string[index] in 'aeiouAEIOU':
            result.append(str(index+1))
        else:
            result.append(string[index])
    return ''.join(result)

print(vowel('this is my string'))

# CODEWARS SOLUTIONS
# def vowel_2_index(string):
#     vowels = 'aeiouAEIOU'
#     return ''.join(x if x not in vowels else str(n + 1) for n,x in enumerate(string))

# import re
# def vowel_2_index(string):
#     return re.sub("[aeiou]",lambda m:str(m.end()),string,0,re.I)