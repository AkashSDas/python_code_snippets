# ###### Shifting and Lagging ######

# =================================
# Importing pandas module
import pandas as pd
# =================================
# Getting the data

df = pd.read_csv('fb.csv', index_col='Date', parse_dates=['Date'])
print(df)
# =================================
# ### shift ###

# Calling shift function on pandas dataframe

# Right Shift
# Shifted by 1 day
print(df.shift(1))

# Shifted by 2 day
print(df.shift(2))

# Left Shift (Using a negative number for Left Shift)
print(df.shift(-1))
# =================================
# Shifting with postive/negative values will shift the data points either by right/left hand side
# We can call shift method on either dataframe or time series
# One common use of this in financial use is to calculate percentage change in 1 day
# =================================
# ### Examples ###

df['Pre Day Price'] = df['Price'].shift(1)
print(df)

df['1 day change'] = df['Price'] - df['Pre Day Price']
print(df)

# Calculate 5 days return
df['5 day % return'] = (df['Price'] - df['Price'].shift(5))*100/df['Price'].shift(5)
print(df)
# =================================
# ### tshift ###

# Instead of shifting data points let's shift dates

df = df[['Price']]
print(df.index)
# Here freq=None
# In order to change date in Pandas we need to know frequency

# It is a Business Day Frequency
df.index = pd.date_range(start='2017-08-15', periods=10, freq='B')
print(df.index)
# Here freq='B'
print(df)

# tshift will shift the dates

print(df.tshift(1))

# Negative value can also be given
print(df.tshift(-1))
