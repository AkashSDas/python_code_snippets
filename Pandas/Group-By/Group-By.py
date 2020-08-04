# ###### Group By (Split,Apply,Combine) ######

# =================================
# Importing pandas module
import pandas as pd
# =================================
# To get answers such as:
#   1. Maximum temperature in each of the cities
#   2. Average wind speed in each city

# For this first we have to group data according to city names
# =================================
# Getting our data

df = pd.read_csv('weather_by_cities.csv')
print(df)
# =================================
# To group this data by city names

g = df.groupby('city')
# Pass the column name by which we want to group
print(g)
# =================================
# Now we have 3 different group each corresponding to a unique city name

# To access each group
for city, city_df in g:
  print(city)
  print(city_df)

# To access a df for specific city we use the get_group method
print(g.get_group('mumbai'))
# ---------------------------------
# Find Maximum temperature in each of the cities
print(g.max())

#  Now we are first dividing our data into different groups based on different cities and then we are running analytics on each of these groups and then we combining the result into single dataframe this is called Split Apply Combine

# To get average wind speed in each city
print(g.mean())

# To get all analytics
print(g.describe())
