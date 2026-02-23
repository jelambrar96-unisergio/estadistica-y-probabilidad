import pandas as pd
import numpy as np

# Datos agrupados (Intervalos, Frecuencia absoluta)
data = {
    'Limite_Inf': [10, 20, 30, 40, 50],
    'Limite_Sup': [20, 30, 40, 50, 60],
    'Frecuencia': [5, 12, 20, 8, 5]
}

df = pd.DataFrame(data)
df['Frec_Acum'] = df['Frecuencia'].cumsum()
n = df['Frecuencia'].sum()

def calcular_medida_posicion(df, n, k, N):
    """
    Calcula una medida de posición (mediana, cuartil, percentil) para datos agrupados.
    k: número de la medida (ej. 1 para Q1, 50 para P50)
    N: divisor de la medida (ej. 4 para cuartiles, 100 para percentiles)
    """
    posicion = (k * n) / N
    
    # Encontrar la clase donde se encuentra la posición
    clase_idx = df[df['Frec_Acum'] >= posicion].index[0]
    
    Li = df.loc[clase_idx, 'Limite_Inf']
    Fi_1 = df.loc[clase_idx - 1, 'Frec_Acum'] if clase_idx > 0 else 0
    fi = df.loc[clase_idx, 'Frecuencia']
    ai = df.loc[clase_idx, 'Limite_Sup'] - Li
    
    medida = Li + ((posicion - Fi_1) / fi) * ai
    return medida

# 1. Mediana (Q2 o P50)
mediana = calcular_medida_posicion(df, n, 2, 4)

# 2. Cuartiles
q1 = calcular_medida_posicion(df, n, 1, 4)
q3 = calcular_medida_posicion(df, n, 3, 4)

# 3. Percentiles (ej. Percentil 90)
p90 = calcular_medida_posicion(df, n, 90, 100)

print("Tabla de Datos Agrupados:")
print(df)
print(f"\nResultados de Posición:")
print(f"Mediana: {mediana:.2f}")
print(f"Cuartil 1 (Q1): {q1:.2f}")
print(f"Cuartil 3 (Q3): {q3:.2f}")
print(f"Percentil 90 (P90): {p90:.2f}")
