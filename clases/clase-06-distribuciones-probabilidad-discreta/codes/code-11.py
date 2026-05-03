import numpy as np
import matplotlib.pyplot as plt
from math import comb

N, K, n = 25, 10, 5
x = np.arange(max(0, n-K), min(n, K) + 1)
p = [comb(K, k) * comb(N-K, n-k) / comb(N, n) for k in x]

plt.stem(x, p, linefmt='r-', markerfmt='ro', basefmt=' ')
plt.title('Distribución Hipergeométrica')
plt.xlabel('k (éxitos en la muestra)')
plt.ylabel('P(X = k)')
plt.grid(axis='y', alpha=0.3)
plt.show()
