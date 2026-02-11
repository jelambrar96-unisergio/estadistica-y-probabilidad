
import matplotlib.pyplot as plt
import numpy as np

# Datos simulados (límites superiores de las clases y frecuencias acumuladas)
# Clases: [10-20), [20-30), [30-40), [40-50), [50-60)
limites_superiores = [20, 30, 40, 50, 60]
frecuencias = [5, 12, 20, 8, 5]
frecuencias_acumuladas = np.cumsum(frecuencias)

# Añadimos el límite inferior de la primera clase con frecuencia acumulada 0
limites = [10] + limites_superiores
acumuladas = [0] + list(frecuencias_acumuladas)

# Crear Ojiva
plt.figure(figsize=(8, 5))
plt.plot(limites, acumuladas, marker='o', linestyle='-', color='darkorange')

plt.title('Ojiva (Polígono de Frecuencias Acumuladas)')
plt.xlabel('Límite Superior de Clase')
plt.ylabel('Frecuencia Acumulada')
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(np.arange(0, 70, 10))
plt.ylim(0, max(acumuladas) * 1.1)

# Anotaciones
for x, y in zip(limites, acumuladas):
    if y > 0:
        plt.text(x, y + 1, str(y), ha='center')

plt.show()
