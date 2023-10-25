import numpy as np
import matplotlib.pyplot as plt

# semnal sinusoidal
fs_sin = 400
duration_sin = 1
no_samples_sin = int(duration_sin * fs_sin)
time_sin = np.linspace(0, duration_sin, no_samples_sin)
sin_signal = np.sin(2 * np.pi * fs_sin * time_sin)

# semnal sawtooth
fs_sawtooth = 400
duration_sawtooth = 1
no_samples_sawtooth = int(duration_sawtooth * fs_sawtooth)
time_sawtooth = np.linspace(0, duration_sawtooth, no_samples_sawtooth)
sawtooth_signal = 2 * (time_sawtooth * fs_sawtooth - np.floor(time_sawtooth * fs_sawtooth + 0.5))

sum_signal = sin_signal + sawtooth_signal

# Semnalul sinusoidal
plt.subplot(3, 1, 1)
plt.plot(time_sin, sin_signal, c='orange')
plt.title("Semnal sinusoidal")
plt.xlabel("Timp")
plt.ylabel("Amplitudine")
plt.grid(True)

# Semnalul sawtooth
plt.subplot(3, 1, 2)
plt.plot(time_sawtooth, sawtooth_signal, c='blue')
plt.title("Semnal sawtooth")
plt.xlabel("Timp")
plt.ylabel("Amplitudine")
plt.grid(True)

# Suma semnalelor
plt.subplot(3, 1, 3)
plt.plot(time_sin, sum_signal, c='green')
plt.title("Suma semnalelor")
plt.xlabel("Timp")
plt.ylabel("Amplitudine")
plt.grid(True)
plt.tight_layout()
plt.savefig("L2_4.pdf", format="pdf", bbox_inches="tight")
plt.show()
