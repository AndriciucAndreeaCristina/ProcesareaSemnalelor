import numpy as np

N = 5
max_coef = 10
p = np.poly1d(np.random.randint(-max_coef, max_coef, size=N+1))
q = np.poly1d(np.random.randint(-max_coef, max_coef, size=N+1))
print("p = ", p)
print("q = ", q)
r = np.polymul(p, q)
print("r = ", r)

p_coef = np.pad(p.coef, (0, N), mode='constant')
q_coef = np.pad(q.coef, (0, N), mode='constant')
p_fft = np.fft.fft(p_coef)
q_fft = np.fft.fft(q_coef)
r_fft = p_fft * q_fft
r_coef = np.fft.ifft(r_fft)
r = np.poly1d(r_coef)
print("r = ", r)