from math import comb

def hipergeo_prob(N, K, n, k):
    return comb(K, k) * comb(N-K, n-k) / comb(N, n)

print('P(X = 2) con N = 25, K = 10, n = 5:', hipergeo_prob(25, 10, 5, 2))


from scipy.stats import hypergeom

print('P(X = 2) con N = 25, K = 10, n = 5:', hypergeom.pmf(2, 25, 10, 5))

