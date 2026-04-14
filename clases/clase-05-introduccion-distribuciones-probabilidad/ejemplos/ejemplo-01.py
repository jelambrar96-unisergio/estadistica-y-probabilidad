# comprobar si las siguientes expresiones son sriven como distribuciones de probbabilidad

epsilon = 1e-6

def comprobar(expresion, valores):
    if any(expresion(valor) < 0 for valor in valores):
        print("hay probabilidades negativas")
        return False
    suma = sum(expresion(valor) for valor in valores)
    if abs(suma - 1) > epsilon:
        print("la suma no es uno")
        print(f"la suma es {suma}")
        return False
    return True

expresion_1 = lambda x: (x - 2) / 2
valores_1 = [1, 2, 3, 4]

print("comprobado la expresion 1")
print(comprobar(expresion_1, valores_1))


expresion_2 = lambda x: x ** 2 / 25
valores_2 = range(5)

print("comprobado la expresion 2")
print(comprobar(expresion_2, valores_2))


expresion_3 = lambda x: (2*x + 1) / 50
valores_3 = range(1, 6)

print("comprobado la expresion 3")
print(comprobar(expresion_3, valores_3))
