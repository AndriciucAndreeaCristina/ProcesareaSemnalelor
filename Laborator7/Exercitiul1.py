from scipy import misc, ndimage
import numpy as np
import matplotlib.pyplot as plt

N = 100
x = np.linspace(0, 1, N, endpoint=True)
y = np.linspace(0, 1, N, endpoint=True)
X, Y = np.meshgrid(x, y)


def function_1(n1, n2):
    return np.sin(2 * np.pi * n1 + 3 * np.pi * n2)


signal = function_1(X, Y)
plt.imshow(signal, cmap='viridis')
plt.title("xn1,n2=sin(2πn1+3πn2)")
plt.colorbar()
plt.savefig("L7_1a.pdf", format="pdf", bbox_inches="tight")
plt.savefig("L7_1a.png", format="png", bbox_inches="tight")
plt.show()

def function_2(n1, n2):
    return np.sin(4 * np. pi * n1) + np.cos(6 * np.pi * n2)

signal = function_2(X, Y)
plt.imshow(signal, cmap='viridis')
plt.title("xn1,n2=sin(4πn1)+cos(6πn2)")
plt.colorbar()
plt.savefig("L7_1b.pdf", format="pdf", bbox_inches="tight")
plt.savefig("L7_1b.png", format="png", bbox_inches="tight")
plt.show()


def function_3(n1, n2):
    res = [[0 for i in range(len(n1))] for j in range(len(n2))]
    res[0][5] = 1
    res[0][N-5] = 1
    return np.array(res)


signal = function_3(x, y)
f = np.fft.irfft2(signal)
plt.imshow(f, cmap='viridis')
plt.title("xn1,n2=1, n1=0, n2=5 sau n2=N-5")
plt.colorbar()
plt.savefig("L7_1c.pdf", format="pdf", bbox_inches="tight")
plt.savefig("L7_1c.png", format="png", bbox_inches="tight")
plt.show()


def function_4(n1, n2):
    res = [[0 for i in range(len(n1))] for j in range(len(n2))]
    res[5][0] = 1
    res[N-5][0] = 1
    return np.array(res)

signal = function_4(x, y)
f = np.fft.irfft2(signal)
plt.imshow(f, cmap='viridis')
plt.title("xn1,n2=1, n1=5 sau n1=N-5, n2=0")
plt.colorbar()
plt.savefig("L7_1d.pdf", format="pdf", bbox_inches="tight")
plt.savefig("L7_1d.png", format="png", bbox_inches="tight")
plt.show()


def function_5(n1, n2):
    res = [[0 for i in range(len(n1))] for j in range(len(n2))]
    res[5][5] = 1
    res[N-5][N-5] = 1
    return np.array(res)


signal = function_5(x, y)
f = np.fft.irfft2(signal)
plt.imshow(f, cmap='viridis')
plt.title("xn1,n2=1, n1=5 sau n1=N-5, n2=5 sau n2=N-5")
plt.colorbar()
plt.savefig("L7_1e.pdf", format="pdf", bbox_inches="tight")
plt.savefig("L7_1e.png", format="png", bbox_inches="tight")
plt.show()
