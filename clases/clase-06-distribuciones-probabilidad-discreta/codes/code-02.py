from math import comb
from scipy.stats import binom

# contruccion de la distribucion binomial a partir de la definicion matematica

def binomial_pdf(k, n, p):
    return comb(n, k) * p**k * (1 - p)**(n - k)

def binomial_cdf(k, n, p):
    return sum(binomial_pdf(i, n, p) for i in range(k + 1))


print('calculo usando la definicion')
print('P(X = 4) con n = 10 y p = 0.4:', binomial_pdf(4, 10, 0.4))
print('P(X <= 4) con n = 10 y p = 0.4:', binomial_cdf(4, 10, 0.4))
print()

print('calculo usando la funicion binom de scipy')
print('P(X = 4) con n = 10 y p = 0.4:', binom.pmf(4, 10, 0.4))
print('P(X <= 4) con n = 10 y p = 0.4:', binom.cdf(4, 10, 0.4))
