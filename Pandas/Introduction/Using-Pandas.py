# ###### Using Pandas ######

# =================================
# To find answers related to nyc_weather.csv file:
#   (1) Max temperature in New York in month of January
#   (2) List of days when it rained
#   (3) Average speed of wind in month of january
# =================================
# Importing pandas module
import pandas as pd
# =================================
# Using the read_csv method to read 
df = pd.read_csv('nyc_weather.csv')
print(df)

# To get max temperature
print(df['Temperature'].max())

# To get on which dates it rain
print(df['EST'][df['Events']=='Rain'])

# To get Average Wind Speed
print(df['WindSpeedMPH'].mean())
# You will see the answer is 6.892857142857143 which is not right, it happened since our data is not clean i.e. wind speed data was nan that is there is no data in some places 
# =================================
# ### Data Munging ###

# Data Munging - The process of cleaning messy data is called Data Munging or data wrangling

df.fillna(0, inplace=True)
# Whenever it see's NaN it fills it with 0

print(df['WindSpeedMPH'].mean())
