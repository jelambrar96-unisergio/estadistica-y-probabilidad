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
