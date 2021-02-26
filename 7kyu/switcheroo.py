"""
Switcheroo
https://www.codewars.com/kata/57f759bb664021a30300007d/train/python

Given a string made up of letters a, b, and/or c, switch the position of letters a and b (change a to b and vice versa). Leave any incidence of c untouched.

Example:

'acb' --> 'bca'
'aabacbaa' --> 'bbabcabb'
"""
def switcheroo(string):
    result = []
    newlist = [letter for letter in string]
    for i in range(len(newlist)):
        if newlist[i] == 'a':
            result.append('b')
        elif newlist[i] == 'b':
            result.append('a')
        else:
            result.append(newlist[i])
    return "".join(result)
print(switcheroo("abc"))
# bac
print(switcheroo('aaabcccbaaa'))
# bbbacccabbb

# # CODEWAR SOLUTIONS
# def switcheroo(string):
#     return ''.join({'a':'b', 'b':'a'}.get(c, c) for c in string)

# def switcheroo(string):
#     return ''.join( [ 'a' if s=='b' else 'b' if s=='a' else s for s in string ] )

# def switcheroo(s):
#     return s.translate(str.maketrans('ab','ba'))