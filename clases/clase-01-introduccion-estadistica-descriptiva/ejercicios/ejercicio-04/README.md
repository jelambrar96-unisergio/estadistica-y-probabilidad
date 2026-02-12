# Ejercicio 1.2.23

En un estudio de ruptura de la urdimbre durante el tejido de telas (Technometrics, 1982: 63), se sometieron a prueba 100 muestras de hilo. Se determinó el número de ciclos de esfuerzo hasta ruptura para cada muestra de hilo y se obtuvieron los datos siguientes:

```python
DATOS = [
    86, 175, 157, 282, 38, 211, 497, 246, 393, 198, 146, 176, 220, 224, 337, 180, 182, 185, 396, 264, 251, 76, 42, 149, 65, 93, 423, 188, 203, 105, 653, 264, 321, 180, 151, 315, 185, 568, 829, 203, 98, 15, 180, 325, 341, 353, 229, 55, 239, 124, 249, 364, 198, 250, 40, 571, 400, 55, 236, 137, 400, 195, 38, 196, 40, 124, 338, 61, 286, 135, 292, 262, 20, 90, 135, 279, 290, 244, 194, 350, 131, 88, 61, 229, 597, 81, 398, 20, 277, 193, 169, 264, 121, 166, 246, 186, 71, 284, 143, 188
]
```

a. Construya un histograma de frecuencia relativa basado en los intervalos de clase `0-<100`, `100-<200`, . . . y comente sobre las características del histograma.

b. Construya un histograma basado en los siguientes intervalos de clase: `0-<50`, `50-<100`, `100-<150`, `150-<200`, `200-<300`, `300-<400`, `400-<500`, `500-<600` y `600-<900`.

c. Si las especificaciones de tejido requieren una resistencia a la ruptura de por lo menos 100 ciclos, ¿qué proporción de los especímenes de hilos en esta muestra sería considerada satisfactoria?

---
*Tomado de Devore, J. L. (2012). Probabilidad y estadística para ingeniería y ciencias- (7a ed.). Cengage Learning.*
