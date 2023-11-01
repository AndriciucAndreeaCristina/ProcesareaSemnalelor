import math
import matplotlib.pyplot as plt
import numpy as np

N = 8
matrix = [[0 for i in range(N)] for x in range(N)]

for x in range(N):
    for y in range(N):
        matrix[x][y] = (1 / np.sqrt(N)) * math.e**(2j * np.pi * x * y / N)

fig, axs = plt.subplots(8, figsize = (10, 6))
for x in range(N):
    real = [matrix[x][y].real for y in range(N)]
    img = [matrix[x][y].imag for y in range(N)]

    axs[x].plot(real, label='Real', color='red')
    axs[x].plot(img, label='Imaginary', color='green')
    axs[x].set_title(f'Row {x}')
plt.subplots_adjust(wspace=1.0, hspace=1.0)
plt.savefig("L3_1.pdf", format="pdf", bbox_inches="tight")
plt.savefig("L3_1.png", format="png", bbox_inches="tight")
plt.show()

fig, axs = plt.subplots(8, 2, figsize = (12, 10))
for x in range(N):
    real = [matrix[x][y].real for y in range(N)]
    img = [matrix[x][y].imag for y in range(N)]
    axs[x, 0].plot(real, label='Real', color='red')
    axs[x, 1].plot(img, label='Imaginary', color='green')
    axs[x, 0].set_title(f'Row {x}')
    axs[x, 1].set_title(f'Row {x}')

plt.subplots_adjust(wspace=0.8, hspace=0.9)
plt.show()

matrix = np.array(matrix)
matrix_h = np.conj(matrix.T)
result = np.dot(matrix_h, matrix)
if np.allclose(result, np.identity(N)):
    print("The Fourier matrix is orthogonal (np.allclose).")
else:
    print("The Fourier matrix is not orthogonal (np.allclose).")

identity = np.identity(matrix.shape[0])
difference_norm = np.linalg.norm(result - identity)
tolerance = 1e-10
is_unitary = difference_norm < tolerance

if is_unitary:
    print("The Fourier matrix is orthogonal (np.linalg.norm).")
else:
    print("The Fourier matrix is not orthogonal (np.linalg.norm).")