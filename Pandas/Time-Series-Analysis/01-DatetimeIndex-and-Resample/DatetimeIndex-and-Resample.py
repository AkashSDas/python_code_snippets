# ###### DatetimeIndex and Resample ######

# TimeSeries - TimeSeries is a set of data points indexed in time order
# =================================
# ##### Objectives #####
#   1. DatatimeIndex
#   2. Resampling
# =================================
# Importing modules
import matplotlib.pyplot as plt
import pandas as pd
# =================================
# Getting the data

df = pd.read_csv('apple_stocks.csv', parse_dates=['Date'], index_col='Date')
print(df.head(5))
# =================================
# Printing the index of our dataframe
print(df.index)
# =================================
# ### Working with Datetime Index ###

# To retrive Jan 2017 stocks price
print(df["2017-01"])

# To find average price of Apple's stock in Jan 2017
print(df["2017-01"].Close.mean())

# To get prices on particular date
print(df["2017-01-25"])

# To get prices between range of dates
print(df["2017-01-07":"2017-01-01"])
# =================================
# ### Resampling ###

# The resample() method is used to resample time-series data
# ---------------------------------
# To get average of monthly stock prices of Apple from our dataset
print(df.Close.resample('M').mean())
# Here we have a montly frequency - 'M'

# Here we first selected a specific column from our dataframe which will give a timeseries and then calling resampling on a monthly frequency and then the use the result of resampling to take average price
# ---------------------------------
# For plotting graph

plt.style.use('seaborn')
fig = plt.figure(figsize=(10, 8))

df.Close.resample('M').mean().plot()

plt.tight_layout()
plt.savefig('graph1.png')
# ---------------------------------
# For weekly frquency

print(df.Close.resample('W').mean())
plt.style.use('ggplot')
fig = plt.figure(figsize=(10, 8))

df.Close.resample('W').mean().plot()

plt.tight_layout()
plt.savefig('graph2.png')
# ---------------------------------
# For quaterly frquency

print(df.Close.resample('Q').mean())
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(10, 8))

df.Close.resample('Q').mean().plot()

plt.tight_layout()
plt.savefig('graph3.png')
# ---------------------------------
# For overall data plotting

plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(10, 8))

df.Close.plot()

plt.tight_layout()
plt.savefig('graph4.png')
