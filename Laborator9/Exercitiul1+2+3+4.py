import numpy as np
import random

import pandas as pd
from matplotlib import pyplot as plt
from statsmodels.tsa.statespace.exponential_smoothing import ExponentialSmoothing

N = 1000
left = 1
right = 15
time = np.linspace(0, 1, N)
a = random.randint(left, right)
b = random.randint(left, right)
c = random.randint(left, right)
trend = a * time * time + b * time + c

fs1 = 2
fs2 = 5
component1 = np.sin(2 * np.pi * fs1 * time)
component2 = 0.5 * np.sin(2 * np.pi * fs2 * time)
season = component1 + component2
variation = np.random.normal(0, 1, N)

signal = trend + season + variation

# 2
new_signal = np.zeros(N)
alpha = 0.1
for t in range(N):
    new_value = 0
    for i in range(t):
        new_value += (1 - alpha) ** (t - i) * signal[i]
    new_signal[t] = alpha * new_value + (1-alpha) ** t * signal[0]

plt.plot(time, signal, label='Signal')
plt.plot(time, new_signal, label='New signal')
plt.savefig("L9_2a.pdf", format="pdf", bbox_inches="tight")
plt.savefig("L9_2a.png", format="png", bbox_inches="tight")
plt.legend()
plt.grid()
plt.show()

alpha_values = np.linspace(0, 1, 1000)
errors = np.zeros(1000)
optimal_alpha = -1
min_error = 10000000
for i in range(1000):
    new_signal = np.zeros(N)
    for t in range(N):
        new_value = 0
        for j in range(t):
            new_value += (1 - alpha_values[i]) ** (t - j) * signal[j]
        new_signal[t] = alpha_values[i] * new_value + (1 - alpha_values[i]) ** t * signal[0]
    errors[i] = np.mean(np.abs(signal - new_signal) ** 2)
    print(i)
    if errors[i] < min_error:
        min_error = errors[i]
        optimal_alpha = alpha_values[i]

print("Optimal alpha: ", optimal_alpha)
plt.plot(alpha_values, errors)
plt.grid()
plt.savefig("L9_2b.pdf", format="pdf", bbox_inches="tight")
plt.savefig("L9_2b.png", format="png", bbox_inches="tight")
plt.show()

# 3
mean = 0
std = 1
n = N
w = np.random.normal(mean, std, size=n)

new_signal = pd.Series(signal)
window_size = 3
windows = new_signal.rolling(window_size)

moving_averages = windows.mean()
plt.figure(figsize=(18, 6))
plt.plot(signal, label='Signal')
plt.plot(moving_averages, label='Moving average')
plt.title("Moving Average Series", fontsize=14)
plt.xlabel("Time", fontsize=14)
plt.ylabel("Signal", fontsize=14)
plt.legend()
plt.grid()
plt.savefig("L9_3a.pdf", format="pdf", bbox_inches="tight")
plt.savefig("L9_3a.png", format="png", bbox_inches="tight")
plt.show()