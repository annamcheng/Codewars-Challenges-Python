"""
Is He Gonna Survive
https://www.codewars.com/kata/59ca8246d751df55cc00014c/train/python

A hero is on his way to the castle to complete his mission. However, he's been told that the castle is surrounded with a couple of powerful dragons! each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.. Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, will he survive?
Return True if yes, False otherwise :)
"""

# Logic: takes 2 bullets to kill 1 dragon. 2:1 ratio
# Ex: Takes 100 bullets to kill 50 dragons
# Test each possibility:
# if bullets % dragon has modulo of 0, return True, hero has enough bullets
# if dragons * 2 is less than or equal to bullets, that is enough bullets to kill dragon
# if bullets == 0 or dragons == 0 or bullets == dragons, return False, nothing to kill
# if bullets == dragons at 1:1, return False; not enough bullets

def hero(bullets, dragons):
    if bullets == 0 or dragons == 0 or bullets == dragons:
        return False
    elif bullets % dragons == 0 or dragons * 2 <= bullets:
        return True
    else:
        return False

hero(100,40)
hero(7, 4)
hero(4, 5)
hero(100, 40)
hero(1500, 751)
hero(0, 1)

# Other solutions
# def hero(bullets, dragons):
#     return bullets >= dragons * 2

# hero = lambda b,d: 2*d<=b