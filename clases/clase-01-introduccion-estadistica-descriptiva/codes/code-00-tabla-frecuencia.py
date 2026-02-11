import pandas as pd

# 1. Dataset con 20 valores
datos = [2, 3, 3, 4, 2, 5, 3, 4, 2, 3, 4, 5, 3, 2, 4, 3, 5, 4, 3, 2]
df_input = pd.DataFrame(datos, columns=['horas_estudio'])

# 2. Calculamos la tabla de frecuencias completa
tabla_frec = df_input['horas_estudio'].value_counts().sort_index().reset_index()
tabla_frec.columns = ['Horas', 'Frec_Absoluta']

# 3. Frecuencia Relativa
tabla_frec['Frec_Relativa'] = tabla_frec['Frec_Absoluta'] / len(df_input)

# 4. Frecuencia Acumulada
tabla_frec['Frec_Acumulada'] = tabla_frec['Frec_Absoluta'].cumsum()

# 5. Frecuencia Acumulada en Porcentaje
tabla_frec['Frec_Acum_%'] = (tabla_frec['Frec_Acumulada'] / len(df_input) * 100).round(1)

# 6. Frecuencia Relativa Acumulada
tabla_frec['Frec_Rel_Acumulada'] = tabla_frec['Frec_Relativa'].cumsum()

print(tabla_frec)
