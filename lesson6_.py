import numpy as np
import cv2
# import pandas as pd
from matplotlib import ticker, pyplot as plt


img1=np.random.randint(0,255, size=(32,32,3))
img2=np.random.randint(0,255, size=(16,16,3))
img3=np.random.randint(0,255, size=(32,32))
img4=np.random.randint(0,255, size=(8,8))
fig, ax = plt.subplots(2,2, figsize=(8,6))
ax[0][0].imshow(img1)
ax[0][1].imshow(img2)
ax[1][0].imshow(img3, cmap='gray')
ax[1][1].imshow(img4, cmap='gray')

ax[1][1].yaxis.set_major_locator(ticker.NullLocator())
ax[1][1].xaxis.set_major_locator(ticker.NullLocator())
plt.suptitle("Título principal")
plt.tight_layout()
plt.show()