import numpy as np
from matplotlib import pyplot as plt

fs = 200
time = 0.1
total_samples = int(0.1 * fs)
time = np.linspace(0, 0.1, total_samples)
time_2 = np.linspace(0, 0.1, 1000)
frequency = 400
signal_1 = np.sin(2 * np.pi * frequency * time)

fig, axs = plt.subplots(3, 1)
axs[0].stem(time, signal_1)
axs[0].plot(time, signal_1, color='blue')
axs[0].grid(True)

signal_2 = np.sin(2 * np.pi * (frequency ) * time)
axs[1].stem(time, signal_2)
axs[1].plot(time, signal_2, color='blue')
axs[1].grid(True)

signal_3 = np.sin(2 * np.pi * (frequency + fs) * time)
axs[2].stem(time, signal_3)
axs[2].plot(time, signal_3, color='blue')
axs[2].grid(True)
plt.show()