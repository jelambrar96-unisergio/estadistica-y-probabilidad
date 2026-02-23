import pandas as pd
import numpy as np

# Datos agrupados (Intervalos, Frecuencia absoluta)
data = {
    'Limite_Inf': [10, 20, 30, 40, 50],
    'Limite_Sup': [20, 30, 40, 50, 60],
    'Frecuencia': [5, 12, 20, 8, 5]
}

df = pd.DataFrame(data)

# 1. Calcular Marca de Clase (x_i)
df['Marca_Clase'] = (df['Limite_Inf'] + df['Limite_Sup']) / 2

# 2. Media para datos agrupados: sum(f_i * x_i) / n
n = df['Frecuencia'].sum()
media_agrupada = (df['Frecuencia'] * df['Marca_Clase']).sum() / n

# 3. Varianza para datos agrupados: sum(f_i * (x_i - mean)^2) / (n - 1)
varianza_agrupada = (df['Frecuencia'] * (df['Marca_Clase'] - media_agrupada)**2).sum() / (n - 1)

# 4. Desviación estándar
std_agrupada = np.sqrt(varianza_agrupada)

print("Tabla de Datos Agrupados:")
print(df)
print(f"\nMedia Agrupada: {media_agrupada:.2f}")
print(f"Varianza Agrupada (muestral): {varianza_agrupada:.2f}")
print(f"Desviación Estándar Agrupada: {std_agrupada:.2f}")
