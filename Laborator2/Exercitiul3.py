import numpy as np
import sounddevice as sd
import scipy.io.wavfile
import scipy.signal

fs = 44100
no_samples = 16000*4

# generam axa reala
time = np.linspace(0, no_samples/fs, no_samples)
signal = np.sin(2 * np.pi * fs * time)
sd.play(signal, fs)
sd.wait()



# b. semnal sinusoidal care sa dureze 3 secunde
fs = 44100
duration = 3
no_samples = int(duration * fs)
time = np.linspace(0, duration, no_samples)

signal = np.sin(2 * np.pi * fs * time)
sd.play(signal, fs)
sd.wait()

# c. un semnal de tip sawtooth de frecv 240 Hz
fs = 44100
duration = 1
no_samples = int(duration * fs)
time = np.linspace(0, duration, no_samples)
sawtooth = 2 * (time * fs - np.floor(time * fs + 0.5))
sd.play(signal, fs)
sd.wait()
# d. un semnal de tip square de frecventa 300 Hz
fs = 44100
duration = 1
no_samples = int(duration * fs)
time = np.linspace(0, duration, no_samples)
square = np.sign(np.sin(2 * np.pi * fs * time))
sd.play(signal, fs)
sd.wait()