# Ejercicios 2.61 y 2.62

En 58 especímenes de una nueva aleación de aluminio, que se desarrolla como material para la siguiente generación de aeronaves, se midió la resistencia a la compresión.

```python
DATOS = [
    66.4, 69.2, 70.0, 71.0, 71.9, 74.2, 67.7, 69.3, 70.1, 71.1, 72.1, 74.5, 68.0, 69.3, 70.2, 71.2,
    72.2, 75.3, 68.0, 69.5, 70.3, 71.3, 72.3, 68.3, 69.5, 70.3, 71.3, 72.4, 68.4, 69.6, 70.4, 71.5,
    72.6, 68.6, 69.7, 70.5, 71.6, 72.7, 68.8, 69.8, 70.6, 71.6, 72.9, 68.9, 69.8, 70.6, 71.7, 73.1,
    69.0, 69.9, 70.8, 71.8, 73.3, 69.1, 70.0, 70.9, 71.8, 73.5
]
```

## 2.61 Elabore

a) Una tabla de frecuencias con los datos de resistencia de la aleación de aluminio, usando las clases `[66.0, 67.5)`, `[67.5, 69.0)`, `[69.0, 70.5)`, `[70.5, 72.0)`, `[72.0, 73.5)`, `[73.5, 75.0)`, `[75.0, 76.5)`, donde se excluyen los puntos extremos derechos.

b) Un histograma empleando la tabla de frecuencias del inciso a).

c) Una tabla de frecuencias con los datos de tiempo entre peticiones, usando los intervalos `[0, 2,500)`, `[2,500, 5,000)`, `[5,000, 10,000)`, `[10,000, 20,000)`, `[20,000, 40,000)`, `[40,000, 60,000)`, `[60,000, 80,000)`, donde se incluye el punto extremo izquierdo, pero no el punto extremo derecho.

d) Un histograma usando la tabla de frecuencias del inciso c). (Note que los intervalos no son iguales, así que iguale la altura del rectángulo correspondiente a la frecuencia dividida entre el ancho del intervalo).

---
*Tomado de Miller, I., & Freund, J. E. (2004). Probabilidad y estadística para ingenieros. Pearson Educación.*
