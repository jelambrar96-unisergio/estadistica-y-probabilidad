
import matplotlib.pyplot as plt
import numpy as np

# Datos
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7]

# Preparar datos para el gráfico de puntos
values, counts = np.unique(data, return_counts=True)

# Crear el gráfico
fig, ax = plt.subplots(figsize=(8, 2))
for value, count in zip(values, counts):
    ax.plot([value]*count, range(1, count+1), 'bo', markersize=10)

# Configuración del gráfico
ax.set_xticks(values)
ax.set_yticks([])  # Ocultar eje Y ya que solo representa el conteo visual
ax.set_title('Gráfico de Puntos')
ax.set_xlabel('Valor')
ax.set_ylim(0, max(counts) + 1)
ax.grid(axis='x', linestyle='--', alpha=0.7)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.show()
