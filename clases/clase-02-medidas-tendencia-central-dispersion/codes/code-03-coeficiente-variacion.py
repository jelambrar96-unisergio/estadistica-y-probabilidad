import numpy as np

def coeficiente_variacion(data):
    media = np.mean(data)
    desviacion = np.std(data, ddof=1)
    return (desviacion / abs(media)) * 100

# Comparación de dos grupos
grupo_a = [10, 12, 11, 13, 12]
grupo_b = [100, 120, 110, 130, 120]

cv_a = coeficiente_variacion(grupo_a)
cv_b = coeficiente_variacion(grupo_b)

print(f"Grupo A - Media: {np.mean(grupo_a)}, Std: {np.std(grupo_a, ddof=1):.2f}, CV: {cv_a:.2f}%")
print(f"Grupo B - Media: {np.mean(grupo_b)}, Std: {np.std(grupo_b, ddof=1):.2f}, CV: {cv_b:.2f}%")
