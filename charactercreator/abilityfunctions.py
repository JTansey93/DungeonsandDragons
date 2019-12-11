import math
import random

def modifier(a):
    return math.floor((a / 2) - 5)

#This function simulates rolling a six sided dice four times and adding the three highest results together
def abilityRoll():
    roll = []
    for i in range(4):
        roll.append(random.randint(1, 6))
    roll.sort()
    del roll[0]
    return sum(roll)