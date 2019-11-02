#! python3
#A character creation tool for DnD 5E which takes input from the user with regards to race, class and background and outputs a usable character sheet

import random

#We're going to make a class with all the propertires one would expect of a Dnd 5E character
class PlayerCharacter:
    Name = ""
    Race = ""
    CharClass = ""

RaceList = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Half-Orc", "Halfling", "Human", "Tiefling"]

#Then create an instance of this class to add all our new players information to
NewCharacter = PlayerCharacter()

#We'll start with the obvious step of asking them for their name
print("Hello, and welcome to this character creation program for DnD 5E, please start by entering your character's name:")
NewCharacter.Name = input()

print("Now Enter a numeric character corresponding to your chosen race:")
for i in range(len(RaceList)):
    print((i+1), ": ", RaceList[i])

PlayerRace = input()

NewCharacter.Race = RaceList[int(PlayerRace) - 1]

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

for i in range(len(baseAbility)):
    print(baseAbility[i])

print("Name: ", NewCharacter.Name,
       "Race: ", NewCharacter.Race)