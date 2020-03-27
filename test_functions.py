from functions import func
from functions import ceiling
from functions import square
from functions import turnsix
from functions import remainder

import pytest

@pytest.mark.parametrize("test_input,expected", [((11,3), 4), ((12,6), 2)])
def test_ceiling(test_input,expected):
    assert ceiling(test_input[0],test_input[1]) == expected

def test_turnsix():
    assert turnsix(8) == 6

def test_square():
    assert square(8) == 64

@pytest.mark.parametrize("test_input,expected", [((15,7), 1), ((11,7), 4), ((12,6), 0), ((9,7), 2), ((25,4), 1), ((1,6), 1)])
def test_remainder(test_input,expected):
    assert remainder(test_input[0],test_input[1]) == expected


