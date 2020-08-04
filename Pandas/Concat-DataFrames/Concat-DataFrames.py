# ###### Concat DataFrames ######

# Concatination is an operation that we do when we want to join two or more datafrmes
# =================================
# Importing pandas module
import pandas as pd
# =================================
# Creating a dataframe to work with

india_data = {
    "city": ["mumbai","delhi","banglore"],
    "temperature": [32,45,30],
    "humidity": [80, 60, 78]
}
india_weather = pd.DataFrame(india_data)
print(india_weather)

us_data = {
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
    "humidity": [68, 65, 75]
}
us_weather = pd.DataFrame()
print(us_weather)
# =================================
# ### concat ###

# To join these india_weather and us_weather dataframes into a single dataframe
# We pass a list of dataframes that we want to concatinate into one to the concat method 
df = pd.concat([india_weather, us_weather])
print(df)

# Here it is using index from original dataframes
# ---------------------------------
# To ignore the index set the ignore_index parameter to True

df = pd.concat([india_weather, us_weather], ignore_index=True)
print(df)
# ---------------------------------
# To retrive data for each city we use key parameter where each key is associate to each dataframe that we have passed to concatinate

df = pd.concat([india_weather, us_weather], keys=['india', 'us'])
print(df)
# Here if you have ignore_index=True it doesn't works
# ---------------------------------
# To retrive data of a country

print(df.loc['india'])
# This can be used to get original dataframe

# =================================
# ### To append dataframes in column wise ###

# Untill now we have appended 2 dataframes on top of each other

# Creating the dataframes
temperature_df = pd.DataFrame({
    "city": ["mumbai","delhi","banglore"],
    "temperature": [32,45,30],
})
print(temperature_df)

windspeed_df = pd.DataFrame({
    "city": ["mumbai","delhi","banglore"],
    "windspeed": [23,54,18],
})
print(windspeed_df)
# ---------------------------------
# Now to append this 2 df as columns

new_df = pd.concat([temperature_df, windspeed_df], axis=1)
# When axis=0 it will append 2nd df as row but when it is 1 it as column
print(new_df)
# =================================
# ### index parameter ###

# If the order of cities is different and we have some missing data like we have here the to solve this we have to put index with the list of value by which it is way going to align rows from different df

temperature_data = {
    "city": ["mumbai", "delhi", "banglore"],
    "temperature": [32,45,30],
}
temperature_df = pd.DataFrame(temperature_data, index=[0,1,2])

wind_speed_data = {
    "city": ["delhi","mumbai"],
    "windspeed": [7,12],
}
windspeed_df = pd.DataFrame(wind_speed_data, index=[1,0])

df = pd.concat([temperature_df, windspeed_df], axis=1)

print(df)
# =================================
# ### We can also join a DataFrame with a Series ###

print(temperature_df)

# Creating a Series
s = pd.Series(["Humid","Dry","Rain"], name="event")
print(s)

# Concatinating series and dataframe
df = pd.concat([temperature_df, s], axis=1)
print(df)
