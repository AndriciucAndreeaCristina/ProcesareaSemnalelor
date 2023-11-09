import numpy as np
import matplotlib.pyplot as plt

# Parametrii semnalului inițial
f0 = 5  # Frecvența semnalului inițial


# Interval de timp și frecvență de eșantionare (cu Fs > 2*f0)
T = 1.0  # Durata semnalului
fs = 100  # Frecvența de eșantionare
no_samples = int(fs * T)
# Generăm intervalul de timp
t = np.linspace(0, T, no_samples, endpoint=False)
t_desen = np.linspace(0, T, 1000, endpoint=False)

# Semnalul sinusoidal inițial
x = np.sin(2 * np.pi * f0 * t)
x_desen = np.sin(2 * np.pi * f0 * t_desen)

# Frecvențe pentru semnalele amestecate
f1 = 25  # Frecvența semnalului 1
f2 = 45  # Frecvența semnalului 2

# Semnalele sinusoidale cu frecvențele f1 și f2
x1 = np.sin(2 * np.pi * f1 * t)
x1_desen = np.sin(2 * np.pi * f1 * t_desen)
x2 = np.sin(2 * np.pi * f2 * t)
x2_desen = np.sin(2 * np.pi * f2 * t_desen)

# Afișăm semnalele
fig, axs = plt.subplots(3, 1, figsize=(12, 6))
axs[0].plot(t_desen, x_desen, color='green')
axs[0].stem(t, x, 'b')
axs[1].plot(t_desen, x1_desen, color='green')
axs[1].stem(t, x1, 'b')
axs[2].plot(t_desen, x2_desen, color='green')
axs[2].stem(t, x2, 'b')
plt.tight_layout()
plt.savefig("L4_3.pdf", format="pdf", bbox_inches="tight")
plt.savefig("L4_3.png", format="png", bbox_inches="tight")
plt.show()
