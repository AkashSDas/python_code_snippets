# ###### Handle Missing Data using the replace method ######

# =================================
# Importing modules
import pandas as pd
import numpy as np
# =================================
# Getting the data
df = pd.read_csv('weather_data.csv')
print(df)

# Here we can see -99999 as value in some cells. Those are special values i.e. missing data but special values are placed in its place
# =================================
# When we have one special value and we want to replace that with some other value we use the replace method

# To repalce -99999 with NaN
new_df = df.replace(-99999, np.NaN)
print(new_df)
# =================================
# When we have more than one special value then we pass a list of data that we want to be replaced

new_df = df.replace([-99999, -88888], np.NaN)
print(new_df)

# To replace 0 in event we can use
new_df = df.replace([-99999, -88888, 0], np.NaN)
print(new_df)
# =================================
# But this is not a right the way to replace value, since replace method will go through the entire dataframe and wherever it see's 0 it will replace it with NaN which is an issue since in other columns 0 maybe valid value. 
# To avoid this we pass a dictonary where we specify the column names as key and the values be the values that we want to replace

new_df = df.replace({
  'temperature': -99999,
  'windspeed': -99999,
  'event': '0'
}, np.NaN)
# This dictonary will contain name of columns and value to be replaced
print(new_df)

# Here this dictonary is mapping of what value to be replaced with which value
new_df = df.replace({
  -99999: np.NaN,
  '0': 'Sunny'
})
print(new_df)
# =================================
# ### Using Regular Expression to replace values ###

# If our data had something like 32F and 32C in temperature and 6mph and 7mph in windspeed

# To replace F, C, mph from those data rgex(Regular Expression) is the best way to do that
# To do that we have to set the regex parameter as True

new_df = df.replace('[A-Za-z]', '', regex=True)
print(new_df)
# This erase all columns having A-Z or a-z

# To avoid that and replace value from certain columns we will use dict
new_df = df.replace({
  'temperature': '[A-Za-z]',
  'windspeed': '[A-Za-z]'
}, '', regex=True)
print(new_df)
# =================================
# ### To replace a list of values ###

# Creating different dataframe
df = pd.DataFrame({
    'score': ['exceptional','average', 'good', 'poor', 'average', 'exceptional'],
    'student': ['rob', 'maya', 'parthiv', 'tom', 'julian', 'erica']
})
print(df)

# To replace score with number values
new_df = df.replace(['poor', 'average', 'good', 'exceptional'], [1,2,3,4])
print(new_df)

# This type of replacement is very powerful
