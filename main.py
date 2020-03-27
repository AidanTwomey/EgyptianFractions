from fractions import Fraction
from functions import ceiling
from functions import turnsix
from EgyptianFractions import egyptian_fraction

print('Please enter the numerator:')
n = int(input())

print('Please enter the denominator:')
d = int(input())

for unit_fraction in egyptian_fraction(Fraction(n,d)):
    print(f'{unit_fraction}')
