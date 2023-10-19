import numpy as np
import matplotlib.pyplot as plt

"""
 a. Simulati axa reala de timp printr-un sir de numere suficient de apropiate, spre exemplu [0 : 0.0005 : 0.03].
"""

time = np.arange(0, 0.03 + 0.0005, step = 0.0005)
# functia arange returneaza o lista de valori egal spatiate din intervalul [0, 0.03+0.0005)


"""
  b. Construiti semnalele x(t), y(t), z(t) si afisati-le grafic, in cate un subplot
"""
n = 3

total_samples = int(0.03 * 200) # nr de sample-uri este durata de timp * frecventa cu care masuram (masuram 200 de sample-uri pe secunda)
samples = np.linspace(0, 0.03, total_samples)
# functia linspace returneaza total_samples numere echidistante din intervalul [0, 0.03]


def x(t):
    return np.cos(520 * np.pi * t + np.pi/3)


def y(t):
    return np.cos(280 * np.pi * t - np.pi/3)


def z(t):
    return np.cos(120 * np.pi * t + np.pi/3)


value_x = x(time)
value_y = y(time)
value_z = z(time)

fig, axs = plt.subplots(3)

fig.suptitle("1B")

axs[0].set_title('X')
axs[0].plot(time, value_x)
axs[1].set_title('Y')
axs[1].plot(time, value_y)
axs[2].set_title('Z')
axs[2].plot(time, value_z)

plt.subplots_adjust(wspace=0.6, hspace=0.6)
plt.savefig("L1_1b.pdf", format="pdf", bbox_inches="tight")
plt.show()

fig, axs = plt.subplots(n)
fig.suptitle('1C')
samples_x = x(samples)
samples_y = y(samples)
samples_z = z(samples)

axs[0].set_title('X')
axs[0].stem(samples, samples_x)

axs[1].set_title('Y')
axs[1].stem(samples, samples_y)

axs[2].set_title('Z')
axs[2].stem(samples, samples_z)

plt.subplots_adjust(wspace=0.6, hspace=0.6)
plt.savefig("L1_1c.pdf", format="pdf", bbox_inches="tight")
plt.show()
