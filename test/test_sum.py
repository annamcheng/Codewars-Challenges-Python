a = (1,2,5)
print(round(sum(a)/len(a)))

# list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
print([x for x in fruits if len(x) < 5])

a = 4
b = 10

import math
print(b/a)
print(b//a) # integer divide
print(round(b/a))
print(math.floor(b/a))
print(math.ceil(b/a))