import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

x = np.genfromtxt("D:/facultate/ProcesareaSemnalelor/Laborator5/Train.csv", delimiter=',')
N = len(x)
# a
# avem cate o valoare pentru fiecare ora din zi, pentru 762 de zile, adica 1 an si o luna
# avem deci 1 esantion/ora, adica 0.0166 esantioane/minut, deci 0,002766 esantioane/secunda
# frecventa de esantionare este de 0,002766

# b
# esantionale din fisier acopera 762 de zile, adica 1 an si o luna
# fs = 1/T => T = 361,445 secunde

# c
# stim ca un semnal este esantionat corect daca frecventa de esantionare este de cel putin dublul frecventei maxime a semnalului
# frecventa de esantionare este 0.002766 Hz, deci frecventa maxima a semnalului poate fi maxim 0.001383

# d
fs = 0.002766
signal = np.array(x[1:, 2])
signal = [int(x) for x in signal]
X = np.fft.fft(signal)
X = abs(X/N)
print(X)
plt.plot(X)
plt.yscale("log")
plt.show()
# observam ca valoarea modului este semnificativa pentru frecventa 0Hz, deci putem spune ca avem si o componenta continua
f = fs*np.linspace(0, N, N-1)/N
print(f)
plt.plot(f, X)
plt.yscale("log")
plt.savefig("L5_1d.pdf", format="pdf", bbox_inches="tight")
plt.savefig("L5_1d.png", format="png", bbox_inches="tight")
plt.show()

# e

# f

# g

# h

# i