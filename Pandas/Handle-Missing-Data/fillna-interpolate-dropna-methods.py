# ###### Handle Missing Data using fillna, interpolate and dropna methods ######

# =================================
# ### Objectives ###
#   1.fillna: to fill missing values using different ways
#   2.interpolate: to make a guess on missing values using interpolate
#   3.dropna: to drop rows with missing values
# =================================
# Importing pandas module
import pandas as pd
# =================================
# ### Getting our data ###

df = pd.read_csv('weather_data_1.csv')
print(df)

print(type(df.day[0]))
# Here days are of type string since it is a csv file and not excel

# To convert day column into date type
df = pd.read_csv('weather_data_1.csv', parse_dates=['day'])
print(df)
print(type(df.day[0]))

# Make day as index
df.set_index('day', inplace=True)
# inplace=True otherwise it will not modifie the original df rather create a new one
print(df)
# =================================
# ### fillna ###

# fillna method fills NA/NaN values with the values specifed
# ---------------------------------
new_df = df.fillna(0)
print(new_df)

# This will replace NA/NaN values from every place in our dataframe 
# ---------------------------------
# To replace NA/NaN values from certain columns only

# Sometime 0 is not probably the best guess like here in events column we have 0 which makes no sense
# For this we have to dictonary to fill specific value for specific column
new_df = df.fillna({
  'temperature': 0,
  'windspeed': 0,
  'event': 'no event'
})
print(new_df)
# ---------------------------------
# For better estimation we use the method parameter of fillna method

# There are different methods for better esitmation 

# To carray value for previous days
new_df = df.fillna(method='ffill')
# ffill ---> forward fill
print(new_df)

# To carray value for next days
new_df = df.fillna(method='bfill')
# bfill ---> backward fill
print(new_df)

# Till now we were filling data vertically, to fill data horizonatally we use axis parameter and specify the way we want to fill values
new_df = df.fillna(method='bfill', axis='columns')
print(new_df)

# In ffill it copies value to all NaN coming in its path but to carry for specific times we use the limit parameter
new_df = df.fillna(method='ffill', limit=1)
print(new_df)
# =================================
# ### interpolate ###

# It is basically used to fill NA values in the dataframe or series. But, this is a very powerful methof to fill the missing values. It uses various interpolation technique to fill the missing values rather than hard-coding the value.
# ---------------------------------
# For better guess than fillna we are using the interpolate method

new_df = df.interpolate()
print(new_df)

# The precision also increase like (32.0 ---> 32.000000)
# ---------------------------------
# In interpolate method if we don't specify the method by which interpolation should happen then it the method will be linear by default

# Using other methods 
new_df = df.interpolate(method='time')
print(new_df)
# The time method is very powerfull

# In linear method temperature on 04 becomes 30 which is in between 32 and 28 of 01 and 05
# But by time method our guess imporves
# Now temperature on 04 become 29 which is colse to 28 of 05 since date 04 is close to 05 and not to 01
# =================================
# ### dropna ###

# dropna() method is used to remove rows and columns with Null/NaN values. 
# By default, this function returns a new DataFrame and the source DataFrame remains unchanged.
# ---------------------------------
new_df = df.dropna()
# This will drop all rows having atleast 1 NaN
print(new_df)
# ---------------------------------
# 1. how parameter

# To drop an row which have all NaN, we use how parameter
new_df = df.dropna(how='all')
print(new_df)
# ---------------------------------
# 2. thresh parameter

# If we have atleast one not NaN value and we want to keep that row and drop other rows we use thresh(threshold)
new_df = df.dropna(thresh=1)
print(new_df)
# Here it will drop any row having all NaN since threshold is 1

new_df = df.dropna(thresh=2)
print(new_df)
# Here thresh=2 that means there has to be two not NaN to keep the row from dropping
# =================================
# ### To insert missing date ###

dt = pd.date_range("01-01-2017", "01-11-2017")
index = pd.DatetimeIndex(dt)
df = df.reindex(index)
# inplace=True cannot be use here
print(df)
