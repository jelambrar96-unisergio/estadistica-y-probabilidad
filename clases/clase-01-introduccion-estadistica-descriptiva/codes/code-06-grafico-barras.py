
import matplotlib.pyplot as plt

# Datos de ejemplo
categorias = ['A', 'B', 'C', 'D', 'E']
valores = [23, 45, 56, 12, 33]

# Crear gráfico de barras
plt.figure(figsize=(8, 5))
plt.bar(categorias, valores, color='green', alpha=0.6)

# Añadir títulos y etiquetas
plt.title('Gráfico de Barras Simple')
plt.xlabel('Categoría')
plt.ylabel('Valor')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
