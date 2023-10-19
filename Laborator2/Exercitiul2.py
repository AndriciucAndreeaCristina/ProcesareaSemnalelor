import matplotlib.pyplot as plt
import numpy as np

plot = 1
phases = [np.pi/3, np.pi/2, (-1)*np.pi/2, 7*np.pi/3]
phases_strings = ['pi/3', 'pi/2', '-pi/2', '7*pi/3']

time = np.arange(0, 0.1, step = 0.0005)
noise = np.random.normal(0, 1, len(time))
snr = [0.1, 1, 10, 100]

for phi in phases:
    i = 1
    fig, axs = plt.subplots(len(snr) + 1)
    fig.suptitle("Semnal sinusoidal cu faza " + phases_strings[i] )
    sinus = np.sin(120 * np.pi * time + phi)
    axs[0].set_title("Semnal curat")
    axs[0].plot(time, sinus)
    for snr_i in snr:
        axs[i].set_title('SNR = ' + str(snr_i))
        gamma = np.sqrt(np.sum(sinus**2) / (snr_i * np.sum(noise**2)))
        noise_signal = sinus + gamma * noise
        axs[i].plot(time, noise_signal)
        i = i + 1
    plt.subplots_adjust(wspace=1, hspace=1.2)
    file_name = "L2_2" + str(plot) + ".pdf"
    plt.savefig(file_name, format="pdf", bbox_inches="tight")
    plt.show()
    plot = plot + 1



