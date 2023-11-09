import numpy as np
import time
import matplotlib.pyplot as plt


N_values = [128, 256, 512, 1024, 2048, 4096, 8192]
time_manual = []
time_np = []
for N in N_values:
    t = np.linspace(0, 1, N)
    signal = np.cos(120 * np.pi * t + np.pi/3)
    matrix = []
    time_start_manual = time.time()
    for x in range(N):
        matrix.append([(np.exp(-1j * 2 * np.pi * x * y / N)) for y in range(N)])
    matrix = np.array(matrix)
    result = np.dot(matrix, signal)
    time_end_manual = time.time()
    time_man = time_end_manual - time_start_manual
    time_manual.append(time_man)

    time_start_np = time.time()
    result_np = np.fft.fft(signal)
    time_end_np = time.time()
    time_auto = time_end_np - time_start_np
    time_np.append(time_auto)

plt.plot(N_values, time_manual, color = 'blue')
plt.plot(N_values, time_np, color = 'orange')
plt.yscale('log')
# plt.grid(True)
plt.savefig("L4_1.pdf", format="pdf", bbox_inches="tight")
plt.savefig("L4_1.png", format="png", bbox_inches="tight")
plt.show()
