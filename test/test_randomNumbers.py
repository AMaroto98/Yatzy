import pytest
from src.randomNumbers import RandomNumbers

@pytest.mark.firsRoll
def test_firstRoll():
    assert len(RandomNumbers.firstRoll([])) == 5
    assert type(RandomNumbers.firstRoll([])[0]) == int 
    assert type(RandomNumbers.firstRoll([])[1]) == int 
    assert type(RandomNumbers.firstRoll([])[2]) == int 
    assert type(RandomNumbers.firstRoll([])[3]) == int 
    assert type(RandomNumbers.firstRoll([])[4]) == int 

@pytest.mark.otherRoll
def test_otherRolls():
    assert len(RandomNumbers.otherRolls([], "5,3,4,2,1")) == 0
    assert len(RandomNumbers.otherRolls([], "1,2")) == 3
    assert len(RandomNumbers.otherRolls([], "")) == 5 
    assert type(RandomNumbers.otherRolls([], "")[0]) == int 
    assert type(RandomNumbers.otherRolls([], "")[1]) == int 
    assert type(RandomNumbers.otherRolls([], "")[2]) == int 
    assert type(RandomNumbers.otherRolls([], "")[3]) == int 
    assert type(RandomNumbers.otherRolls([], "")[4]) == int 