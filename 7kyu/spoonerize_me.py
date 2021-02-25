"""
Spoonerize Me
https://www.codewars.com/kata/56b8903933dbe5831e000c76/train/python

A spoonerism is a spoken phrase in which the first letters of two of the words are swapped around, often with amusing results.
In its most basic form a spoonerism is a two word phrase in which only the first letters of each word are swapped:
"not picking" --> "pot nicking"
Your task is to create a function that takes a string of two words, separated by a space: words and returns a spoonerism of those words in a string, as in the above example.
NOTE: All input strings will contain only two words. Spoonerisms can be more complex. For example, three-word phrases in which the first letters of the first and last words are swapped: "pack of lies" --> "lack of pies" or more than one letter from a word is swapped: "flat battery --> "bat flattery" You are NOT expected to account for these, or any other nuances involved in spoonerisms.
"""

# split the string
# grab the first character of the second string + the first word starting at 1st index using index slicing
# grab the first character of the first string + the second word starting at 1st index
def spoonerize(words):
    newlist = [x for x in words.split()]
    return f"{newlist[1][:1] + newlist[0][1:]} {newlist[0][:1] + newlist[1][1:]}"

print(spoonerize("nit picking"))
print(spoonerize("wedding bells"))
print(spoonerize("jelly beans"))
print(spoonerize("pop corn"))
print(spoonerize('rwxb gccdwkkzsj'))

