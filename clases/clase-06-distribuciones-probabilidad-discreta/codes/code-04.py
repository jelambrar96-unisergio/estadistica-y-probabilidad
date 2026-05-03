from math import factorial
from scipy.stats import multinomial

def multinomial_prob(n, ps, ks):
    numer = factorial(n)
    denom = 1
    prod = 1
    for ki, pi in zip(ks, ps):
        denom *= factorial(ki)
        prod *= pi**ki
    return numer * prod / denom

print('P([2,2,1,0,0,0]) en 5 lanzamientos:', multinomial_prob(5, [1/6]*6, [2, 2, 1, 0, 0, 0]))
print()

rv = multinomial(6, [1/6]*6,)
print('P([2,2,1,0,0,0]) en 5 lanzamientos:', rv.pmf([2, 2, 1, 0, 0, 0]))
