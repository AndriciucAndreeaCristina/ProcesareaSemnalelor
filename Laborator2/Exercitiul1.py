import matplotlib.pyplot as plt
import numpy as np

time = np.arange(0, 0.1, step = 0.0005)
# semnal sinusoidal de tip sinus
# amplitudine = 1, frecv = 60, faza = pi/3
sinus = np.sin(120 * np.pi * time + np.pi/3)
# semnal sinusoidal de tip cosinus
# amplitudine = 1, frecv = 60, faza = pi/3 - pi/2 = -pi/6
cosinus = np.cos(120 * np.pi * time + np.pi/3 - np.pi/2)

fig, axs = plt.subplots(2)
fig.suptitle("Semnal sinusoidal")

axs[0].set_title('Semnal de tip sinus')
axs[0].plot(time, sinus)
axs[1].set_title('Semnal de tip cosinus')
axs[1].plot(time, cosinus)

plt.subplots_adjust(wspace=0.6, hspace=0.6)
plt.savefig("L2_1.pdf", format="pdf", bbox_inches="tight")
plt.show()