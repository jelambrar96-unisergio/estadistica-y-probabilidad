import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

x = np.linspace(-4, 4, 100)
cdf_values = norm.cdf(x, 0, 1)

plt.plot(x, cdf_values, color='red', label='Normal Standard CDF')
plt.title("Función de Probabilidad Acumulada")
plt.grid(True)
plt.show()
