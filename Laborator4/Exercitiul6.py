import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from scipy.signal import spectrogram

rate, data = wavfile.read('vowels.wav')
print(f"number of channels = {data.shape[1]}")
length = data.shape[0] / rate
print(f"length = {length}s")

size = int(0.01 * rate)
overlap = size // 2
frequencies, times, Sxx = spectrogram(data[:, 0], fs=rate, nperseg=size, noverlap=overlap)

# Plot the spectrogram
plt.figure(figsize=(10, 6))
plt.imshow(10 * np.log10(Sxx), cmap='viridis', aspect='auto')
plt.colorbar(label='Amplitudine (dB)')
plt.title('Spectrograma Semnalului Audio')
plt.xlabel('Timp (s)')
plt.ylabel('Frecvență (Hz)')
plt.savefig("L4_6.pdf", format="pdf", bbox_inches="tight")
plt.savefig("L4_6.png", format="png", bbox_inches="tight")
plt.show()