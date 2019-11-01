#! python3
import random

#This function simulates rolling a six sided dice four times and adding the three highest results together
def abilityRoll():
    roll = []
    for i in range(4):
        roll.append(random.randint(1, 6))
    roll.sort()
    del roll[0]
    return sum(roll)

#Then we get a list of six ability scores by using the abilityRoll function and appending our results in a list
baseAbility = []
for i in range(6):
    baseAbility.append(abilityRoll())

#Lets sort them for convenience as well
baseAbility.sort()

print(*baseAbility, sep = ", ")