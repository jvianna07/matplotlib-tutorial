from matplotlib.patches import FancyBboxPatch
from matplotlib import pyplot as plt

# Dados
categorias = ["A", "B", "C", "D"]
valores = [5, 7, 3, 6]

# Criar figura
fig, ax = plt.subplots()

# Largura das barras
width = 0.5

# Plotar barras com cantos arredondados
for i, valor in enumerate(valores):
    bar = FancyBboxPatch(
        (i - width/2, 0),   # posição (x, y)
        width,              # largura
        valor,              # altura
        boxstyle="round,pad=0.02,rounding_size=0.2",  # cantos arredondados
        ec="black",         # cor da borda
        fc="skyblue"        # cor de preenchimento
    )
    ax.add_patch(bar)

# Ajustar limites e rótulos
ax.set_xlim(-0.5, len(categorias) - 0.5)
ax.set_ylim(0, max(valores) + 1)
ax.set_xticks(range(len(categorias)))
ax.set_xticklabels(categorias)

plt.show()
