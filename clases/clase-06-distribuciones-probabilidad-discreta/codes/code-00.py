from math import ceil

def probabilidad_impar(a=1, b=6):
    valores = list(range(a, b + 1))
    impares = [x for x in valores if x % 2 == 1]
    return len(impares) / len(valores)

print('Probabilidad de impar en un dado justo:', probabilidad_impar())
