# ###### DataFrame Basics ######

# =================================
# ### Objectives ###
#   1. Creating dataframe
#   2. Dealing with rows and columns
#   3. Operations: min, max, std, describe
#   4. Conditional selection
#   5. set_index
# =================================
# Importing pandas module
import pandas as pd
# =================================
# Dataframe is the main object in Pandas. It is used to represent data with rows and columns(tabular or excel spreadsheet like data)
# It is a Data Structure
# =================================
# ### read_csv ###

# Using the read_csv method to read a csv file into DataFrame
df = pd.read_csv('weather_data.csv')
print(df)
# =================================
# ### DataFrame ###

# We can also create a dataframe using python dictonary 
weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature': [32,35,28,24,32,31],
    'windspeed': [6,7,2,7,4,2],
    'event': ['Rain', 'Sunny', 'Snow','Snow','Rain', 'Sunny']
}

# Using the DataFrame method to convert dictonary to a DataFrame
df = pd.DataFrame(weather_data)
print(df)

# Data frame is all about rows and columns
# =================================
# ### Visualizing Data ###

# ---------------------------------
# ### shape ###

# shape means dimensions
print(df.shape)
# It returns a tuple --> (number of rows, number of columns)

# Unpacking the values returned by df.shape
rows, columns = df.shape
print(rows)
print(columns)
# ---------------------------------
# ### head ###

# df prints the entire rows
# To print certain amount of rows from starting of df we will use the head method

print(df.head())
# It provides a convinence when you have large number of rows

# By default it gives only first 5 rows (if no argument is not given)
# If we want certain number of rows from starting then we can specify that as an argument to the head method
print(df.head(2))
# ---------------------------------
# ### tail ###

# To print certain amount of rows from end of df we will use the tail method
print(df.tail())

# By default it gives only last 5 rows (if no argument is not given)
# If we want certain number of rows from ending then we can specify that as an argument to the tail method
print(df.tail(2))
# ---------------------------------
# ### df slicing ###

# Like list slicing we can also slice our df

print(df[2:5])
# It will include rows from 2 to 5, including 2 and excluding 5 

# To print everything we can us df or df[:]
print(df)
print(df[:])
# ---------------------------------
# ### columns ###

# To print columns in our dataframe
print(df.columns)
# ---------------------------------
# ### To print individual column with their contents ###

# There are two ways 

# First way using the dot(.) notation
print(df.day)
print(df.event)

# Secondy way is like we access elements in dictonary
print(df['event']) # It is same as --> df.event
# This way is much preferable since if we have spaces in our column name then dot notation won't work and also if there are attributes with the same name as our column name then we might get an error or overwrite the attribute meaning

# Type of columns in our data frame are of type series
print(type(df['event']))
# ---------------------------------
# ### To print only certain columns ###

print(df[['event', 'day', 'temperature']])
# This will give us a dataframe and not series
# =================================
# ### Performing Operations ### 

print(df['temperature'].max())
print(df['temperature'].min())
print(df['temperature'].mean())
print(df['temperature'].std()) # std ==> standard deviation

print(df.describe())
# describe method wil give a dataframe that will have all statistics result for all those columns
# Note: This will not exculde results for columns that contain categorical data
# =================================
# ### Conditional Selection ### 

print(df[df.temperature >= 32])

print(df[df.temperature == df['temperature'].max()])
# The above syntax is very useful when the column name has spaces between them

# To just print the day of max temperature
print(df['day'][df.temperature == df['temperature'].max()])

# To just print the day and temperature of max temperature
print(df[['day', 'temperature']][df.temperature == df['temperature'].max()])
# =================================
# ### set_index ###

# ---------------------------------
# Our df has index that is automatically assigned to it
print(df.index)
# ---------------------------------
# To change the index to something like days
print(df.set_index('day'))
# Not the index is our actual day column
# But this returns a new df it doesn't modifies the original df
# ---------------------------------
# To modify day as index in our original df:
df.set_index('day', inplace=True)
# setting inplace to True will modify the original df
# ---------------------------------
# Now we can use date as an index
print(df.loc['1/3/2017'])
# ---------------------------------
# To reset the index to the original one
df.reset_index(inplace=True)
print(df)
# ---------------------------------
df.set_index('event', inplace=True)
print(df)
# But here the index is not unique
print(df.loc['Snow'])
# This will give all rows with index Snow
# ---------------------------------
# Here, we create dataframe using csv file and dictonary but there are other ways also for creating dataframe
