import numpy as np
from matplotlib import ticker, pyplot as plt

x=np.linspace(-2.0*np.pi, 2.0*np.pi, 201)
y=np.sin(x)
z=np.cos(x)

fig, ax = plt.subplots()
ax.plot(x,y, color="red", label="Sine function")
ax.plot(x,z, color="green", label="Cosine function")


"""
Nesse caso estamos a mudar a posicão dos spines bottom e left. 
Se nos quisermos manter uma linha no limite teremos que usar o comando
ax.axhline(y=-1), que traz uma linha horizontal no ponto y=-1 cor padrão azul.
Para colocar o extremo máximo e dar a cor que queremos
# ax.axhline(y=ax.get_ylim()[0], color="black")
"""
ax.spines[["bottom", "left"]].set_position(("data",0))
# ax.spines[["top", "right"]].set_visible(False)
# ax.axhline(y=-1)
ax.axhline(y=ax.get_ylim()[0], color="black")
ax.axvline(x=ax.get_xlim()[0], color="black")
plt.suptitle("Plot of sine and cosine function")
plt.legend(loc=(0,0))
plt.tight_layout()
plt.show()
