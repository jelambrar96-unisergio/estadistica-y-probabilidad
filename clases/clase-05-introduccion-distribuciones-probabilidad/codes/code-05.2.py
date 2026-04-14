import numpy as np

x = np.array([0, 1, 2, 3])
probabilidades = np.array([0.1, 0.2, 0.3, 0.4])

# funcion de valor esperado
func = lambda x: x ** 2

valor_esperado = np.sum(x * probabilidades)
print(f"Valor Esperado (Media): {valor_esperado}")

variaza_esperada = np.sum((x - valor_esperado) ** 2 * probabilidades)
print(f"Varianza Esperada: {variaza_esperada}")

valor_esperado_func = np.sum(func(x) * probabilidades)
print(f"Valor Esperado (Media): {valor_esperado_func}")
