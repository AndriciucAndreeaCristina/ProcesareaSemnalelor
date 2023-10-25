import numpy as np
import sounddevice as sd
from matplotlib import pyplot as plt
from scipy.io import wavfile
from scipy.signal import resample

fs1 = 44100
fs2 = 4*fs1
duration = 1
no_samples = int(duration * fs1)

time = np.linspace(0, duration, no_samples)
signal1 = 4 * np.sin(2 * np.pi * fs1 * time)
signal2 = np.sin(2 * np.pi * fs2 * time)
signal2 = resample(signal2, no_samples)

combined_signal = np.concatenate((signal1, signal2))
combined_time = np.concatenate((time, time))

plt.plot(combined_time, combined_signal)
plt.title("L2_5")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

wavfile.write('L2_5.wav', fs1, combined_signal)
sd.play(combined_signal, fs1)
sd.wait()

# se observa ca sunetele au frecventa diferita, al doilea fiind mai rapid decat primul
# durata semnalelor combinate este de 2 secunde