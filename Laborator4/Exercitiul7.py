
P_semnal_dB = 90
SNR_dB = 80
# SNR_dB = 10 * log_10(P_semnal / P_zgomot)
# SNR_dB = 10 * (log_10(P_semnal) - log_10(P_zgomot))
# SNR_dB = P_semnal_dB - P_zgomot_dB
# P_zgomot_dB = P_semnal_dB - SNR_dB
print(f"Puterea zgomotului este {P_semnal_dB - SNR_dB} dB")
