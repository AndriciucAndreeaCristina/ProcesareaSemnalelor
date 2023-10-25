import numpy as np
import sounddevice
import sounddevice as sd
from scipy.io import wavfile
import scipy.signal

fs_audio = 44100
no_samples = 1600
fs = 400

# generam axa reala
time = np.linspace(0, no_samples/fs_audio, no_samples)
signal = np.sin(2 * np.pi * fs * time)
wavfile.write('L2_3a.wav', no_samples, signal)
x, signal = scipy.io.wavfile.read("L2_3a.wav")
sd.play(signal, fs_audio)
sd.wait()

# b. semnal sinusoidal care sa dureze 3 secunde

duration = 3
no_samples = int(duration * fs)
time = np.linspace(0, duration, no_samples)

signal = np.sin(2 * np.pi * fs * time)
wavfile.write('L2_3b.wav', no_samples, signal)
x, signal = scipy.io.wavfile.read("L2_3b.wav")
sd.play(signal, fs_audio)
sd.wait()

# c. un semnal de tip sawtooth de frecv 240 Hz
duration = 1
fs = 240
no_samples = int(duration * fs)
time = np.linspace(0, duration, no_samples)
sawtooth = 2 * (time * fs - np.floor(time * fs + 0.5))
wavfile.write('L2_3c.wav', no_samples, sawtooth)
x, signal = scipy.io.wavfile.read("L2_3c.wav")
sd.play(signal, fs_audio)
sd.wait()

# d. un semnal de tip square de frecventa 300 Hz
fs = 300
duration = 1
no_samples = int(duration * fs)
time = np.linspace(0, duration, no_samples)
square = np.sign(np.sin(2 * np.pi * fs * time))
wavfile.write('L2_3d.wav', no_samples, square)
x, signal = scipy.io.wavfile.read("L2_3d.wav")
sd.play(signal, fs_audio)
sd.wait()