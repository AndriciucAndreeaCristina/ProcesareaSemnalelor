import matplotlib.pyplot as plt
import numpy as np

# general formula

mean = 0.7
std = 0.1
x = np.linspace(mean - std - 0.5, mean + std + 0.5, 100)
y = np.exp(-0.5 * ((x - mean) / std) ** 2) / (std * np.sqrt(2 * np.pi))
plt.plot(x, y)
plt.show()

# general normal distribution
normal = np.random.standard_normal(100)
x = np.linspace(0, 1, 100)
z = np.exp( (-1) * normal ** 2 / 2) / np.sqrt(2 * np.pi)
X = std * z + mean
plt.plot(X)
plt.show()

# multivariate normal distribution
n = np.random.normal(0, 1, 2)
epsilon = [[1, 3/5], [1, 3/5]]
mean = [0, 0]
eigenvalues, eigenvectors = np.linalg.eig(epsilon)
v = eigenvectors
diag = np.diag(eigenvalues)
v_inv = np.linalg.inv(eigenvectors)
# decomp = np.dot(np.dot(eigenvectors, diag), v_inv)
# print(decomp)
x = v * np.sqrt(diag) * n + mean
print(x)
# z = np.random.normal(0, 1, 1000).transpose()
# x = np.dot(x, z) + mean
# print(x)




