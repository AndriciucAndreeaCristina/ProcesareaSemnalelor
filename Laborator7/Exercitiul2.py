from scipy import misc, ndimage
import numpy as np
import matplotlib.pyplot as plt

X = misc.face(gray=True)
plt.imshow(X, cmap=plt.cm.gray)
plt.show()

X_fft = np.fft.fft2(X)
freq_db = 20 * np.log10(np.abs(X_fft))
plt.imshow(freq_db, cmap=plt.cm.gray)
plt.show()

SNR = 50
freq_cutoff = np.max(freq_db) - SNR
Y_cutoff = X_fft.copy()
Y_cutoff[freq_db > freq_cutoff] = 0
X_cutoff = np.fft.ifft2(Y_cutoff).real
plt.imshow(X_cutoff, cmap=plt.cm.gray)
plt.savefig("Laborator7/L7_2.pdf", format="pdf", bbox_inches="tight")
plt.savefig("Laborator7/L7_2.png", format="png", bbox_inches="tight")
plt.show()