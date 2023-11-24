from scipy import misc, ndimage
import numpy as np
import matplotlib.pyplot as plt

X = misc.face(gray=True)
plt.imshow(X, cmap=plt.cm.gray)
plt.show()

print(X.shape)

