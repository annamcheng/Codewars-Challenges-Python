"""
Calculate BMI
https://www.codewars.com/kata/57a429e253ba3381850000fb/train/python

Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"
if bmi <= 25.0 return "Normal"
if bmi <= 30.0 return "Overweight"
if bmi > 30 return "Obese"
"""
# save formula of input inside variable bmi_input
# match the respective strings to the conditionals in if/elif/else statement

def bmi(weight, height):
    bmi_input = weight / (height**2)
    if bmi_input <= 18.5:
        print('Underweight')
    elif bmi_input <= 25.0:
        print('Normal')
    elif bmi_input <= 30.0:
        print("Overweight")
    else:
        return "Obese"

bmi(50,1.80) # Underweight
bmi(80, 1.80) # Normal
bmi(90, 1.80) # Overweight
bmi(110, 1.80) # Obese
bmi(50, 1.50) # Normal