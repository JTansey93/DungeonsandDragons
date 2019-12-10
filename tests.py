import pytest

import sys
sys.path.insert(0, "C:\\Users\\jmsta\\OneDrive\\Documents\\GitHub\\DungeonsandDragons")

import CharacterCreation.myfunctions

modifier = CharacterCreation.myfunctions.modifier

def test_modifier():
    assert modifier(15) == 2, "Should be 2"

print('Tests passed')