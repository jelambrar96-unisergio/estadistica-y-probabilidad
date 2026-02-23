import numpy as np
from scipy import stats

# Dataset de ejemplo: Edades de un grupo de estudio
datos = [20, 22, 22, 23, 25, 26, 28, 30, 32, 45]

# 1. Media Aritmética
media = np.mean(datos)

# 2. Mediana
mediana = np.median(datos)

# 3. Moda
# stats.mode retorna un objeto con el valor y la cuenta
moda_res = stats.mode(datos, keepdims=True)
moda = moda_res.mode[0]
frecuencia = moda_res.count[0]

print(f"Dataset: {datos}")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda} (aparece {frecuencia} veces)")
