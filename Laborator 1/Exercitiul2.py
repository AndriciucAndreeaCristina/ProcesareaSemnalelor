import numpy as np
import matplotlib.pyplot as plt

# a. semnal sinusoidal de frecventa 400Hz, care sa contina 1600 de esantioane
fs = 400
no_samples = 1600

# generam axa reala
time = np.linspace(0, no_samples/fs, no_samples)
signal = np.sin(2 * np.pi * fs * time)

plt.plot(time, signal, c='orange')
plt.title("2A")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.savefig("L1_2a.pdf", format="pdf", bbox_inches="tight")
plt.show()

# b. semnal sinusoidal care sa dureze 3 secunde
fs = 800
duration = 3
no_samples = int(duration * fs)
time = np.linspace(0, duration, no_samples)

signal = np.sin(2 * np.pi * fs * time)
# plt.plot(time, signal, c='orange')
plt.plot(time, signal, c='orange')
plt.title("2B")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.savefig("L1_2b.pdf", format="pdf", bbox_inches="tight")
plt.show()

# c. un semnal de tip sawtooth de frecv 240 Hz
fs = 240
duration = 1
no_samples = int(duration * fs)
time = np.linspace(0, duration, no_samples)
sawtooth = 2 * (time * fs - np.floor(time * fs + 0.5))
plt.plot(time, sawtooth, c='orange')
plt.title("2C")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.savefig("L1_2c.pdf", format="pdf", bbox_inches="tight")
plt.show()

# d. un semnal de tip square de frecventa 300 Hz
fs = 300
duration = 1
no_samples = int(duration * fs)
time = np.linspace(0, duration, no_samples)
square = np.sign(np.sin(2 * np.pi * fs * time))

plt.plot(time, square, c='orange')
plt.title("2D")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.savefig("L1_2d.pdf", format="pdf", bbox_inches="tight")
plt.show()

# e. un semnal 2d aleator
x = 128
y = 128
signal = np.random.rand(x, y)
plt.imshow(signal, cmap='viridis')
plt.title('Semnal 2D Aleator')
plt.colorbar()
plt.savefig("L1_2e.pdf", format="pdf", bbox_inches="tight")
plt.show()


# f. un semnal 2d particular
def checkerboard(n):
    checkerboard = np.kron(np.array([[0, 1], [1, 0]]), np.ones((n//2,  n//2)))
    return checkerboard


signal = checkerboard(128)
print(signal.shape)
plt.imshow(signal, cmap='viridis')
plt.title('Semnal 2D')
plt.colorbar()
plt.savefig("L1_2f.pdf", format="pdf", bbox_inches="tight")
plt.show()

