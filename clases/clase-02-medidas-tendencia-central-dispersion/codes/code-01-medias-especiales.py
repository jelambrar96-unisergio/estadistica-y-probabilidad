import numpy as np
from scipy import stats

# Dataset de ejemplo: Tasas de crecimiento o razones
# Nota: Los valores deben ser positivos para estas medias
datos = [1.05, 1.10, 1.02, 1.15, 1.08]

# 1. Media Geométrica
# Útil para promediar razones, porcentajes o tasas de crecimiento
media_geom = stats.gmean(datos)

# 2. Media Armónica
# Útil para promediar velocidades, tiempos o densidades
media_armon = stats.hmean(datos)

print(f"Dataset: {datos}")
print(f"Media Geométrica: {media_geom:.4f}")
print(f"Media Armónica: {media_armon:.4f}")
