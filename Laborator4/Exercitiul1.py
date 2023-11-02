import math
import numpy as np
import time
import matplotlib.pyplot as plt
import scipy.linalg

N_values = [8, 128, 256, 512, 1024, 2048, 4096, 8192]

plt.figure(figsize=(6, 6))
plt.yscale('log')

for N in N_values:
    for x in range(N):
        time_start_manual = time.time()
        matrix = [[0 for i in range(N)] for x in range(N)]
        for y in range(N):
            matrix[x][y] = (1 / np.sqrt(N)) * math.e**(2j * np.pi * x * y / N)
        time_end_manual = time.time()
        time_elapsed_manual = time_end_manual - time_start_manual

        time_start_dft = time.time()
        matrix_dft = scipy.linalg.dft(N)
        time_end_dft = time.time()
        time_elapsed_dft = time_end_dft - time_start_dft
        plt.plot(time_elapsed_manual, time_elapsed_dft)

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()