import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import binom

n = 10
ps = [0.2, 0.4, 0.7]
colors = ['r', 'b', 'g'] # red, blue, green
x = np.arange(0, n + 1)

plt.figure(figsize=(10, 4))
for p, color in zip(ps, colors):
    p_x = [binom.pmf(k, n, p) for k in x]
    plt.stem(x, p_x, label=f'p = {p}', linefmt=f'{color}-', markerfmt=f'{color}o', basefmt=' ')

plt.title('Distribución Binomial para diferentes valores de p')
plt.xlabel('k (número de éxitos)')
plt.ylabel('P(X = k)')
plt.legend()
plt.grid(True)
plt.show()
