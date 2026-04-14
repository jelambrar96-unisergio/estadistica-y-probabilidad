import numpy as np
import matplotlib.pyplot as plt

# Definimos parámetros: n=intentos, p=probabilidad de éxito
x = np.array([0, 1, 2, 3])
probabilidades = np.array([0.1, 0.2, 0.3, 0.4])
CDF = np.cumsum(probabilidades)

# Se grafica la funcion de probabilidad acumulada como una funcion escalonada
plt.step(x, CDF, label="CDF")
plt.title("Función de Probabilidad Acumulada")
plt.show()