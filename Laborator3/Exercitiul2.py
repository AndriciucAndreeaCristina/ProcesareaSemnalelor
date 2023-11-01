import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fs = 10                             # frecventa fundamentala
samples = np.linspace(0, 1, 1000)    # 100 de esantioane intre 0 si 1
exponential = np.exp(-2*np.pi*1j*samples)
x = np.sin(2 * np.pi * fs * samples)
y = np.multiply(x, exponential)

y_real = [y[i].real for i in range(len(y))]
y_imag = [y[i].imag for i in range(len(y))]

plt.figure(figsize=(6, 6))
plt.plot(y_real, y_imag)
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.grid()
plt.savefig("L3_2a.pdf", format="pdf", bbox_inches="tight")
plt.savefig("L3_2a.png", format="png", bbox_inches="tight")
plt.show()

fig, axs = plt.subplots(2, 2, figsize = (10, 8))
omega = [1, 5, 7, fs]
for i in range(len(omega)):
    exponential = np.exp(-2*np.pi*1j*omega[i]*samples)
    y = np.multiply(x, exponential)
    y_real = [y[i].real for i in range(len(y))]
    y_imag = [y[i].imag for i in range(len(y))]
    row = i //2
    col = i % 2
    axs[row, col].plot(y_real, y_imag)
    axs[row, col].set_title(f'Omega = {omega[i]}')
    axs[row, col].set_xlabel('Real')
    axs[row, col].set_ylabel('Imaginary')
    axs[row, col].grid()

plt.subplots_adjust(wspace=0.8, hspace=0.9)
plt.savefig("L3_2b.pdf", format="pdf", bbox_inches="tight")
plt.savefig("L3_2b.png", format="png", bbox_inches="tight")
plt.show()


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('3D Scatter Plot')
ax.set_xlabel('Real Part')
ax.set_ylabel('Imaginary Part')
ax.set_zlabel('Distances')
for i in range(len(omega)):
    exponential = np.exp(-2*np.pi*1j*omega[i]*samples)
    y = np.multiply(x, exponential)
    y_real = [y_i.real for y_i in y]
    y_imag = [y_i.imag for y_i in y]
    distances = [np.abs(y_i) for y_i in y]
    ax.scatter(y_real, y_imag, distances, c=distances, cmap='viridis', marker='o')

plt.savefig("L3_2c.pdf", format="pdf", bbox_inches="tight")
plt.savefig("L3_2c.png", format="png", bbox_inches="tight")
plt.show()


