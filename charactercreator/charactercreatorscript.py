#! python3
#A character creation tool for DnD 5E which takes input from the user with regards to race, class and background and outputs a usable character sheet

import os
import sys
sys.path.insert(0, os.path.abspath('C:\\Users\\jmsta\\OneDrive\\Documents\\Github\\DungeonsandDragons'))

import charactercreator.abilityfunctions as ability

racialbonuses = {'Dragonborn':[2,0,0,0,0,1],
'Dwarf':[0,0,2,0,0,0],
'Elf':[0,2,0,0,0,0],
'Gnome':[0,0,0,2,0,0],
'Half-Elf':[0,0,0,0,0,2],
'Half-Orc':[2,0,1,0,0,0],
'Halfling':[0,2,0,0,0,0],
'Human':[1,1,1,1,1,1],
'Tiefling':[0,0,0,1,0,2]}

raceList = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Half-Orc", "Halfling", "Human", "Tiefling"]
charClassList = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorceror", "Warlock", "Wizard"]
backgroundList = ["Acolyte", "Charlatan", "Criminal/Spy", "Entertainer", "Folk Hero", "Gladiator", "Guild Artisan", "Hermit", "Knight", "Noble", "Outlander", "Pirate", "Sage", "Sailor", "Soldier", "Urchin"]

#We're going to make a class with all the propertires one would expect of a Dnd 5E character
class PlayerCharacter:
    Name = ""
    Race = ""
    CharClass = ""
    Background = ""

#Then create an instance of this class to add all our new players information to
NewCharacter = PlayerCharacter()

#We'll start with the obvious step of asking them for their name
print("Hello, and welcome to this character creation program for DnD 5E, please start by entering your character's name:")
NewCharacter.Name = input()

def userinput(array):
    for index, value in enumerate(array):
        print((index + 1), ": ", value)
    playervariable = input()
    return array[int(playervariable) - 1]

print("Now Enter a numeric character corresponding to your chosen race:")
NewCharacter.Race = userinput(raceList)

print("Now Enter a numeric character corresponding to your chosen class:")
NewCharacter.CharClass = userinput(charClassList)

print("Now Enter a numeric character corresponding to your chosen background:")
NewCharacter.Background = userinput(backgroundList)

#Then we get a list of six ability scores by using the abilityRoll function and appending our results in a list
baseAbility = []
for i in range(6):
    baseAbility.append(ability.abilityRoll())

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

print("Name: ", NewCharacter.Name,
       "\nRace: ", NewCharacter.Race,
       "\nClass: ", NewCharacter.CharClass,
       "\nBackround: ", NewCharacter.Background,
       "\nInitiative: ", ability.modifier(finalscore['Dexterity']),
       "\nArmour Class: ", (10 + ability.modifier(finalscore['Dexterity'])))

for k, v in finalscore.items():
    print(k, ": ", v, ability.modifier(v))