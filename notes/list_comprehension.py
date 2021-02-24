# LIST COMPREHENSION
# Syntax: [expression for item in iterable if condition == True]
num = [1,2,3,4,5]
newlist = []
for x in num:
    if x < 3:
        newlist.append(x)
print(newlist) # [1,2]

print([x for x in num if x < 3]) # [1,2]
