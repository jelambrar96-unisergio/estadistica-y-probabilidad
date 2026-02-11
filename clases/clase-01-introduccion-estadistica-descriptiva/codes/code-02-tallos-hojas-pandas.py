import matplotlib.pyplot as plt
import pandas as pd
import stemgraphic

LIST_VALUES = [
    31, 40, 45, 49, 52, 53, 57, 58, 58, 60, 
    61, 61, 63, 66, 67, 67, 67, 67, 68, 69, 
    70, 70, 70, 70, 72, 73, 75, 75, 76, 76, 
    78, 79, 80, 81, 83, 84]

df = pd.DataFrame(LIST_VALUES, columns=['Datos'])

# Ordenar los datos
df = df.sort_values(by='Datos')

# Separar tallos y hojas
df['Tallo'] = df['Datos'] // 10
df['Hoja'] = df['Datos'] % 10

# Agrupar por tallo
stem_leaf = df.groupby('Tallo')['Hoja'].apply(list)
print(stem_leaf)
