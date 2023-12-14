import numpy as np
import scipy
import matplotlib.pyplot as plt
import random

# a)
from keras.losses import mean_squared_error
from pandas import concat
from pandas.plotting import autocorrelation_plot

N = 1000
left = 1
right = 15
time = np.linspace(0, 1, N)
a = random.randint(left, right)
b = random.randint(left, right)
c = random.randint(left, right)
trend = a * time * time + b * time + c

fs1 = 2
fs2 = 5
component1 = np.sin(2 * np.pi * fs1 * time)
component2 = 0.5 * np.sin(2 * np.pi * fs2 * time)
season = component1 + component2
variation = np.random.normal(0, 1, N)

signal = trend + season + variation

fig, axs = plt.subplots(4, figsize = (10, 8))
axs[0].plot(time, signal)
axs[0].set_title('Signal')
axs[0].set_xlabel('Time')
axs[0].set_ylabel('x(t)')
axs[0].grid()
axs[1].plot(time, trend)
axs[1].set_title('Trend')
axs[1].set_xlabel('Time')
axs[1].set_ylabel('x(t)')
axs[1].grid()
axs[2].plot(time, season)
axs[2].set_title('Season')
axs[2].set_xlabel('Time')
axs[2].set_ylabel('x(t)')
axs[2].grid()
axs[3].plot(time, variation)
axs[3].set_title('Variation')
axs[3].set_xlabel('Time')
axs[3].set_ylabel('x(t)')
axs[3].grid()
plt.subplots_adjust(wspace=0.6, hspace=0.8)
plt.savefig("L8_1a.pdf", format="pdf", bbox_inches="tight")
plt.savefig("L8_1a.png", format="png", bbox_inches="tight")
plt.show()

# b
# sliding dot product
# correlation = how much two signals overlap when one is shifted progressively
correlation = scipy.signal.correlate(signal, signal, mode='full', method='auto')
correlation = correlation / np.max(correlation)
plt.plot(correlation)
plt.title('Correlation')
plt.xlabel('Time')
plt.ylabel('Correlation')
plt.grid()
plt.savefig("L8_1b.pdf", format="pdf", bbox_inches="tight")
plt.savefig("L8_1b.png", format="png", bbox_inches="tight")
plt.show()

# c
p = 2
data = signal
mean = np.mean(data)
std_dev = np.std(data)
data_standardized = (data - mean) / std_dev

X = np.zeros((len(data) - p, p))
Y = data_standardized[p:]

for i in range(len(data) - p):
    X[i] = data_standardized[i:i+p]

coefficients = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(Y)

predictions = []
for i in range(p, len(data)):
    pred = np.dot(data_standardized[i-p:i], coefficients)
    predictions.append(pred * std_dev + mean)

print("Coeficienții AR:", coefficients)
plt.plot(time[p:], predictions)
plt.plot(time[p:], signal[p:])
plt.title('AR')
plt.grid()
plt.savefig("L8_1c.pdf", format="pdf", bbox_inches="tight")
plt.savefig("L8_1c.png", format="png", bbox_inches="tight")
plt.show()

# d
from statsmodels.tsa.ar_model import AutoReg
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import TimeSeriesSplit
import numpy as np
data = signal
train_size = int(len(data) * 0.7)
train_data, test_data = data[:train_size], data[train_size:]
horizon = 1
max_lags = 50

best_mse = np.inf
best_p = None

for p in range(1, max_lags + 1):
    model = AutoReg(train_data, lags=p)
    model_fit = model.fit()
    predictions = model_fit.predict(start=len(train_data), end=len(train_data) + len(test_data) - 1)
    mse = mean_squared_error(test_data, predictions)
    if mse < best_mse:
        best_mse = mse
        best_p = p

final_model = AutoReg(train_data, lags=best_p)
final_model_fit = final_model.fit()
test_predictions = final_model_fit.predict(start=len(train_data), end=len(train_data) + len(test_data) - 1)

test_mse = mean_squared_error(test_data, test_predictions)
print(f"Cel mai bun p: {best_p}")
print(f"Eroarea medie pătratică pe setul de testare: {test_mse}")

plt.plot(np.arange(len(data)), data, label='Date originale')
plt.plot(np.arange(len(train_data), len(data)), test_predictions, label='Predicții', color='red')
plt.legend()
plt.xlabel('Timp')
plt.ylabel('Valoare')
plt.title('Predicții cu modelul AR')
plt.savefig("L8_1d.pdf", format="pdf", bbox_inches="tight")
plt.savefig("L8_1d.png", format="png", bbox_inches="tight")
plt.show()