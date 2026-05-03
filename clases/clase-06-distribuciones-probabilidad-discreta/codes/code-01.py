import numpy as np
import matplotlib.pyplot as plt

# Parámetros
a, b = 1, 6
x = np.arange(a, b + 1)
p = np.ones_like(x) / len(x)

plt.bar(x, p, color='skyblue')
plt.title('Distribución uniforme discreta: dado justo')
plt.xlabel('x')
plt.ylabel('P(X = x)')
plt.grid(axis='y', alpha=0.3)
plt.show()
