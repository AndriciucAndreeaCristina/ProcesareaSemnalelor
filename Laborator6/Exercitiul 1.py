import numpy as np
from matplotlib import pyplot as plt


def apply_convolution(x, h):
    N = len(x)
    M = len(h)
    y = np.zeros(N + M - 1)
    for n in range(N + M - 1):
        for k in range(M):
            if n - k >= 0 and n - k < N:
                y[n] += x[n - k] * h[k]
    return y


N = 100
x = np.random.rand(N)
h = x
fig, axs = plt.subplots(4, figsize=(12, 8))
axs[0].plot(x)
axs[0].set_title("x")

for i in range(3):
    x = apply_convolution(x, h)
    h = x
    axs[i + 1].plot(x)
    axs[i + 1].set_title("x convoluted " + str(i + 1) + " times")

plt.tight_layout()
plt.savefig("L6_1.pdf", format="pdf", bbox_inches="tight")
plt.savefig("L6_1.png", format="png", bbox_inches="tight")
plt.show()

# se observa ca vectorl x devine din ce in ce mai neted, filtrandu-se astfel zgomotul