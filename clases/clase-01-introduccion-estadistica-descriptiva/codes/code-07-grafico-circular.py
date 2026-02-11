
import matplotlib.pyplot as plt

# Datos de ejemplo
labels = ['Frutas', 'Verduras', 'Carnes', 'Lácteos']
sizes = [30, 45, 15, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explotar la primera rebanada

# Crear gráfico circular
plt.figure(figsize=(7, 7))
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')  # Para asegurar que se dibuje como un círculo
plt.title('Distribución de Alimentos')
plt.show()
