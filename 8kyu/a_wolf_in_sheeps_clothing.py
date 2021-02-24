"""
A Wolf In Sheep's Clothing
https://www.codewars.com/kata/5c8bfa44b9d1192e1ebd3d15/train/python

Wolves have been reintroduced to Great Britain. You are a sheep farmer, and are now plagued by wolves which pretend to be sheep. Fortunately, you are good at spotting them.
Warn the sheep in front of the wolf that it is about to be eaten. Remember that you are standing at the front of the queue which is at the end of the array:

[sheep, sheep, sheep, sheep, sheep, wolf, sheep, sheep]      (YOU ARE HERE AT THE FRONT OF THE QUEUE)
   7      6      5      4      3            2      1

If the wolf is the closest animal to you, return "Pls go away and stop eating my sheep". Otherwise, return "Oi! Sheep number N! You are about to be eaten by a wolf!" where N is the sheep's position in the queue.
Note: there will always be exactly one wolf in the array.
"""

# https://www.w3schools.com/python/ref_keyword_pass.asp
# https://www.geeksforgeeks.org/difference-between-keyword-and-identifier/
# https://www.w3schools.com/python/python_ref_keywords.asp
# pass statement: used as a placeholder for future code; null statement that does nothing
#                  avoid getting an error when empty code is not allowed
# EMPTY CODE NOT ALLOWED: loops, functions, definitions, class definitions, or in if statements
# What is the difference between keyword v. statement?
# Keyword = predefined reserved word that have specific meanings and purposes to the interpreter and cannot get used anywhere else
# Identifiers = values used to define diff. programming items such as variables, integers, structures, union and others
# Statement = a command that program should execute//specifies an action to be performed

# need to know the index of wolf
# if wolf is at end of list (len-1), return "Pls go away..."
# if wold is near a sheep, return index
# use reverse indexing...or reverse list
# reverse() happens in place/doesnt return any value; Updates existing list

# how do you get the index of an element in a list?
# https://www.programiz.com/python-programming/methods/list/index
# list.index(element, start, end) //takes in an element
# index() method only returns the first occurrence of the matching element
def warn_the_sheep(queue):
    # queue.reverse()
    # print(queue)
    for animal in queue:
            pass
        print([animal.index('wolf') for animal in queue if animal == 'wolf'])


warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']) #oi! sleep number N