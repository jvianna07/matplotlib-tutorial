import numpy as np
from matplotlib import ticker, pyplot as plt

n=21
theta = np.linspace(0, 2*np.pi, n)
heights = np.random.rand(n)

fig = plt.figure()
ax = plt.subplot(polar=True)
bar= ax.bar(theta,heights,
            # color='deeppink',
            color=plt.cm.jet_r(heights),
            edgecolor='k',
            width=.5, # Pode usar width=heights,
            bottom=0.25, #indica o raio interno
            alpha=.5)

ax.set_ylim([0,1.25])
ax.set_yticks([.25,.5,.75,1,1.25])
ax.set_rlabel_position(270)
fig.suptitle("Polar bar")
plt.tight_layout()
# plt.grid(False)
plt.show()