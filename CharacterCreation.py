#! python3
#A character creation tool for DnD 5E which takes input from the user with regards to race, class and background and outputs a usable character sheet

import random
import math
import csv

racialbonuses = {'Dragonborn':[2,0,0,0,0,1],
'Dwarf':[0,0,2,0,0,0],
'Elf':[0,2,0,0,0,0],
'Gnome':[0,0,0,2,0,0],
'Half-Elf':[0,0,0,0,0,2],
'Half-Orc':[2,0,1,0,0,0],
'Halfling':[0,2,0,0,0,0],
'Human':[1,1,1,1,1,1],
'Tiefling':[0,0,0,1,0,2]}

#We're going to make a class with all the propertires one would expect of a Dnd 5E character
class PlayerCharacter:
    Name = ""
    Race = ""
    CharClass = ""
    Background = ""

RaceList = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Half-Orc", "Halfling", "Human", "Tiefling"]
CharClassList = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorceror", "Warlock", "Wizard"]
BackgroundList = ["Acolyte", "Charlatan", "Criminal/Spy", "Entertainer", "Folk Hero", "Gladiator", "Guild Artisan", "Hermit", "Knight", "Noble", "Outlander", "Pirate", "Sage", "Sailor", "Soldier", "Urchin"]

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

#Same thing for character class
print("Now Enter a numeric character corresponding to your chosen class:")
for i in range(len(CharClassList)):
    print((i+1), ": ", CharClassList[i])

PlayerClass = input()

NewCharacter.CharClass = CharClassList[int(PlayerClass) - 1]

#Background
print("Now Enter a numeric character corresponding to your chosen background:")
for i in range(len(BackgroundList)):
    print((i+1), ": ", BackgroundList[i])

PlayerBackground = input()

NewCharacter.Background = BackgroundList[int(PlayerBackground) - 1]

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

#Now we print them and ask the user to assign them to each of the six abilities
print("We have generated a list of ability scores for you:")

for i in range(len(baseAbility)):
    print(baseAbility[i], sep=", ")

abilities = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

finalscore = {}

for i in range(len(abilities)):
    while True:
      print("What score would you like to assign to ", abilities[i], "?")
      answer = input()
      if int(answer) not in baseAbility:
          print("Please enter a value from the list given (You cannot enter duplicate values)")
      else:
          finalscore[abilities[i]] = int(answer)
          for i in range(len(baseAbility)):
              if baseAbility[i] == int(answer):
                  baseAbility.remove(int(answer))
                  break
          break

#This modifies the characters ability scores according to their racial bonuses
for k in racialbonuses.keys():
    if k == NewCharacter.Race:
        race = k
        for k in finalscore.keys():
            for i in range(len(abilities)):
                if abilities[i] == k:
                    finalscore[k] = finalscore[k] + racialbonuses[race][i]

#This turns the ability scores into ability modifiers
def modifier(a):
    return math.floor((a / 2) - 5)

print("Name: ", NewCharacter.Name,
       "\nRace: ", NewCharacter.Race,
       "\nClass: ", NewCharacter.CharClass,
       "\nBackround: ", NewCharacter.Background,
       "\nInitiative: ", modifier(finalscore['Dexterity']),
       "\nArmour Class: ", (10 + modifier(finalscore['Dexterity'])))

for k, v in finalscore.items():
    print(k, ": ", v, modifier(v))