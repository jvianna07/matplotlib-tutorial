import numpy as np
from matplotlib import ticker, pyplot as plt

x=np.arange(-4,4,00.1)
y=x**2

fig, ax = plt.subplots()

ax.plot(x,y, color='r', linewidth=3)
ax.spines[['left', 'bottom']].set_position(('data',0))
ax.spines[['right', 'top']].set_visible(False)

"""
COMO FUNCIONA O FILL BETWEEN?
(DOMINIO, LIM_SUPERIOR, LIM_INFERIOR)
"""
plt.fill_between(x,y+1, y-1, color=(.3, .9,.1,.25))
plt.show()