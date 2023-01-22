import pytest
from src.keepDice import keepDice

def test_keepDice():
    assert keepDice('2', [2,3]) == [2,3,2]
    assert keepDice("2, 4", [3]) == [3,2,4]
    assert keepDice('1,3', [4,5,6]) == [4,5,6,1,3]
    assert keepDice('2', [2,3,2]) == [2,3,2,2]

