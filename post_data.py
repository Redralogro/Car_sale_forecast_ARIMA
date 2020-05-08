import warnings

warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
import itertools
import numpy as np
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_model import ARIMA

# plt.style.use('fivethirtyeight')
plt.rcParams.update({'figure.figsize': (9, 7), 'figure.dpi': 120})
import pandas as pd
# df = pd.read_csv (r'norway_new_car_sales_by_make.csv')

from sklearn.utils import resample

# Import data
df = pd.read_csv(r'data_set\norway_new_car_sales_by_month.csv')
# Original Series
y = df['Quantity']
print(y)
s = y
# s = y[0:12]
r = adfuller(s)
print('Original Series :')
print('ADF Statistic: {}'.format(r[0]))
print('p-value: {}'.format(r[1]))
print('---------------------------------')
# y[0:12].plot(figsize=(15, 6))
fig, axes = plt.subplots(2, 3, sharex=True)
axes[0, 0].plot(s)
axes[0, 0].set_title('Original Series')
plot_acf(s, ax=axes[0, 1])
plot_pacf(s, ax=axes[0, 2])


# plt.subplot(2,2,1)
# plt.plot(s)
# plt.title('Original Series')

def differencing(s, interval=1):
    diff = [s[i] - s[i - interval] for i in range(interval, len(s))]
    return diff


# 1st Differencing
ds_1 = differencing(s, 1)
r2 = adfuller(ds_1)
print('1st Differencing :')
print('ADF Statistic: {}'.format(r2[0]))
print('p-value: {}'.format(r2[1]))
print('---------------------------------')
axes[1, 0].plot(s.diff())
axes[1, 0].set_title('1st Order Differencing')
plot_acf(s.diff().dropna(), ax=axes[1, 1])
plot_pacf(s.diff().dropna(), ax=axes[1, 2])
# plt.plot(ds_1)

# ARIMA_MODEL
# 1,1,2 ARIMA Model
temp = [5, 1, 1]
model = ARIMA(s, order=temp)
model_fit = model.fit(disp=0)
print(model_fit.summary())
# Actual vs Fitted
model_fit.plot_predict(dynamic=False)
# diagram
# plt.show()
## Adf Test
from pmdarima.arima.utils import ndiffs

print(ndiffs(y, test='adf'))
