from scipy import misc, ndimage
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

X = misc.face(gray=True)
X_fft = np.fft.fft2(X)
freq_db = 20 * np.log10(np.abs(X_fft))
SNR = 50
freq_cutoff = np.max(freq_db) - SNR
Y_cutoff = X_fft.copy()
Y_cutoff[freq_db > freq_cutoff] = 0
X_cutoff = np.fft.ifft2(Y_cutoff).real

noise = X_cutoff - X
plt.imshow(noise, cmap=plt.cm.gray)
plt.title("Noise")
plt.show()

SNR_X = 20 * np.log10(np.mean(X) / np.std(X))
SNR_X_cutoff = 20 * np.log10(np.mean(X_cutoff) / np.std(X_cutoff))
print("SNR_X: ", SNR_X)
print("SNR_X_cutoff: ", SNR_X_cutoff)
