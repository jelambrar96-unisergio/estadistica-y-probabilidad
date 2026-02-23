import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generar datos aleatorios con algunos valores atípicos
np.random.seed(42)
datos = np.concatenate([np.random.normal(100, 20, 100), [200, 210, 50]])

# 1. Crear el diagrama de caja usando Seaborn (más estético)
plt.figure(figsize=(10, 6))
sns.boxplot(x=datos, color="skyblue")

# Añadir títulos y etiquetas
plt.title('Diagrama de Cajas y Bigotes (Boxplot)')
plt.xlabel('Valores de la Variable')

# Mostrar el gráfico
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()
