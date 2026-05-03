import numpy as np
import matplotlib.pyplot as plt
from math import exp, factorial

lambdas = [1, 3, 6]
k_max = 15
x = np.arange(0, k_max + 1)

plt.figure(figsize=(10, 4))
for lam in lambdas:
    p = [exp(-lam) * lam**k / factorial(k) for k in x]
    plt.plot(x, p, marker='o', label=f'λ = {lam}')

plt.title('Distribución de Poisson para diferentes valores de λ')
plt.xlabel('k')
plt.ylabel('P(X = k)')
plt.legend()
plt.grid(True)
plt.show()

# --- 

import numpy as np
import matplotlib.pyplot as plt
from math import exp, factorial

lambdas = [1, 3, 6]
colors = ['r', 'b', 'g'] # red, blue, green
k_max = 15
x = np.arange(0, k_max + 1)

plt.figure(figsize=(10, 4))
for lam, color in zip(lambdas, colors):
    p = [exp(-lam) * lam**k / factorial(k) for k in x]
    plt.stem(x, p, label=f'λ = {lam}', linefmt=f'{color}-', markerfmt=f'{color}o', basefmt=' ')

plt.title('Distribución de Poisson para diferentes valores de λ')
plt.xlabel('k')
plt.ylabel('P(X = k)')
plt.legend()
plt.grid(True)
plt.show()
