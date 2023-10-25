import numpy as np
import matplotlib.pyplot as plt

fs_initial = 1000
duration = 1
no_samples = int(fs_initial * duration)

time_initial = np.linspace(0, duration, no_samples)
signal_initial = np.sin(2 * np.pi * 1000 * time_initial)

signal_decimated = signal_initial[::4]
time_decimated = time_initial[::4]

plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.stem(time_initial, signal_initial)
plt.title("Semnal Sinusoidal Inițial")
plt.xlabel("Timp (secunde)")
plt.ylabel("Amplitudine")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.stem(time_decimated, signal_decimated)
plt.title("Semnal Sinusoidal Decimat")
plt.xlabel("Timp (secunde)")
plt.ylabel("Amplitudine")
plt.grid(True)

plt.tight_layout()
plt.savefig("L2_7a.pdf", format="pdf", bbox_inches="tight")
plt.show()

# frecventa de esantionare este suficient de mare pentru a genera un semnal sinusoidal si daca renuntam la 3/4 din esantionae

signal_decimated = signal_initial[1::4]
time_decimated = time_initial[1::4]

plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.stem(time_initial, signal_initial)
plt.title("Semnal Sinusoidal Inițial")
plt.xlabel("Timp (secunde)")
plt.ylabel("Amplitudine")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.stem(time_decimated, signal_decimated)
plt.title("Semnal Sinusoidal Decimat")
plt.xlabel("Timp (secunde)")
plt.ylabel("Amplitudine")
plt.grid(True)

plt.savefig("L2_7b.pdf", format="pdf", bbox_inches="tight")
plt.tight_layout()
plt.show()

# incepand de la a doua valoare, graficul nu mai este centrat in 0 si are durata mai mica, dar isi pastreaza forma de sinusioda