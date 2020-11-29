from itertools import product
from fractions import Fraction

p = list(product([1,2,3,4,5,6], repeat=2))

pDiff = [(x,y) for x,y in p if x + y == 6 and x!=y]


print(Fraction(len(pDiff), len(p)))
# 1/9

