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
import pandas as pd
import pandas.plotting
dataframe = pd.DataFrame(signal)
lag = pandas.plotting.lag_plot(dataframe)
lag.set_title('Lag Plot')
lag.set_xlabel('x(t)')
lag.set_ylabel('x(t + lag)')
lag.grid()
plt.show()

dataframe = concat([dataframe.shift(1), dataframe], axis=1)
dataframe.columns = ['t-1', 't']
result = dataframe.corr()
print(result)

X = dataframe.values
train, test = X[1:int(len(X)*0.9)], X[int(len(X)*0.9):]
# print("Train: ", train)
# print("Test: ", test)
train_X, train_y = train[:,0], train[:,1]
test_X, test_y = test[:,0], test[:,1]

def model_persistence(x):
	return x

pred = []
for x in test_X:
    yhat = model_persistence(x)
    pred.append(x)
test_score = mean_squared_error(test_y, pred)
print('Test MSE: %.3f' % test_score)
plt.plot(test_y)
plt.plot(pred, color='red')
plt.show()