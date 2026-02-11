
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Datos de ejemplo: Quejas de clientes
data = {'Defecto': ['Fuga', 'Ruido', 'Vibración', 'Calentamiento', 'Olor', 'Otros'],
        'Frecuencia': [45, 30, 15, 5, 3, 2]}

df = pd.DataFrame(data)
df = df.sort_values(by='Frecuencia', ascending=False)
df['Porcentaje Acumulado'] = df['Frecuencia'].cumsum() / df['Frecuencia'].sum() * 100

# Configurar figura y ejes
fig, ax1 = plt.subplots(figsize=(10, 6))

# Gráfico de barras
ax1.bar(df['Defecto'], df['Frecuencia'], color='C0')
ax1.set_xlabel('Defecto')
ax1.set_ylabel('Frecuencia', color='C0')
ax1.tick_params(axis='y', labelcolor='C0')

# Eje secundario para la línea de porcentaje acumulado
ax2 = ax1.twinx()
ax2.plot(df['Defecto'], df['Porcentaje Acumulado'], color='C1', marker='D', ms=7)
ax2.yaxis.set_major_formatter(PercentFormatter())
ax2.set_ylabel('Porcentaje Acumulado', color='C1')
ax2.tick_params(axis='y', labelcolor='C1')
ax2.set_ylim(0, 110)

plt.title('Diagrama de Pareto')
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.show()
