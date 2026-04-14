from scipy.stats import norm

esperanza = norm.expect(lambda x: x ** 2 + 2 * x + 3, loc=0, scale=1)
print(f"Valor Esperado (Media): {esperanza:.4f}")