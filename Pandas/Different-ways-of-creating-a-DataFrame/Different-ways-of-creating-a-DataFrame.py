# ###### Different ways of creating a DataFrame ######

# =================================
# ### Objectives ###
# Different ways of creating dataframe:
#   1. Using CSV File
#   2. Using Excel
#   3. From Python Dictonary
#   4. From List of Tuples
#   5. From List of Dictonaries
# =================================
# Importing pandas module
import pandas as pd
# =================================
# ### Using CSV ###

# Using the read_csv method to read a csv file into DataFrame
df = pd.read_csv('weather_data.csv')
print(df)
# =================================
# ### Using Excel ###

# Using the read_excel method to read a excel file into DataFrame
df = pd.read_excel('weather_data.xlsx', 'Sheet1')
# The second argument here('Sheet1') is the excel sheet name
print(df)
# =================================
# ### From Python Dictonary ###

weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'windspeed': [6,7,2],
    'event': ['Rain', 'Sunny', 'Snow']
}

# Using the DataFrame method to convert dictonary to a DataFrame
df = pd.DataFrame(weather_data)
print(df)
# =================================
# ### From List of Tuples ###

weather_data = [
    ('1/1/2017',32,6,'Rain'),
    ('1/2/2017',35,7,'Sunny'),
    ('1/3/2017',28,2,'Snow')
]

# Using the DataFrame method to convert list of tuples to a DataFrame
df = pd.DataFrame(weather_data, columns=['day', 'temperature', 'windspeed', 'event'])
# Here we need to provide column names which will be header of our columns
print(df)
# =================================
# ### From List of Dictonaries ###

weather_data = [
    {'day': '1/1/2017', 'temperature': 32, 'windspeed': 6, 'event': 'Rain'},
    {'day': '1/2/2017', 'temperature': 35, 'windspeed': 7, 'event': 'Sunny'},
    {'day': '1/3/2017', 'temperature': 28, 'windspeed': 2, 'event': 'Snow'}  
]

# Using the DataFrame method to convert list of dictonaries to a DataFrame
df = pd.DataFrame(weather_data)
print(df)
# =================================
# There are also other ways to create dataframe
