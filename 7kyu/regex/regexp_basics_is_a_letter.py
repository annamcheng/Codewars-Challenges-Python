"""
Regexp Basics - is it a letter?
https://www.codewars.com/kata/567de72e8b3621b3c300000b/solutions
Complete the code which should return true if the given object is
a single ASCII letter (lower or upper case), false otherwise.
"""
# re.fullmatch(pattern, string, flags=0)
# If the whole string matches the regular expression pattern,
# return a corresponding match object. Return None if the
# string does not match the pattern;
# note that this is different from a zero-length match.

# The bool() function returns the boolean value of a specified object.
# The object will always return True, unless:
# The object is empty, like [], (), {}
# The object is False
# The object is 0
# The object is None

import re
def is_letter(s):
    return bool(re.fullmatch("[A-Za-z]",s))

print(is_letter(""))
#false
print(is_letter("a"))
#true
print(is_letter("X"))
#true