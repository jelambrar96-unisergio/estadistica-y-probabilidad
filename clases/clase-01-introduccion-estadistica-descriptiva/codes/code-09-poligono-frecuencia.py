
import matplotlib.pyplot as plt
import numpy as np

# Datos simulados (puntos medios de las clases y sus frecuencias)
# Supongamos clases: [0-10), [10-20), [20-30), [30-40), [40-50)
puntos_medios = [5, 15, 25, 35, 45]
frecuencias = [10, 25, 40, 15, 5]

# Para cerrar el polígono, añadimos puntos ficticios al inicio y al final con frecuencia 0
puntos_medios_ext = [puntos_medios[0] - 10] + puntos_medios + [puntos_medios[-1] + 10]
frecuencias_ext = [0] + frecuencias + [0]

# Crear polígono de frecuencias
plt.figure(figsize=(8, 5))
plt.plot(puntos_medios_ext, frecuencias_ext, marker='o', linestyle='-', color='purple')
plt.fill_between(puntos_medios_ext, frecuencias_ext, alpha=0.2, color='purple')

plt.title('Polígono de Frecuencias')
plt.xlabel('Punto Medio de Clase')
plt.ylabel('Frecuencia Absoluta')
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(np.arange(-5, 60, 10))

plt.show()
