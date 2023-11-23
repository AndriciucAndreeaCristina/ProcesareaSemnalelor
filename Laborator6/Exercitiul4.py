import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy

data = pd.read_csv("D:/facultate/ProcesareaSemnalelor/Laborator6/Train.csv")
data['Datetime'] = pd.to_datetime(data['Datetime'], format='%d-%m-%Y %H:%M')

# a.
x = data[3096: 3096 + 24 * 3]
print(x)

# b.
w_list = [5, 9, 13, 17]
fig, axs = plt.subplots(5, figsize=(12, 8))
axs[0].plot(x['Count'])
axs[0].set_title('Semnalul original')
axs[0].set_xlabel('Timp (h)')
axs[0].set_ylabel('Numar de pasageri')
for i, w in enumerate(w_list):
  y = np.convolve(x['Count'], np.ones(w), 'valid') / w
  axs[i+1].plot(y)
  axs[i+1].set_title(f'Semnalul netezit cu fereastra de dimensiune {w}')
  axs[i+1].set_xlabel('Timp (h)')
  axs[i+1].set_ylabel('Numar de pasageri')

plt.savefig("L6_4b.pdf", format="pdf", bbox_inches="tight")
plt.savefig("L6_4b.png", format="png", bbox_inches="tight")

plt.tight_layout()
plt.show()

# c.
fs = 1 / 3600
f_nyquist = fs / 2
f_taiere = 1 / (3600 * 24)
f_norm = f_taiere / f_nyquist
print(f'Frecventa de taiere: {f_taiere} Hz')
print(f'Frecventa normalizata: {f_norm} Hz')
# d.
order = 5
rp = 5
b_butter, a_butter = scipy.signal.butter(order, f_norm, btype='low')
filtered_butter = scipy.signal.filtfilt(b_butter, a_butter, x['Count'])

b_cheby, a_cheby = scipy.signal.cheby1(order, rp, f_norm, btype='low')
filtered_cheby = scipy.signal.filtfilt(b_cheby, a_cheby, x['Count'])

# e.
fig, axs = plt.subplots(2, figsize=(12, 8))
axs[0].plot(x['ID'], x['Count'], color = 'green', label='Semnalul original')
axs[0].plot(x['ID'], filtered_butter, color = 'blue', label='Semnalul netezit')
axs[0].set_title('Semnalul netezit cu filtrul Butterworth')
axs[0].legend()

axs[1].plot(x['ID'], x['Count'], color = 'green', label='Semnalul original')
axs[1].plot(x['ID'], filtered_cheby, color = 'blue', label='Semnalul netezit')
axs[1].set_title('Semnalul netezit cu filtrul Chebyshev')
axs[1].legend()

plt.savefig("L6_4d.pdf", format="pdf", bbox_inches="tight")
plt.savefig("L6_4d.png", format="png", bbox_inches="tight")
plt.show()


# f.
N_list = [3, 5, 7]
rp_list = [3, 5, 7]
fig, axs = plt.subplots (len(N_list), len(rp_list), figsize=(15, 10))
for i, N in enumerate(N_list):
  for j, rp in enumerate(rp_list):
    b_butter, a_butter = scipy.signal.butter(N, f_norm, btype='low')
    b_cheby, a_cheby = scipy.signal.cheby1 (N, rp, f_norm, btype='low')

    filtered_butter = scipy.signal.filtfilt(b_butter, a_butter, x['Count'])
    filtered_cheby = scipy.signal.filtfilt(b_cheby, a_cheby, x['Count'])

    axs[i, j].plot(x['ID'], filtered_butter, color = 'blue', label='Butterworth')
    axs[i, j].plot(x['ID'], filtered_cheby, color = 'green', label='Chebyshev')
    axs[i, j].set_title(f'Filtre de ordin {N} si atenuare {rp} dB')
    axs[i, j].set_xlabel('Frecventa (Hz)')
    axs[i, j].set_ylabel('Amplitudine (dB)')
    axs[i, j].grid(True)
    axs[i, j].legend()

fig.tight_layout()
plt.savefig("L6_4f.pdf", format="pdf", bbox_inches="tight")
plt.savefig("L6_4f.png", format="png", bbox_inches="tight")
plt.show()