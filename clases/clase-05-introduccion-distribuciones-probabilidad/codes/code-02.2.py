import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


x = np.linspace(-4, 4, 100)
pdf = norm.pdf(x, 0, 1)

plt.plot(x, pdf, label='Normal Standard PDF')
plt.fill_between(x, pdf, alpha=0.2)
plt.title("Función de Densidad de Probabilidad")
plt.show()