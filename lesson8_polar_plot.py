import numpy as np
from matplotlib import ticker, pyplot as plt

n=2001
f= np.pi
r=5

theta =np.linspace(0,20.0*f, n)
curve =r*np.cos(f*theta)

ax1 = plt.subplot(111,polar=True)

ax1.plot(theta, curve, color='deeppink', label='rose curve')
ax1.set_ylim([0,6])
ax1.set_yticks([1,3,6])
ax1.set_xticks(np.linspace(0,2.0*np.pi, 17)[:-1]) # O [:-1] é pra nao sobrescrever o zero
ax1.set_rlabel_position(270) # alinhamos ao eixo de 270 graus
plt.title("Rose plots")
plt.legend()
plt.show()