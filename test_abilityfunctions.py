import pytest

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import charactercreator.abilityfunctions

modifier = charactercreator.abilityfunctions.modifier
roll = charactercreator.abilityfunctions.abilityRoll

def test_modifier():
    assert modifier(15) == 2, "Should be 2"

def test_roll():
    assert 18 >= roll() >= 3, "Should be between 3 & 18"