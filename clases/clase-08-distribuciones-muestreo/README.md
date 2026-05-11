# Clase 08: Distribuciones muestrales

## 1. Introducción: Muestreo aleatorio

## 2. Población y muestra

## 3. Algunos estadísticos importantes

Nuestro principal propósito al seleccionar muestras aleatorias consiste en obtener información acerca de los parámetros desconocidos de la población

Ahora, $p̂$ es una función de los valores observados en la muestra aleatoria; ya que es posible tomar muchas muestras aleatorias de la misma población, esperaríamos que $p̂$ varíe de una muestra a otra.

$p̂$ es un valor de una variable aleatoria que representamos con P. Tal variable aleatoria se llama **estadístico**. Cualquier función de las variables aleatorias que forman una muestra aleatoria se llama estadístico.

La distribución de probabilidad de un estadístico se denomina distribución muestral.

### 3.1. Media muestral

### 3.2. Varianza muestral

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

## 7. Distribución muestral de $S^2$

Si $S^2$ es la varianza de una muestra aleatoria de tamaño $n$ que se toma de una población
normal que tiene la varianza $\sigma^2$, entonces el estadístico

$$
\chi^2 = \frac{(n-1)S^2}{\sigma^2}
$$

tiene una distribución chi cuadrada con $v = n – 1$ grados de libertad.
