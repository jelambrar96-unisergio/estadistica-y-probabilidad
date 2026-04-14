from scipy.stats import norm

# Definimos una distribución normal (media=0, desviación=1)
mu, sigma = 0, 1
# Calculamos la probabilidad de que X esté entre -1 y 1
prob_intervalo = norm.cdf(1, mu, sigma) - norm.cdf(-1, mu, sigma)

print(f"Probabilidad P(-1 < X < 1): {prob_intervalo:.4f}")
