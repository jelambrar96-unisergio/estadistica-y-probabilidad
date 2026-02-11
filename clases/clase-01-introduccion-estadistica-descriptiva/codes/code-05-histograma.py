
import matplotlib.pyplot as plt
import numpy as np

# Generar datos aleatorios con distribución normal
np.random.seed(42)
data = np.random.normal(loc=170, scale=10, size=250)

# Crear el histograma
plt.figure(figsize=(10, 6))
plt.hist(data, bins=15, color='skyblue', edgecolor='black', alpha=0.7)

# Añadir títulos y etiquetas
plt.title('Histograma de Alturas (Simulado)')
plt.xlabel('Altura (cm)')
plt.ylabel('Frecuencia')
plt.grid(axis='y', alpha=0.5)

plt.show()
