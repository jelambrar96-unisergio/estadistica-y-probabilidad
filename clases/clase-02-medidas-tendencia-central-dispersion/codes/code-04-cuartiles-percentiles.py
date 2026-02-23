import numpy as np

# Dataset de ejemplo
datos = [12, 15, 17, 20, 22, 25, 28, 30, 35, 40, 45, 50]

# 1. Cuartiles (Q1, Q2, Q3)
# Q2 es la mediana
q1 = np.percentile(datos, 25)
q2 = np.percentile(datos, 50)
q3 = np.percentile(datos, 75)

# 2. Rango Intercuartílico (IQR)
iqr = q3 - q1

# 3. Percentiles específicos
p10 = np.percentile(datos, 10)
p90 = np.percentile(datos, 90)

print(f"Dataset: {datos}")
print(f"Q1 (Percentil 25): {q1}")
print(f"Q2 (Mediana/Percentil 50): {q2}")
print(f"Q3 (Percentil 75): {q3}")
print(f"IQR: {iqr}")
print(f"Percentil 10: {p10}")
print(f"Percentil 90: {p90}")
