import pytest
import numpy as np

from fractions import Fraction
from functions import ceiling
from functions import remainder

from EgyptianFractions import egyptian_fraction

def test_addition():
    assert Fraction(1,3) + Fraction(1,4) == Fraction(7,12)

def test_egyptian_fraction():
    ef = egyptian_fraction(Fraction(7,15))
    expected = [Fraction(1,3), Fraction(1,8), Fraction(1,120)]
    assert ef == expected