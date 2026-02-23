import numpy as np

# Dataset de ejemplo: Resultados de un test
datos = [75, 80, 82, 85, 88, 90, 92, 95]

# 1. Rango
rango = np.ptp(datos) # "peak to peak"

# 2. Varianza Poblacional (sigma^2)
varianza_pob = np.var(datos)

# 3. Varianza Muestral (s^2)
# El parámetro ddof (Delta Degrees of Freedom) es 1 para la muestral
varianza_muest = np.var(datos, ddof=1)

# 4. Desviación Estándar Poblacional (sigma)
std_pob = np.std(datos)

# 5. Desviación Estándar Muestral (s)
std_muest = np.std(datos, ddof=1)

print(f"Dataset: {datos}")
print(f"Rango: {rango}")
print(f"Varianza Poblacional: {varianza_pob:.2f}")
print(f"Varianza Muestral: {varianza_muest:.2f}")
print(f"Desviación Estándar Poblacional: {std_pob:.2f}")
print(f"Desviación Estándar Muestral: {std_muest:.2f}")
