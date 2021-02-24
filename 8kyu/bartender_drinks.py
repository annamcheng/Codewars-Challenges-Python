"""
Bartender, drinks!
https://www.codewars.com/kata/568dc014440f03b13900001d/train/python
Complete the function that receives as input a string, and produces outputs according to the following table:

Input	Output
"Jabroni"	"Patron Tequila"
"School Counselor"	"Anything with Alcohol"
"Programmer"	"Hipster Craft Beer"
"Bike Gang Member"	"Moonshine"
"Politician"	"Your tax dollars"
"Rapper"	"Cristal"
anything else	"Beer"
Note: anything else is the default case: if the input to the function is not any of the values in the table, then the return value should be "Beer".

Make sure you cover the cases where certain words do not show up with correct capitalization. For example, the input "pOLitiCIaN" should still return "Your tax dollars".
"""

# make string that is passed in all lowercase
# return the matching value
# Python does not have switch statement function

def get_drink_by_profession(param):
    # code me!
    if param.lower() == 'jabroni':
        return'Patron Tequila'
    elif param.lower() == 'school counselor':
        return 'Anything with Alcohol'
    elif param.lower() == 'programmer':
        return 'Hipster Craft Beer'
    elif param.lower() == 'bike gang member':
        return 'Moonshine'
    elif param.lower() == 'politician':
        return 'Your tax dollars'
    elif param.lower() == 'rapper':
        return 'Cristal'
    else:
        return 'Beer'

def get_drink2(param):
    name = {'jabroni':'Patron Tequila', 'school counselor':'Anything with Alcohol', 'programmer':'Hipster Craft Beer', 'bike gang member':'Moonshine', 'politician':'Your tax dollars', 'rapper':'Cristal'}
    param = param.lower()
    return name[param] if param in name else 'Beer'

# get_drink_by_profession("jabrOni")
# # get_drink_by_profession("scHOOl counselor")
# # get_drink_by_profession("prOgramMer")
# # get_drink_by_profession("bike ganG member")
# # get_drink_by_profession("Pug")

print(get_drink2("jabrOni"))

