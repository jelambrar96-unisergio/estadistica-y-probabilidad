import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Definimos parámetros: n=intentos, p=probabilidad de éxito
n, p = 3, 0.5
x = np.arange(0, n+1)
probabilidades = binom.pmf(x, n, p)

print(f"Valores posibles: {x}")
print(f"Probabilidades: {probabilidades}")