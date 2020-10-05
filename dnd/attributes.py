# Matt Colville rolling method
# 1. Roll 4d6, frop the lowest value die for 1 stat
# 2. If the roll is lower than 8, reroll it
# 3. Repeat steps 1-2 until you have set of 6 stats
# 4. If there are not at least 2 values of 15 or higher, start over.

import random

def roll():
    return random.randint(1,6)

def roll_attribute():
    while True:
        rolls = []
        for _ in range(4):
            rolls.append(roll())
        rolls.remove(min(rolls))
        value = sum(rolls)
        if value >= 8:
            return value

def roll_all_attributes():
    attributes = []
    for _ in range(6):
        attributes.append(roll_attribute())
    return attributes

def has_high_attributes(attributes):
    if attributes[-1] < 15 or attributes[-2] < 15:
        return False
    return True

def roll_attribtues():
    attributes = roll_all_attributes()
    while not has_high_attributes(attributes):
        attributes = roll_all_attributes()
    return attributes

print('Attributes: %s' % roll_attribtues())
