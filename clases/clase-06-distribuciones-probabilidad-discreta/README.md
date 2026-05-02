# Clase 06: Algunas distribuciones de probabilidad discretas

## 1. Distribución uniforme discreta

### 1.1. Introducción

La distribución uniforme discreta describe un experimento en el cual todos los resultados tienen la misma probabilidad. Es útil para modelar situaciones en las que no hay preferencia entre las opciones.

### 1.2. Definición matemática

Si una variable aleatoria discreta X toma valores en el conjunto finito:

$(\{a, a+1, \dots, b\})$,

con $a$ y $b$ enteros y $a \le b$, entonces:

$$
P(X = x) = \begin{cases}
\frac{1}{b-a+1} & \text{si } x \in \{a, a+1, \dots, b\} \\
0 & \text{en otro caso}
\end{cases}
$$

### 1.3. Características

- Media:

$$\mu = \frac{a+b}{2}$$

- Varianza:
  
$$\sigma^2 = \frac{(b-a+1)^2-1}{12}$$

### 1.4. Ejemplo de ejercicio

"Se lanza un dado no cargado y se observa el número de puntos. ¿Cuál es la probabilidad de obtener un valor impar?"

### 1.5. Ejemplo resuelto en Python

```python
from math import ceil

def probabilidad_impar(a=1, b=6):
    valores = list(range(a, b + 1))
    impares = [x for x in valores if x % 2 == 1]
    return len(impares) / len(valores)

print('Probabilidad de impar en un dado justo:', probabilidad_impar())
```

### 1.6. Código Python de ejemplo

```python
import numpy as np
import matplotlib.pyplot as plt

# Parámetros
a, b = 1, 6
x = np.arange(a, b + 1)
p = np.ones_like(x) / len(x)

plt.bar(x, p, color='skyblue')
plt.title('Distribución uniforme discreta: dado justo')
plt.xlabel('x')
plt.ylabel('P(X = x)')
plt.grid(axis='y', alpha=0.3)
plt.show()
```

---

## 3. Distribución Binomial

### 3.1. Introducción

La distribución binomial modela el número de éxitos en $n$ ensayos independientes de Bernoulli, cada uno con probabilidad $p$ de éxito.

### 3.2. Definición matemática

Para $k = 0, 1, \dots, n$:

$$
P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}
$$

### 3.3. Características

- Media:

$$\mu = np$$

- Varianza:

$$
\sigma^2 = np(1-p)
$$

### 3.4. Ejemplo de ejercicio

"Una moneda se lanza 10 veces con probabilidad de cara $p = 0.4$. ¿Cuál es la probabilidad de obtener exactamente 4 caras?"

### 3.5. Ejemplo resuelto en Python

```python
from math import comb

def binomial_prob(n, p, k):
    return comb(n, k) * p**k * (1 - p)**(n - k)

print('P(X = 4) con n = 10 y p = 0.4:', binomial_prob(10, 0.4, 4))
```

### 3.6. Código Python de ejemplo

```python
import numpy as np
import matplotlib.pyplot as plt
from math import comb

n = 10
ps = [0.2, 0.4, 0.7]
x = np.arange(0, n + 1)

plt.figure(figsize=(10, 4))
for p in ps:
    p_x = [comb(n, k) * p**k * (1 - p)**(n - k) for k in x]
    plt.plot(x, p_x, marker='o', label=f'p = {p}')

plt.title('Distribución Binomial para diferentes valores de p')
plt.xlabel('k (número de éxitos)')
plt.ylabel('P(X = k)')
plt.legend()
plt.grid(True)
plt.show()
```

---

## 5. Distribución Multinomial

### 5.1. Introducción

La distribución multinomial generaliza la binomial cuando hay más de dos categorías posibles en cada ensayo, como lanzar un dado o clasificar elementos en varias clases.

### 5.2. Definición matemática

Para $n$ ensayos y categorías con probabilidades $p_1, \dots, p_m$ que suman 1, la probabilidad de obtener los conteos $k_1, \dots, k_m$ es:

$$
P(X_1 = k_1, \dots, X_m = k_m) = \frac{n!}{k_1! \cdots k_m!} p_1^{k_1} \cdots p_m^{k_m}
$$

con

$$
\sum_{i=1}^m k_i = n
$$

### 5.3. Características

- Media:

$$
E[X_i] = n p_i
$$

para cada categoría $i$

- Varianza:

$$
\operatorname{Var}[X_i] = n p_i (1-p_i)
$$

### 5.4. Ejemplo de ejercicio

"En 5 lanzamientos de un dado, ¿cuál es la probabilidad de obtener exactamente 2 unos, 2 doses y 1 tres?"

### 5.5. Ejemplo resuelto en Python

```python
from math import factorial

def multinomial_prob(n, ps, ks):
    numer = factorial(n)
    denom = 1
    prod = 1
    for ki, pi in zip(ks, ps):
        denom *= factorial(ki)
        prod *= pi**ki
    return numer * prod / denom

print('P([2,2,1,0,0,0]) en 5 lanzamientos:', multinomial_prob(5, [1/6]*6, [2, 2, 1, 0, 0, 0]))
```

### 5.6. Código Python de ejemplo

```python
import numpy as np
import matplotlib.pyplot as plt
from math import factorial

n = 5
p = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]

# Ejemplo de una sola combinación: 2 unos, 2 doses, 1 tres, 0 demás
k = [2, 2, 1, 0, 0, 0]
multinomial_prob = factorial(n)
for ki, pi in zip(k, p):
    multinomial_prob *= pi**ki / factorial(ki)

print('Probabilidad de [2,2,1,0,0,0]:', multinomial_prob)
```

---

## 4. Distribución Binomial Negativa

### 4.1. Introducción

La distribución binomial negativa cuenta el número de ensayos necesarios hasta obtener un número fijo de éxitos. Es útil cuando se observa repetición de ensayos hasta alcanzar una meta.

### 4.2. Definición matemática

Si se desea obtener $r$ éxitos y la probabilidad de éxito en cada ensayo es $p$, entonces la probabilidad de que el $r$-ésimo éxito ocurra en el ensayo $k$ es:

$$
P(X = k) = \binom{k-1}{r-1} p^r (1-p)^{k-r}, \qquad k = r, r+1, r+2, \dots
$$

### 4.3. Características

- Media:

$$\mu = \frac{r}{p}$$

- Varianza:

$$\sigma^2 = \frac{r(1-p)}{p^2}$$

### 4.4. Ejemplo de ejercicio

"Se lanzan monedas hasta obtener 3 caras. ¿Cuál es la probabilidad de que se necesiten exactamente 7 lanzamientos?"

### 4.5. Ejemplo resuelto en Python

```python
from math import comb

def negative_binomial_prob(r, p, k):
    return comb(k - 1, r - 1) * p**r * (1 - p)**(k - r)

print('P(k = 7) con r = 3 y p = 0.5:', negative_binomial_prob(3, 0.5, 7))
```

### 4.6. Código Python de ejemplo

```python
import numpy as np
import matplotlib.pyplot as plt
from math import comb

r = 3
ps = [0.3, 0.5]
k = np.arange(r, r + 15)

plt.figure(figsize=(10, 4))
for p in ps:
    p_k = [comb(ki - 1, r - 1) * p**r * (1 - p)**(ki - r) for ki in k]
    plt.plot(k, p_k, marker='o', label=f'p = {p}')

plt.title('Distribución Binomial Negativa para diferentes valores de p')
plt.xlabel('k (ensayos hasta r éxitos)')
plt.ylabel('P(X = k)')
plt.legend()
plt.grid(True)
plt.show()
```

---

## 2. Distribución de Poisson

### 2.1. Introducción

La distribución de Poisson modela el número de eventos que ocurren en un intervalo fijo de tiempo o espacio cuando los eventos son raros e independientes.

### 2.2. Definición matemática

Si $\lambda > 0$ es la tasa promedio de ocurrencias, entonces:

$$
P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}, \qquad k = 0, 1, 2, \dots
$$

### 2.3. Características

- Media: $\mu = \lambda$

- Varianza: $\sigma^2 = \lambda$

### 2.4 Ejemplo de ejercicio

"En promedio se reciben 3 llamadas por hora a un centro de atención. ¿Cuál es la probabilidad de recibir exactamente 5 llamadas en una hora?"

### 2.5. Ejemplo resuelto en Python

```python
from math import exp, factorial

def poisson_prob(k, lam):
    return exp(-lam) * lam**k / factorial(k)

print('P(X = 5) con λ = 3:', poisson_prob(5, 3))
```

### 2.6. Código Python de ejemplo

```python
import numpy as np
import matplotlib.pyplot as plt
from math import exp, factorial

lambdas = [1, 3, 6]
k_max = 15
x = np.arange(0, k_max + 1)

plt.figure(figsize=(10, 4))
for lam in lambdas:
    p = [exp(-lam) * lam**k / factorial(k) for k in x]
    plt.plot(x, p, marker='o', label=f'λ = {lam}')

plt.title('Distribución de Poisson para diferentes valores de λ')
plt.xlabel('k')
plt.ylabel('P(X = k)')
plt.legend()
plt.grid(True)
plt.show()
```

---


## 6. Distribución Hipergeométrica

### 6.1. Introducción

La distribución hipergeométrica modela la probabilidad de éxitos en una muestra sin reemplazo tomada de una población finita que contiene éxitos y fracasos.

### 6.2. Definición matemática

Si la población tiene $N$ elementos, $K$ éxitos, y se extraen $n$ elementos sin reemplazo, entonces:

$$
P(X = k) = \frac{\binom{K}{k} \binom{N-K}{n-k}}{\binom{N}{n}}, \qquad \max(0, n-K) \le k \le \min(n, K)
$$

### 6.3. Características

- Media:

$$
\mu = n \frac{K}{N}
$$

- Varianza:

$$
\sigma^2 = n \frac{K}{N} \frac{N-K}{N} \frac{N-n}{N-1}
$$

### 6.4. Ejemplo de ejercicio

"En una urna con 10 bolas rojas y 15 bolas azules, se extraen 5 bolas sin reemplazo. ¿Cuál es la probabilidad de obtener exactamente 2 bolas rojas?"

### 6.5. Ejemplo resuelto en Python

```python
from math import comb

def hipergeo_prob(N, K, n, k):
    return comb(K, k) * comb(N-K, n-k) / comb(N, n)

print('P(X = 2) con N = 25, K = 10, n = 5:', hipergeo_prob(25, 10, 5, 2))
```

### 6.6. Código Python de ejemplo

```python
import numpy as np
import matplotlib.pyplot as plt
from math import comb

N, K, n = 25, 10, 5
x = np.arange(max(0, n-K), min(n, K) + 1)
p = [comb(K, k) * comb(N-K, n-k) / comb(N, n) for k in x]

plt.bar(x, p, color='salmon')
plt.title('Distribución Hipergeométrica')
plt.xlabel('k (éxitos en la muestra)')
plt.ylabel('P(X = k)')
plt.grid(axis='y', alpha=0.3)
plt.show()
```

---

## 7. Resumen de las distribuciones

| Distribución      | Uso principal                                     | Definición                                        | Media     | Varianza                                      |
|-------------------|---------------------------------------------------|---------------------------------------------------|-----------|-----------------------------------------------|
| Uniforme discreta | Experimentos con resultados igualmente probables  | $P(X=x)=1/(b-a+1)$                                | $(a+b)/2$ | $((b-a+1)^2-1)/12$                            |
| Binomial          | Conteo de éxitos en $n$ ensayos Bernoulli         | $\binom{n}{k}p^k(1-p)^{n-k}$                      | $np$      | $np(1-p)$                                     |
| Poisson           | Eventos raros en intervalo fijo                   | $e^{-\lambda} \lambda^k / k!$                     | $\lambda$ | $\lambda$                                     |
| Binomial negativa | Ensayos hasta $r$ éxitos                          | $\binom{k-1}{r-1}p^r(1-p)^{k-r}$                  | $r/p$     | $r(1-p)/p^2$                                  |
| Multinomial       | Conteos de múltiples categorías                   | $n!/(k_1!\cdots k_m!) p_1^{k_1}\cdots p_m^{k_m}$  | $np_i$    | $np_i(1-p_i)$                                 |
| Hipergeométrica   | Muestra sin reemplazo de población finita         | $\binom{K}{k}\binom{N-K}{n-k}/\binom{N}{n}$       | $nK/N$    | $n\frac{K}{N}\frac{N-K}{N}\frac{N-n}{N-1}$    |

### 7.1. Principales usos en contexto

- **Uniforme discreta**: juegos, sorteos, lanzamiento de dados.
- **Binomial**: calidad, ensayos con dos resultados, control de defectos.
- **Poisson**: llegadas, llamadas, eventos raros en tiempo/espacio.
- **Binomial negativa**: número de pruebas hasta lograr cierto número de éxitos.
- **Multinomial**: clasificación por categorías, resultados de múltiples opciones.
- **Hipergeométrica**: muestras sin reemplazo, poblaciones finitas y lotes.

### 7.2. Ejemplos resueltos recomendados

1. **Uniforme discreta**: calcular probabilidad de número impar al lanzar un dado.
2. **Poisson**: probabilidad de llamadas en un período fijo.
3. **Binomial**: exactas caras al lanzar una moneda varias veces.
4. **Binomial negativa**: probar hasta obtener un número fijo de éxitos.
5. **Multinomial**: contar resultados de un experimento con más de dos categorías.
6. **Hipergeométrica**: extraer muestras sin reemplazo de una urna finita.

---

Fin del capítulo.
