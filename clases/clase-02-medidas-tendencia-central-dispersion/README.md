# Clase 02: Medidas de tendencia central y Medidas de dispersión

## 1. Introducción

En estadística, la descripción de un conjunto de datos no solo requiere de su visualización gráfica, sino también de medidas numéricas que resumen sus propiedades más importantes. Las **medidas de tendencia central** buscan identificar un valor "típico" o central alrededor del cual se agrupan los datos, mientras que las **medidas de dispersión** cuantifican qué tan extendidos o concentrados se encuentran dichos datos respecto al centro.

Estas medidas son fundamentales para el análisis exploratorio de datos (EDA) y constituyen la base para la inferencia estadística.

---

## 2. Medidas de tendencia central

Las **medidas de tendencia central** son parámetros estadísticos que informan sobre el centro de la distribución de la muestra o población.

### 2.1. La Media

La **media aritmética** es la medida de tendencia central más común. Se calcula sumando todos los valores y dividiendo por el número total de observaciones.

- **Media Poblacional ($\mu$):**
  
$$
\mu = \frac{\sum_{i=1}^{N} X_i}{N}
$$

- **Media Muestral ($\bar{x}$):**

$$
\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}
$$

### 2.2. La Mediana

La **mediana** es el valor que ocupa la posición central cuando los datos están ordenados de menor a mayor. Si el número de datos es par, es el promedio de los dos valores centrales. Es una medida robusta frente a valores atípicos.

### 2.3. La Moda

La **moda** es el valor que aparece con mayor frecuencia en un conjunto de datos. Un conjunto puede ser unimodal, bimodal o multimodal.

### 2.4. Ejemplo en Python (Media, Mediana, Moda)

```python
import numpy as np
from scipy import stats

datos = [20, 22, 22, 23, 25, 26, 28, 30, 32, 45]

media = np.mean(datos)
mediana = np.median(datos)
moda = stats.mode(datos, keepdims=True).mode[0]

print(f"Media: {media}, Mediana: {mediana}, Moda: {moda}")
```

[Código completo: code-00-medidas-tendencia-central.py](codes/code-00-medidas-tendencia-central.py)

### 2.5. Otras medidas de tendencia central

#### 2.5.1. La media geométrica

Se define como la raíz n-ésima del producto de todos los números. Es útil para promediar razones o tasas de crecimiento.

$$
G = \sqrt[n]{x_1 \cdot x_2 \cdot \dots \cdot x_n}
$$

#### 2.5.2. La media armónica

Es el recíproco de la suma de los recíprocos de los valores. Se utiliza principalmente para promediar velocidades o densidades.

$$
H = \frac{n}{\sum_{i=1}^{n} \frac{1}{x_i}}
$$

### 2.6. Ejemplo en Python (Geométrica y Armónica)

```python
from scipy import stats

datos = [1.05, 1.10, 1.02, 1.15, 1.08]
media_geom = stats.gmean(datos)
media_armon = stats.hmean(datos)

print(f"Media Geométrica: {media_geom:.4f}, Media Armónica: {media_armon:.4f}")
```

[Código completo: code-01-medias-especiales.py](codes/code-01-medias-especiales.py)

---

## 3. Medidas de dispersión

Las **medidas de dispersión** indican qué tanto se alejan los datos respecto a la media aritmética. Son esenciales para entender la variabilidad y el riesgo en los procesos.

### 3.1. El Rango

Es la diferencia entre el valor máximo y el valor mínimo de un conjunto de datos.

$$
R = X_{max} - X_{min}
$$

### 3.2. La Varianza

La **varianza** mide el promedio de los cuadrados de las desviaciones de los datos respecto a su media.

#### 3.2.1. Varianza poblacional ($\sigma^2$)

Se utiliza cuando se dispone de todos los datos de la población.

$$
\sigma^2 = \frac{\sum_{i=1}^{N} (X_i - \mu)^2}{N}
$$

#### 3.2.2. Varianza muestral ($s^2$)

Se utiliza cuando se trabaja con una muestra. Se divide por $n-1$ (corrección de Bessel) para obtener un estimador insesgado.

$$
s^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n - 1}
$$

### 3.3. La Desviación Estándar

Es la raíz cuadrada de la varianza. Tiene la ventaja de estar expresada en las mismas unidades que los datos originales.

#### 3.3.1. Desviación estándar poblacional ($\sigma$)

$$
\sigma = \sqrt{\sigma^2}
$$

#### 3.3.2. Desviación estándar muestral ($s$)

$$
s = \sqrt{s^2}
$$

### 3.4. Ejemplo en Python (Varianza y Desviación Estándar)

```python
import numpy as np

datos = [75, 80, 82, 85, 88, 90, 92, 95]

varianza_muest = np.var(datos, ddof=1)
std_muest = np.std(datos, ddof=1)

print(f"Varianza Muestral: {varianza_muest:.2f}")
print(f"Desviación Estándar Muestral: {std_muest:.2f}")
```

[Código completo: code-02-medidas-dispersion.py](codes/code-02-medidas-dispersion.py)

### 3.5. El Coeficiente de Variación (CV)

Es una medida de dispersión relativa que permite comparar la variabilidad entre conjuntos de datos con diferentes unidades o medias. Se expresa generalmente en porcentaje.

$$
CV = \left( \frac{s}{|\bar{x}|} \right) \cdot 100\%
$$

### 3.6. Ejemplo en Python (Coeficiente de Variación)

```python
import numpy as np

datos = [10, 12, 11, 13, 12]
cv = (np.std(datos, ddof=1) / np.mean(datos)) * 100

print(f"Coeficiente de Variación: {cv:.2f}%")
```

[Código completo: code-03-coeficiente-variacion.py](codes/code-03-coeficiente-variacion.py)

---

## 4. Cuartiles y percentiles

Los **cuartiles** y **percentiles** son medidas de posición que dividen un conjunto de datos ordenados en partes iguales.

- **Cuartiles ($Q_1, Q_2, Q_3$):** Dividen los datos en cuatro partes iguales (25%, 50%, 75%). $Q_2$ es equivalente a la mediana.
- **Percentiles ($P_k$):** Dividen los datos en 100 partes iguales. El percentil $k$ es el valor por debajo del cual se encuentra el $k\%$ de los datos.
- **Rango Intercuartílico (IQR):** Es la diferencia entre el tercer y primer cuartil.

$$
IQR = Q_3 - Q_1
$$

Se utiliza para medir la dispersión de la parte central de los datos y detectar valores atípicos.

### 4.1. Ejemplo en Python (Cuartiles y Percentiles)

```python
import numpy as np

datos = [12, 15, 17, 20, 22, 25, 28, 30, 35, 40, 45, 50]

q1 = np.percentile(datos, 25)
q3 = np.percentile(datos, 75)
iqr = q3 - q1

print(f"Q1: {q1}, Q3: {q3}, IQR: {iqr}")
```

[Código completo: code-04-cuartiles-percentiles.py](codes/code-04-cuartiles-percentiles.py)

---

## 5. Diagramas de cajas y bigotes (Boxplots)

El **diagrama de cajas y bigotes** es una representación gráfica basada en los cinco números resumen: mínimo, $Q_1$, mediana, $Q_3$ y máximo. Permite visualizar:

1. La dispersión y simetría de los datos.
2. La ubicación de la mediana.
3. La presencia de **valores atípicos (outliers)** (valore fuera de $1.5 \cdot IQR$).

### 5.1. Ejemplo en Python (Boxplot)

```python
import matplotlib.pyplot as plt
import seaborn as sns

datos = [10, 12, 15, 14, 13, 11, 12, 100] # 100 es un outlier
sns.boxplot(x=datos)
plt.show()
```

[Código completo: code-05-boxplot.py](codes/code-05-boxplot.py)

---

## 6. Cálculos datos agrupados

Cuando los datos se presentan en tablas de frecuencia con intervalos, las formulas se ajustan utilizando la **marca de clase ($x_i$)** (punto medio del intervalo) y la **frecuencia absoluta ($f_i$)**.

### 6.1. Media para datos agrupados

$$
\bar{x} = \frac{\sum f_i x_i}{n}
$$

### 6.2. Varianza para datos agrupados

$$
s^2 = \frac{\sum f_i (x_i - \bar{x})^2}{n - 1}
$$

### 6.3. Desviación estándar

$$
s = \sqrt{s^2}
$$

### 6.4. Coeficiente de variación

$$
CV = \left( \frac{s}{|\bar{x}|} \right) \cdot 100\%
$$

### 6.5. Medidas de posición para datos agrupados

Para calcular la mediana, los cuartiles o los percentiles en datos agrupados, se utiliza la siguiente fórmula general:

$$
M_k = L_i + \left( \frac{\frac{k \cdot n}{N} - F_{i-1}}{f_i} \right) \cdot a_i
$$

Donde:

- $L_i$: Límite inferior de la clase donde se encuentra la medida.
- $k \cdot n / N$: Posición de la medida (ej. $n/2$ para la mediana, $n/4$ para $Q_1$).
- $F_{i-1}$: Frecuencia absoluta acumulada de la clase anterior.
- $f_i$: Frecuencia absoluta de la clase actual.
- $a_i$: Amplitud del intervalo (ancho de clase).

### 6.6. Ejemplo en Python (Datos Agrupados)

#### Cálculos de tendencia y dispersión

[Código completo: code-06-datos-agrupados.py](codes/code-06-datos-agrupados.py)

#### Cálculos de posición (Mediana, Cuartiles y Percentiles)

[Código completo: code-07-posicion-agrupados.py](codes/code-07-posicion-agrupados.py)

---

## Referencias

1. Devore, J. L. (2012). *Probabilidad y estadística para ingeniería y ciencias* (7a ed.). Cengage Learning.
2. Walpole, R. E., Myers, R. H., Myers, S. L., & Ye, K. (2012). *Probabilidad y estadística para ingeniería y ciencias* (8a ed.). Pearson.
3. Mendenhall, W., Beaver, R. J., & Beaver, B. M. (2010). *Introducción a la probabilidad y estadística* (13a ed.). Cengage Learning.
4. Bruce, P., Bruce, A., & Gedeck, P. (2020). *Practical Statistics for Data Scientists: 50+ Essential Concepts Using R and Python* (2nd ed.). O’Reilly Media.
