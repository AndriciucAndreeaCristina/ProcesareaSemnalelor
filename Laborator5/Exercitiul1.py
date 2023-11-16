import numpy as np
import matplotlib.pyplot as plt


x = np.genfromtxt("D:/facultate/ProcesareaSemnalelor/Laborator5/Train.csv", delimiter=',', skip_header=1)
N = len(x)
# a
# avem cate o valoare pentru fiecare ora din zi, pentru 762 de zile, adica 1 an si o luna
# avem deci 1 esantion/ora, adica 0.0166 esantioane/minut, deci 0,002766 esantioane/secunda
# frecventa de esantionare este de 0,002766

# b
# esantionale din fisier acopera 762 de zile, adica 2 ani si o luna

# c
# stim ca un semnal este esantionat corect daca frecventa de esantionare este de cel putin dublul frecventei maxime a semnalului
# frecventa de esantionare este 0.002766 Hz, deci frecventa maxima a semnalului poate fi maxim 0.001383

# d
fs = 1 / 3600
signal = np.array(x[1:, 2])
X = np.fft.fft(signal)
X = abs(X/N)
X = X[0:int(N/2)]
f = fs * np.linspace(0, N/2, N//2)/N
plt.plot(X)
plt.yscale("log")
# plt.savefig("L5_1d.pdf", format="pdf", bbox_inches="tight")
# plt.savefig("L5_1d.png", format="png", bbox_inches="tight")
plt.show()

# e
med = np.median(signal)
if med != 0:
    print("Semnalul are o componenta continua")
    signal = signal - med
else:
    print("Semnalul nu are o componenta continua")
# X = np.fft.fft(signal)

# f
max_indexes = np.argsort(X)[-4:]
max_vals = X[max_indexes]
max_freqs = f[max_indexes]

print(max_vals)
print(max_freqs)

# g
start = 1056
month = x[start : start + 24 * 30]
print(month[:,2])
plt.plot(month[:,2], color = "red")
plt.savefig("L5_1g.pdf", format="pdf", bbox_inches="tight")
plt.savefig("L5_1g.png", format="png", bbox_inches="tight")
plt.show()
