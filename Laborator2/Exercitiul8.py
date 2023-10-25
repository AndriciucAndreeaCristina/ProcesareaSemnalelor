import numpy as np
import matplotlib.pyplot as plt

alpha = np.linspace(-np.pi/2, np.pi/2, 1000)
sin_alpha = np.sin(alpha)
approx_alpha = alpha
pade_alpha = (alpha - (7 * alpha**3) / 60) / (1 + (alpha**2) / 20)

error = np.abs(sin_alpha - approx_alpha)
pade_error = np.abs(sin_alpha - pade_alpha)

plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(alpha, sin_alpha, label="sin(α)", color='b')
plt.plot(alpha, approx_alpha, label="α (Aproximare Taylor)", linestyle='--', color='r')
plt.plot(alpha, pade_alpha, label="Aproximare Pade", linestyle='-.', color='g')
plt.title("Compararea Aproximărilor cu sin(α)")
plt.xlabel("α")
plt.ylabel("Valoare")
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.yscale('log')
plt.plot(alpha, error, label="Eroare Aproximare Taylor", color='r')
plt.plot(alpha, pade_error, label="Eroare Aproximare Pade", color='g')
plt.title("Erori pe scală logaritmică")
plt.xlabel("α")
plt.ylabel("Eroare (log scale)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("L2_7b.pdf", format="pdf", bbox_inches="tight")
plt.show()
