import numpy as np
import matplotlib.pyplot as plt
from math import comb

r = 3
ps = [0.3, 0.5]
colors = ['r', 'b'] # red, blue
k = np.arange(r, r + 15)


plt.figure(figsize=(10, 4))
for p, color in zip(ps, colors):
    p_k = [comb(ki - 1, r - 1) * p**r * (1 - p)**(ki - r) for ki in k]
    plt.stem(k, p_k, label=f'p = {p}', linefmt=f'{color}-', markerfmt=f'{color}o', basefmt=' ')  

plt.title('Distribución Binomial Negativa para diferentes valores de p')
plt.xlabel('k (ensayos hasta r éxitos)')
plt.ylabel('P(X = k)')
plt.legend()
plt.grid(True)
plt.show()
