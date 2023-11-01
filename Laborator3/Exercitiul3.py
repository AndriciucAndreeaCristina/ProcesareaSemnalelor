import matplotlib.pyplot as plt
import numpy as np

fs1 = 2
fs2 = 5
fs3 = 10
time = np.linspace(0, 1, 1000)
component1 = np.sin(2 * np.pi * fs1 * time)
component2 = 0.5 * np.sin(2 * np.pi * fs2 * time)
component3 = 0.2 * np.sin(2 * np.pi * fs3 * time)

signal = component1 + component2 + component3
N = 1000
fig, axs = plt.subplots(2, figsize = (10, 8))

axs[0].plot(time, signal)
axs[0].set_title('Signal')
axs[0].set_xlabel('Time')
axs[0].set_ylabel('x(t)')
axs[0].grid()

omega = [i for i in range(0, 12)]
for i in range(len(omega)):
    function = [xn * (np.exp(-2 * np.pi * 1j * omega[i] * k / N)) for k, xn in enumerate(signal)]
    axs[1].stem(omega[i], abs(np.sum(function)))

axs[1].set_xlabel('Frequency (ω)')
axs[1].set_ylabel('Magnitude')
axs[1].grid()
plt.subplots_adjust(wspace=0.6, hspace=0.8)
plt.savefig("L3_3.pdf", format="pdf", bbox_inches="tight")
plt.savefig("L3_3.png", format="png", bbox_inches="tight")
plt.show()