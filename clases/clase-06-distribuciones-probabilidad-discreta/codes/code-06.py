from math import comb
from scipy.stats import nbinom

def negative_binomial_prob(r, p, k):
    return comb(k - 1, r - 1) * p**r * (1 - p)**(k - r)

print('P(k = 7) con r = 3 y p = 0.5:', negative_binomial_prob(3, 0.5, 7))

rv = nbinom(3, 0.5)
print('P(k = 7) con r = 3 y p = 0.5:', rv.pmf(7))
