# ###### date_range ######

# =================================
# Importing modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# =================================
# Getting the data

df = pd.read_csv('apple_stocks_no_dates.csv')
print(df)
# =================================
# ### Creating a date range ###

# ---------------------------------
# Since the date are not given we have to generate them and these are not straight forward from 1-22, there are weekends also, so we have to take care of that also

rng = pd.date_range(start='6/1/2017', end='6/30/2017', freq='B')
# Here frequency as 'B'(Business) will exclude weekends
print(rng)
# ---------------------------------
# Changing the index of our dataframe to "rng" column that we have created
df.set_index(rng, inplace=True)
# inplace=True if not given then it will give a new df and not modifie the original df
print(df)
# ---------------------------------
# Plotting the graph

plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(10, 8))

df.Close.plot()

plt.tight_layout()
plt.savefig('graph1.png')
# =================================
# ### Partial Date Selection ###

print(df["2017-06-01":"2017-06-10"])
print(df["2017-06-01":"2017-06-10"].Close.mean())
# =================================
# ### asfreq ###

# To get our df to have prices on weenkends, on weekend the stocks really have not traded so we don't have the prices but we assume that whatever was the price on friday the same was the price on saturday and sunday
# For this we will use the asfreq() method

print(df.asfreq('D', method='pad'))
# Here the D-->Days frequency will generate df and the prices on weekend will be carried forward friday
# pad --> padding - it will just carry forward the values

# For Weekly
print(df.asfreq('W', method='pad'))

# For Hourly
print(df.asfreq('H', method='pad'))
# =================================
# ### periods ###

# ---------------------------------
# Now let's say we don't know about end date but we know how many period we will generate then we can create a date range by passing the periods argument with value being the period

rng = pd.date_range(start='1/1/2019', periods=72, freq='B')
# These are Business Days
print(rng)
# ---------------------------------
# This could be useful when we are generating test data

rng = pd.date_range(start='1/1/2019', periods=72, freq='H')
print(rng)

print(np.random.randint(1,10,len(rng)))
time_series = pd.Series(np.random.randint(1,10,len(rng)), index=rng)
print(time_series.head(10))
