import numpy as np
import matplotlib.pyplot as plt

# Definimos parámetros: n=intentos, p=probabilidad de éxito
x = np.array([0, 1, 2, 3])
probabilidades = np.array([0.1, 0.2, 0.3, 0.4])

print(f"Valores posibles: {x}")
print(f"Probabilidades: {probabilidades}")

plt.stem(x, probabilidades)
plt.title("Función de Masa de Probabilidad")
plt.show()
