import pytest
from src.logicYatzy import Yatzy

@pytest.mark.chance
def test_chance():
    assert Yatzy.chance(1, 2, 3, 4, 5) == 15 
    assert Yatzy.chance(1, 1, 3, 3, 6) == 14
    assert Yatzy.chance(4, 5, 5, 6, 1) == 21

@pytest.mark.yatzy
def test_yatzy():
    assert Yatzy.yatzy(5, 5, 5, 5, 5) == 50
    assert Yatzy.yatzy(5, 5, 5, 5, 4) == 0
    assert Yatzy.yatzy(6, 6, 6, 6, 6) == 50

@pytest.mark.ones
def test_ones():
    assert Yatzy.ones(1, 2, 3, 4, 1) == 2
    assert Yatzy.ones(1, 1, 1, 4, 5) == 3
    assert Yatzy.ones(5, 2, 6, 4, 5) == 0

@pytest.mark.twos
def test_twos():
    assert Yatzy.twos(1, 2, 3, 4, 1) == 2
    assert Yatzy.twos(2, 2, 2, 4, 5) == 6
    assert Yatzy.twos(5, 1, 6, 4, 5) == 0

@pytest.mark.threes
def test_threes():
    assert Yatzy.threes(1, 2, 3, 4, 1) == 3
    assert Yatzy.threes(2, 2, 2, 4, 5) == 0
    assert Yatzy.threes(3, 3, 6, 3, 5) == 9

@pytest.mark.fours
def test_fours():
    assert Yatzy.fours(4, 4, 3, 4, 1) == 12
    assert Yatzy.fours(2, 2, 2, 4, 5) == 4
    assert Yatzy.fours(3, 3, 6, 3, 5) == 0

@pytest.mark.fives
def test_fives():
    assert Yatzy.fives(5, 5, 3, 4, 1) == 10
    assert Yatzy.fives(2, 5, 2, 5, 5) == 15
    assert Yatzy.fives(3, 3, 6, 3, 1) == 0

@pytest.mark.sixes
def test_sixes():
    assert Yatzy.sixes(5, 2, 1, 6, 1) == 6
    assert Yatzy.sixes(6, 6, 6, 5, 5) == 18
    assert Yatzy.sixes(3, 3, 5, 3, 1) == 0

@pytest.mark.score_pair
def test_score_pair():
    assert Yatzy.score_pair(5, 5, 1, 6, 1) == 10
    assert Yatzy.score_pair(6, 6, 1, 3, 5) == 12
    assert Yatzy.score_pair(3, 4, 5, 2, 1) == 0

@pytest.mark.two_pair
def test_two_pair():
    assert Yatzy.two_pair(1, 1, 2, 2, 3) == 6
    assert Yatzy.two_pair(6, 6, 2, 4, 4) == 20
    assert Yatzy.two_pair(1, 1, 2, 3, 4) == 0

@pytest.mark.three_of_kind
def test_three_of_a_kind():
    assert Yatzy.three_of_a_kind(1, 1, 1, 2, 2) == 3
    assert Yatzy.three_of_a_kind(6, 6, 4, 6, 2) == 18
    assert Yatzy.three_of_a_kind(5, 6, 5, 6, 5) == 15
    assert Yatzy.three_of_a_kind(6, 6, 6, 6, 6) == 0

@pytest.mark.four_of_kind
def test_four_of_a_kind():
    assert Yatzy.four_of_a_kind(1, 1, 1, 1, 2) == 4
    assert Yatzy.four_of_a_kind(6, 6, 6, 6, 2) == 24
    assert Yatzy.four_of_a_kind(5, 1, 5, 5, 5) == 20
    assert Yatzy.four_of_a_kind(6, 2, 4, 5, 6) == 0

@pytest.mark.smallStraight
def test_smallStraight():
    assert Yatzy.smallStraight(2, 2, 3, 4, 5) == 0
    assert Yatzy.smallStraight(1, 2, 3, 4, 5) == 15
    assert Yatzy.smallStraight(2, 6, 3, 4, 5) == 0

@pytest.mark.largeStraight
def test_largeStraight():
    assert Yatzy.largeStraight(1, 2, 3, 4, 5) == 20
    assert Yatzy.largeStraight(2, 2, 3, 3, 5) == 0

@pytest.mark.fullHouse
def test_fullHouse():
    assert Yatzy.fullHouse(6, 2, 2, 6, 6) == 22
    assert Yatzy.fullHouse(1, 1, 1, 1, 4) == 0




