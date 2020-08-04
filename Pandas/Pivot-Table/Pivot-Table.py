# ###### Pivot Table ######

# Pivot allows us to tranform/reshape data i.e. to change format of our table apperance
# =================================
# Importing pandas module
import pandas as pd
# =================================
# Getting the data

df = pd.read_csv('weather.csv')
print(df)
# =================================
# ### pivot ###

# ---------------------------------
# To have x-axis as date

print(df.pivot(index='date', columns='city'))

# index - What we want in our x-axis
# columns - What we want to be as our column
# ---------------------------------
# To have only certain values display on our pivot table we use the values parameter

print(df.pivot(index='date', columns='city', values='humidity'))

# To show multiple values use a list
print(df.pivot(index='city', columns='date', values=['humidity', 'temperature']))
# =================================
# ### pivot_table ###

# Pivot table is used to summarize and aggregate data inside dataframe
# Create a spreadsheet-style pivot table as a DataFrame. The levels in the pivot table will be stored in MultiIndex objects (hierarchical indexes) on the index and columns of the result DataFrame.
# ---------------------------------
# Getting the data

df = pd.read_csv('weather2.csv')
print(df)

# Here you can see that on same dates there are two different values for the same thing
# ---------------------------------
# To create a df where we want mean temperature for same dates we use the pivot_table method

print(df.pivot_table(index='city', columns='date'))
# ---------------------------------
# We can also provide our own aggregate function using the aggfunc parameter

print(df.pivot_table(index='city', columns='date', aggfunc='mean'))

# mean is default value of aggfunc parameter
# ---------------------------------
# Using other values of aggfunc parameter

print(df.pivot_table(index='city', columns='date', aggfunc='sum'))
print(df.pivot_table(index='city', columns='date', aggfunc='count'))
# ---------------------------------
# Setting the margins parameter to True will provide margin which will have statistics

print(df.pivot_table(index='city', columns='date', margins=True))

# Default value of margins is False
# =================================
# ### Grouper ###

# ---------------------------------
# Getting the data 

df = pd.read_csv('weather3.csv')
print(df)

# Converting date column from string to datetime
df['date'] = pd.to_datetime(df['date'])
print(df)
# ---------------------------------
# To aggregate on Date Frequency 
# Let's say to have mean temperature in month of may and december
# To aggreate as per month

print(df.pivot_table(index=pd.Grouper(freq='M', key='date'), columns='city'))
# Here we get average of humidity and temperature for the month

# There are other arguments for Grouper
# Also there are other values for freq argument
