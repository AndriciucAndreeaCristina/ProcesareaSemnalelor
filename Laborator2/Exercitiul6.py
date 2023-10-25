import numpy as np
import matplotlib.pyplot as plt

fs = 24
duration = 1
no_samples = int(duration * fs)
time = np.linspace(0, duration, no_samples)
frequencies = [fs/2, fs/4, 0]
signal = np.sin(2 * np.pi * fs * time)

fig, axs = plt.subplots(4)
axs[0].plot(time, signal)
axs[0].set_title(f"Semnal initial: f = {fs} Hz")
axs[0].grid(True)

for i, freq in enumerate(frequencies):
    signal = np.sin(2 * np.pi * freq * time)
    axs[i+1].plot(time, signal)
    axs[i+1].set_title(f"Semnal {chr(97+i)}: f = {freq} Hz")
    axs[i+1].grid(True)

plt.tight_layout()
plt.show()

# esantionarea nu se face suficient de rapid pentru a genera un semnal sinusoidal, fiind un semnal mai putin neted
# cu cat frecventa e mai scazuta, cu atat ne indepartam ami mult de forma originala a semnalului continuu.