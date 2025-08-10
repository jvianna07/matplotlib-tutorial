from matplotlib import pyplot as plt
import numpy as np

# Dados de exemplo
valores = [4, 7, 3, 5, 6, 2, 8, 4]
categorias = len(valores)

# Ângulos igualmente espaçados
angulos = np.linspace(0, 2*np.pi, categorias, endpoint=False)

# Criando o gráfico polar
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})

# Criando as barras
barras = ax.bar(angulos, valores, width=2*np.pi/categorias, align='edge', edgecolor='white')

# Estilizar as barras (cor e transparência)
for barra in barras:
    barra.set_facecolor(plt.cm.viridis(np.random.rand()))
    barra.set_alpha(0.8)

# Remover grades e rótulos de ângulo
ax.set_yticklabels([])
ax.set_xticklabels([])

plt.show()