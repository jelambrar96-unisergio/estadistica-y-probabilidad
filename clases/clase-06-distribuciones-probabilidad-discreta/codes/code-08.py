from math import exp, factorial

def poisson_prob(k, lam):
    return exp(-lam) * lam**k / factorial(k)

print('P(X = 5) con λ = 3:', poisson_prob(5, 3))
