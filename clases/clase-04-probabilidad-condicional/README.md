# Clase 05 - Probabilidad condicional y Teorema de Bayes

## 1. Probabilidad condicional

Es la probabilidad de que ocurra un evento $A$, sabiendo que ya ha ocurrido (o se asume que ocurrió) otro evento $B$. Restringe el espacio muestral original a los resultados contenidos en $B$.
$$
P(A|B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0
$$

---

## 2. Regla de Bayes

Permite calcular la probabilidad de una causa (evento $A_i$) dado un efecto observado (evento $B$), basándose en el conocimiento previo de las probabilidades de las causas y las probabilidades del efecto dada cada causa.
Sea $A_1, A_2, \ldots, A_n$ una partición del espacio muestral:
$$
P(A_i|B) = \frac{P(B|A_i)P(A_i)}{\sum_{j=1}^{n} P(B|A_j)P(A_j)}
$$

![alt text](media/fig4_regla_bayes.png)

#### Ejemplo: Diagnóstico de una enfermedad rara

Supongamos que el 0.1% de los adultos padece una enfermedad rara ($A_1$). Se ha desarrollado una prueba de diagnóstico tal que:

* Si un individuo tiene la enfermedad, la prueba es positiva ($B$) el 99% de las veces ($P(B|A_1) = 0.99$).
* Si un individuo no tiene la enfermedad ($A_2$), la prueba es positiva el 2% de las veces ($P(B|A_2) = 0.02$).

Si un individuo seleccionado al azar da positivo, ¿cuál es la probabilidad de que realmente tenga la enfermedad?

![alt text](media/fig5_ejemplo_bayes.png)

$$
P(A_1|B) = \frac{P(B|A_1)P(A_1)}{P(B|A_1)P(A_1) + P(B|A_2)P(A_2)}
$$

$$
P(A_1|B) = \frac{(0.99)(0.001)}{(0.99)(0.001) + (0.02)(0.999)} = \frac{0.00099}{0.00099 + 0.01998} \approx 0.0472
$$

```python
# Probabilidades a priori
p_a1 = 0.001  # Tiene la enfermedad
p_a2 = 1 - p_a1  # No tiene la enfermedad

# Probabilidades condicionales (verosimilitud)
p_b_dado_a1 = 0.99  # Positivo dado que tiene la enfermedad
p_b_dado_a2 = 0.02  # Positivo dado que no tiene la enfermedad (falso positivo)

# Teorema de Bayes
p_a1_dado_b = (p_b_dado_a1 * p_a1) / (p_b_dado_a1 * p_a1 + p_b_dado_a2 * p_a2)

print(f"La probabilidad de tener la enfermedad dado un resultado positivo es: {p_a1_dado_b:.4f}")
```

```plain
La probabilidad de tener la enfermedad dado un resultado positivo es: 0.0472
```

Este resultado parece contraintuitivo; la prueba de diagnóstico parece tan precisa que es altamente probable que alguien con un resultado positivo de prueba tenga la enfermedad, mientras que la probabilidad condicional calculada es de sólo `0.0472`. Sin embargo, como la enfermedad es rara y la prueba es sólo moderadamente confiable, surgen más resultados positivos falsos que positivos verdaderos.

---

## Referencias

1. Devore, J. L. (2012). *Probabilidad y estadística para ingeniería y ciencias* (7a ed.). Cengage Learning.
2. Walpole, R. E., Myers, R. H., Myers, S. L., & Ye, K. (2012). *Probabilidad y estadística para ingeniería y ciencias* (8a ed.). Pearson.
3. Mendenhall, W., Beaver, R. J., & Beaver, B. M. (2010). *Introducción a la probabilidad y estadística* (13a ed.). Cengage Learning.
4. Bruce, P., Bruce, A., & Gedeck, P. (2020). *Practical Statistics for Data Scientists: 50+ Essential Concepts Using R and Python* (2nd ed.). O’Reilly Media.
