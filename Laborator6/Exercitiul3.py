import numpy as np
import matplotlib.pyplot as plt

f = 100
A = 1
phi = 0
T = 1/f
Nw = 200
t = np.linspace(0, 1, Nw)
x = A * np.sin(2 * np.pi * f * t + phi)

w_rect = np.ones(Nw)
w_hann = np.hanning(Nw)

x_rect = x * w_rect
x_hann = x * w_hann

fig, axs = plt.subplots(4, figsize=(12, 8))
axs[0].plot(t, x)
axs[0].set_title('Semnalul original')
axs[0].set_xlabel('Timp (s)')
axs[0].set_ylabel('Amplitudine')

axs[1].plot(t, x_rect)
axs[1].set_title('Semnalul trecut prin fereastra dreptunghiulara')
axs[1].set_xlabel('Timp (s)')
axs[1].set_ylabel('Amplitudine')

axs[2].plot(t, x_hann)
axs[2].set_title('Semnalul trecut prin fereastra Hanning')
axs[2].set_xlabel('Timp (s)')
axs[2].set_ylabel('Amplitudine')

axs[3].plot(t, w_rect, label='Fereastra dreptunghiulara')
axs[3].plot(t, w_hann, label='Fereastra Hanning')
axs[3].set_title('Forma ferestrelor')
axs[3].set_xlabel('Timp (s)')
axs[3].set_ylabel('Amplitudine')

plt.legend()
plt.savefig("L6_3.pdf", format="pdf", bbox_inches="tight")
plt.savefig("L6_3.png", format="png", bbox_inches="tight")

plt.tight_layout()
plt.show()
