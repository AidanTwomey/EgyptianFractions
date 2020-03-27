import numpy as np

from fractions import Fraction
from functions import ceiling
from functions import remainder

def make_egytpian_fraction(x, ef):
    n = x.numerator
    d = x.denominator

    if (n ==1 ):
        ef.append(x)
        return ef
        
    ef.append(Fraction(1, ceiling(d,n)))

    next_ef =Fraction(n - remainder(d,n), d * ceiling(d,n))

    return make_egytpian_fraction(next_ef, ef)

def egyptian_fraction(x):
    
    ef = []

    return make_egytpian_fraction(x,ef)