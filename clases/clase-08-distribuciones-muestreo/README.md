# Clase 08: Distribuciones muestrales

## 1. Introducción: Muestreo aleatorio

El muestreo aleatorio es un proceso fundamental en estadística que consiste en seleccionar un subconjunto de individuos de una población de tal manera que cada miembro tenga una probabilidad conocida y no nula de ser incluido. Este método garantiza que la muestra sea representativa, permitiendo que las conclusiones obtenidas se generalicen a toda la población con un margen de error controlable.

---

## 2. Población y muestra

- **Población**: Es el conjunto total de elementos, individuos o medidas que comparten una característica común y que son el objeto de interés en un estudio.
- **Muestra**: Es un subconjunto representativo de la población que se extrae para su análisis. El estudio de la muestra permite inferir propiedades de la población completa de manera más eficiente y económica.

---

## 3. Algunos estadísticos importantes

Nuestro principal propósito al seleccionar muestras aleatorias consiste en obtener información acerca de los parámetros desconocidos de la población

Ahora, $\hat{p}$ es una función de los valores observados en la muestra aleatoria; ya que es posible tomar muchas muestras aleatorias de la misma población, esperaríamos que $\hat{p}$ varíe de una muestra a otra.

$\hat{p}$ es un valor de una variable aleatoria que representamos con P. Tal variable aleatoria se llama **estadístico**. Cualquier función de las variables aleatorias que forman una muestra aleatoria se llama estadístico.

La distribución de probabilidad de un estadístico se denomina distribución muestral.

### 3.1. Media muestral

$$
\bar{X} = \frac{1}{n} \sum_{i=1}^n X_i
$$

```python
import numpy as np

# Ejemplo de cálculo de media muestral
muestra = [1.2, 2.4, 3.1, 2.8, 2.5]
media_muestral = np.mean(muestra)
print(f"Media muestral: {media_muestral}")
```

### 3.2. Varianza muestral

$$
S^2 = \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X})^2
$$

```python
# Ejemplo de cálculo de varianza muestral (ddof=1 para n-1)
varianza_muestral = np.var(muestra, ddof=1)
print(f"Varianza muestral: {varianza_muestral}")
```

---

## 4. Distribución muestral de la media

La primera distribución muestral importante a considerar es la de la media $\bar{X}$. Suponga que de una población normal con media $\mu$ y varianza $\sigma^2$ se toma una muestra aleatoria de $n$ observaciones. Cada observación $X_i$, $i = 1, 2,\dots, n$, de la muestra aleatoria tendrá entonces la misma distribución normal que la población de donde se tomó.

$$
\bar{X} = \frac{1}{n} \sum_{i=1}^n X_i
$$

Tiene una distribución normal con media $\mu$ y varianza $\sigma^2$.

$$
\mu_{\bar{X}} = \frac{1}{n} \sum_{i=1}^n \mu_i = \mu
$$

$$
\sigma^2_{\bar{X}} = \frac{1}{n^2} \sum_{i=1}^n \sigma^2_i = \frac{\sigma^2}{n}
$$

Si tomamos muestras de una población con distribución desconocida, ya sea finita o infinita, la distribución muestral de $\bar{X}$ aún será aproximadamente normal con media $\mu$ y varianza $\sigma^2/n$, siempre que el tamaño de la muestra sea grande. Este asombroso resultado es una consecuencia inmediata del siguiente teorema, que se conoce como **teorema del límite central**.

---

## 5. Teorema del límite central

Teorema del límite central: Si $\bar{X}$ es la media de una muestra aleatoria de tamaño $n$,
tomada de una población con media $\mu$ y varianza finita $\sigma^2$, entonces la forma límite de
la distribución de

$$
Z = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}}
$$

a medida que $n \to \infty$, es la distribución normal estándar $n(z; 0, 1)$.

La aproximación normal para $\bar{X}$ por lo general será buena si $n \ge 30$, siempre y
cuando la distribución de la población no sea muy asimétrica. Si $n < 30$, la aproxima-
ción será buena sólo si la población no es muy diferente de una distribución normal y,
como antes se estableció, si se sabe que la población es normal, la distribución muestral
de $\bar{X}$ seguirá siendo una distribución normal exacta, sin importar qué tan pequeño sea el
tamaño de las muestras.

### 5.1. Ejemplo de ejercicio

Partes para automóviles. Un importante proceso de fabricación produce partes de com-
ponentes cilíndricos para la industria automotriz. Es importante que el proceso produzca
partes que tengan un diámetro medio de 5.0 milímetros. El ingeniero implicado asume
que la media de la población es de 5.0 milímetros. Se lleva a cabo un experimento donde
se seleccionan al azar 100 partes elaboradas por el proceso y se mide el diámetro de cada
una de ellas. Se sabe que la desviación estándar de la población es σ = 0.1 milímetros.
El experimento indica un diámetro promedio muestral de x̄ = 5.027 milímetros. ¿Esta
información de la muestra parece apoyar o refutar la suposición del ingeniero?

**Solución en Python:**

```python
import numpy as np
from scipy import stats

# Parámetros poblacionales
mu = 5.0
sigma = 0.1
n = 100

# Resultado muestral
x_barra = 5.027

# Cálculo del estadístico Z
z = (x_barra - mu) / (sigma / np.sqrt(n))
print(f"Estadístico Z: {z:.3f}")

# Cálculo del valor p (dos colas)
p_value = 2 * (1 - stats.norm.cdf(abs(z)))
print(f"Valor p: {p_value:.4f}")

if p_value < 0.05:
    print("La evidencia refuta la suposición del ingeniero (α=0.05).")
else:
    print("La evidencia apoya la suposición del ingeniero (α=0.05).")
```

Como $z = 2.7$, el valor p es aproximadamente $0.0069$. Al ser menor que $0.05$, refutamos la suposición del ingeniero de que la media es $5.0$.

---

## 6. Distribución muestral de la diferencia entre dos medias

Si se extraen al azar muestras independientes de tamaños $n_1$ y $n_2$ de dos poblaciones,
discretas o continuas, con medias $\mu_1$ y $\mu_2$ y varianzas $\sigma^2_1$ y $\sigma^2_2$, respectivamente, entonces
la distribución muestral de las diferencias de las medias, $\bar{X}_1 - \bar{X}_2$, tiene una distribución
aproximadamente normal, con media y varianza dadas por

$$
\mu_{\bar{X}_1 - \bar{X}_2} = \mu_1 - \mu_2 \quad \text{y} \quad \sigma^2_{\bar{X}_1 - \bar{X}_2} = \frac{\sigma^2_1}{n_1} + \frac{\sigma^2_2}{n_2}
$$

De aquí,

$$
Z = \frac{(\bar{X}_1 - \bar{X}_2) - (\mu_1 - \mu_2)}{\sqrt{\frac{\sigma^2_1}{n_1} + \frac{\sigma^2_2}{n_2}}}
$$

es aproximadamente una variable normal estándar.

### 6.1. Ejemplo de ejercicio

Tiempo de secado de pinturas. Se llevan a cabo dos experimentos independientes en
los que se comparan dos tipos diferentes de pintura, el A y el B. Con la pintura tipo A se
pintan 18 especímenes y se registra el tiempo (en horas) que cada uno tarda en secar. Lo
mismo se hace con la pintura tipo B. Se sabe que la desviación estándar de población de
ambas es 1.0.

Si se supone que los especímenes pintados se secan en el mismo tiempo medio con
los dos tipos de pintura, calcule $P ( \bar{X}_A - \bar{X}_B > 1.0)$, donde $\bar{X}_A$ y $\bar{X}_B$ son los tiempos
promedio de secado para muestras de tamaño $n_A = n_B = 18$.

**Solución en Python:**

```python
import numpy as np
from scipy import stats

# Parámetros (H0: muA - muB = 0)
n_A = n_B = 18
sigma_A = sigma_B = 1.0
diferencia_mu = 0

# Diferencia observada
diff_x_barra = 1.0

# Varianza de la diferencia de medias
sigma_diff = np.sqrt((sigma_A**2 / n_A) + (sigma_B**2 / n_B))

# Cálculo de Z
z = (diff_x_barra - diferencia_mu) / sigma_diff
print(f"Estadístico Z: {z:.3f}")

# Probabilidad P(diff > 1.0)
probabilidad = 1 - stats.norm.cdf(z)
print(f"P(X_A - X_B > 1.0): {probabilidad:.6f}")
```

Como $z \approx 3.0$, la probabilidad de que la diferencia de las medias sea mayor a 1.0 es aproximadamente $0.00135$.

---

## 7. Distribución muestral de $S^2$

Si $S^2$ es la varianza de una muestra aleatoria de tamaño $n$ que se toma de una población
normal que tiene la varianza $\sigma^2$, entonces el estadístico

$$
\chi^2 = \frac{(n-1)S^2}{\sigma^2}
$$

tiene una distribución chi cuadrada con $v = n – 1$ grados de libertad.

### 7.1. Ejemplo

Un fabricante de baterías para automóvil garantiza que su producto durará, en promedio,
3 años con una desviación estándar de 1 año. Si cinco de estas baterías tienen duraciones
de 1.9, 2.4, 3.0, 3.5 y 4.2 años, ¿el fabricante continuará convencido de que sus baterías
tienen una desviación estándar de 1 año? Suponga que las duraciones de las baterías siguen una distribución normal.

**Solución en Python:**

```python
import numpy as np
from scipy import stats

# Datos del problema
sigma_pob = 1.0
muestras = np.array([1.9, 2.4, 3.0, 3.5, 4.2])
n = len(muestras)

# Cálculo de la varianza muestral
s2 = np.var(muestras, ddof=1)
print(f"Varianza muestral (s^2): {s2:.4f}")

# Estadístico Chi-cuadrado
chi_cuadrado = (n - 1) * s2 / (sigma_pob**2)
print(f"Estadístico χ²: {chi_cuadrado:.4f}")

# Grados de libertad
v = n - 1

# Probabilidad de observar un valor tan extremo (o más)
# Verificamos si cae en las colas (ej. area 0.05 y 0.95)
p_right = 1 - stats.chi2.cdf(chi_cuadrado, v)
p_left = stats.chi2.cdf(chi_cuadrado, v)

print(f"Probabilidad a la derecha: {p_right:.4f}")
print(f"Probabilidad a la izquierda: {p_left:.4f}")

# Valores críticos para α = 0.05
alpha = 0.05
val_crit_low = stats.chi2.ppf(alpha/2, v)
val_crit_high = stats.chi2.ppf(1 - alpha/2, v)

print(f"Rango de aceptación (α=0.05): [{val_crit_low:.4f}, {val_crit_high:.4f}]")

if val_crit_low <= chi_cuadrado <= val_crit_high:
    print("El fabricante puede continuar convencido.")
else:
    print("La evidencia sugiere que la desviación estándar podría ser diferente.")
```

Con una varianza muestral $s^2 \approx 0.815$ y $\chi^2 \approx 3.26$, el valor cae dentro del rango de aceptación $[0.484, 11.143]$. El fabricante puede seguir convencido.

---

### 8. La Distribución t de Student

Si se extrae una muestra aleatoria de tamaño $n$ de una población normal con media $\mu$ y varianza $\sigma^2$, entonces

$$

t = \frac{\bar{X} - \mu}{S/\sqrt{n}}
$$

tiene una distribución t de Student con $v = n – 1$ grados de libertad.

La distribución de T se parece a la distribución de Z en que ambas son simétricas al-
rededor de una media de cero. Ambas distribuciones tienen forma de campana, pero
la distribución t es más variable debido al hecho de que los valores T dependen de las
fluctuaciones de dos cantidades, $\bar{X}$ y $S^2$; mientras que los valores Z dependen sólo de
los cambios en $\bar{X}$ de una muestra a otra. La distribución de T difiere de la de Z en que la
varianza de T depende del tamaño de la muestra n y siempre es mayor que 1. Sólo cuando
el tamaño de la muestra $n \to \infty$ las dos distribuciones serán iguales. En la figura 8.8
se presenta la relación entre una distribución normal estándar ($v = \infty$) y las distribucio-
nes t con 2 y 5 grados de libertad.

### 8.1. Ejemplo

Un ingeniero químico afirma que el rendimiento medio de la población de un cierto
proceso de lotes es 500 gramos por mililitro de materia prima. Para verificar dicha afir-
mación muestrea 25 lotes cada mes. Si el valor t calculado cae entre –t0.05 y t0.05, queda
satisfecho con su afirmación. ¿Qué conclusión debería sacar de una muestra que tiene
una media x̄ = 518 gramos por mililitro y una desviación estándar muestral s = 40 gra-
mos? Suponga que la distribución de rendimientos es aproximadamente normal.

**Solución en Python:**

```python
import numpy as np
from scipy import stats

# Parámetros bajo la hipótesis nula
mu_h0 = 500
n = 25
alpha_crit = 0.05 # Área en la cola superior (t_0.05)

# Datos de la muestra
x_barra = 518
s = 40

# Cálculo del estadístico t
t_calc = (x_barra - mu_h0) / (s / np.sqrt(n))
print(f"Estadístico t calculado: {t_calc:.3f}")

# Grados de libertad
v = n - 1

# Valor crítico t_0.05 (área a la derecha = 0.05)
t_crit = stats.t.ppf(1 - alpha_crit, v)
print(f"Valor crítico t_0.05 (v={v}): {t_crit:.3f}")

if -t_crit <= t_calc <= t_crit:
    print("El valor t cae dentro del rango de aceptación. Se apoya la afirmación.")
else:
    print("El valor t cae fuera del rango. Se refuta la afirmación.")
```

Como $t = 2.25$ y el valor crítico $t_{0.05}$ para 24 grados de libertad es $1.711$, el valor calculado cae en la región de rechazo. El ingeniero debe rechazar su afirmación.

### 8.2. ¿Para qué se usa la distribución t de Student?

Se utiliza para estimar la media de una población cuando el tamaño de la muestra es pequeño ($n < 30$) y la desviación estándar de la población es desconocida. También se utiliza para realizar pruebas de hipótesis sobre la media de una población cuando el tamaño de la muestra es pequeño y la desviación estándar de la población es desconocida.

---

## 9. La distribución F

La distribución F tiene una amplia aplicación en la com-
paración de varianzas muestrales y también es aplicable en problemas que implican dos
o más muestras.
El estadístico F se define como el cociente de dos variables aleatorias chi cuadrada
independientes, dividida cada una entre su número de grados de libertad. En consecuen-
cia, podemos escribir

$$

F = \frac{U/v_1}{V/v_2}

$$

donde $U$ y $V$ son variables aleatorias independientes que tienen distribuciones chi cua-
drada con $v_1$ y $v_2$ grados de libertad, respectivamente. Estableceremos ahora la distribu-
ción muestral de F.

### 9.1 Definición

Sean U y V dos variables aleatorias independientes que tienen distribuciones chi cuadra-
da con v1 y v2 grados de libertad, respectivamente. Entonces, la distribución de la varia-

ble aleatoria F = V /v 1 es dada por la función de densidad

$$
f(f) = \frac{\Gamma \left( \frac{\nu_1 + \nu_2}{2} \right)}{\Gamma \left( \frac{\nu_1}{2} \right) \Gamma \left( \frac{\nu_2}{2} \right)} \left( \frac{\nu_1}{\nu_2} \right)^{\nu_1/2} \frac{f^{\nu_1/2-1}}{\left( 1 + \frac{\nu_1}{\nu_2} f \right)^{(\nu_1 + \nu_2)/2}}, \quad f > 0
$$

Ésta se conoce como la distribución F con $v_1$ y $v_2$ grados de libertad (g.l.).

Sea $f_\alpha$ el valor f por arriba del cual encontramos un área igual a α. Esto se ilustra
mediante la región sombreada de la figura 8.12. La tabla A.6 proporciona valores de $f_\alpha$
sólo para α = 0.05 y α = 0.01 para varias combinaciones de los grados de libertad $v_1$
y $v_2$. Por lo tanto, el valor f con 6 y 10 grados de libertad, que deja un área de 0.05 a la
derecha, es $f_{0.05} = 3.22$. Por medio del siguiente teorema, la tabla A.6 también se puede
utilizar para encontrar valores de $f_{0.95}$ y $f_{0.99}$.

Al escribir fα (v1, v2) para fα con v1 y v2 grados de libertad, obtenemos

$$
f_{1-\alpha}(v_1, v_2) = \frac{1}{f_{\alpha}(v_2, v_1)}
$$

**Uso de la distribución F en Python:**

```python
from scipy import stats

v1 = 6
v2 = 10
alpha = 0.05

# Encontrar f_0.05 (valor que deja 0.05 a la derecha)
f_005 = stats.f.ppf(1 - alpha, v1, v2)
print(f"f_0.05(6, 10): {f_005:.3f}")

# Encontrar f_0.95 usando el teorema: 1 / f_0.05(10, 6)
f_095_directo = stats.f.ppf(alpha, v1, v2)
f_095_teorema = 1 / stats.f.ppf(1 - alpha, v2, v1)

print(f"f_0.95(6, 10) directo: {f_095_directo:.4f}")
print(f"f_0.95(6, 10) teorema: {f_095_teorema:.4f}")
```

### 9.2. La distribución F con dos varianzas muestrales

Si $S^2_1$ y $S^2_2$ son las varianzas de muestras aleatorias independientes de tamaños $n_1$ y $n_2$, respectivamente, que se extraen de poblaciones normales con varianzas $\sigma^2_1$ y $\sigma^2_2$, entonces el estadístico

$$
F = \frac{S^2_1 / \sigma^2_1}{S^2_2 / \sigma^2_2}
$$

tiene una distribución F con $v_1 = n_1 - 1$ y $v_2 = n_2 - 1$ grados de libertad.

### 9.3. Para qué se usa la distribución F

Se utiliza para comparar las varianzas de dos poblaciones normales. También se utiliza para realizar pruebas de hipótesis sobre las varianzas de dos poblaciones normales.

---

Fin.
