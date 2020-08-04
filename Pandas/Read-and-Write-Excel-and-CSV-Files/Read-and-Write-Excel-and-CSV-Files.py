# ###### Read and Write Excel and CSV Files ######

# =================================
# ### Objectives ###
#   1. Read CSV
#   2. Write CSV
#   3. Read Excel
#   4. Write Excel
# =================================
# Importing pandas module
import pandas as pd
# =================================
# ### Read CSV ###

# ---------------------------------
# Using the read_csv method to read a csv file into DataFrame

df = pd.read_csv("stock_data.csv")
print(df)
# ---------------------------------
# If there are extra header in our file and we want to skip it

# Note: Add extra header to csv file then apply these codes to see affects

# Use the skiprows parameter in which we have to specify the number of rows we want to skip
df = pd.read_csv("stock_data.csv", skiprows=1)
print(df)

# We can also do the same thing with the header parameter
df = pd.read_csv("stock_data.csv", header=1)
# This will say that my header is located at index=1
print(df)
# ----------------------------------
# If we have no header and we want some header for our columns

# Note: Remove the header from csv file then apply these codes

# Use the header argument to give its value as None(since we don't have header)
df = pd.read_csv("stock_data.csv", header=None)
# This will produce header number from 0 and so on
print(df)

# But the header names produced above are not much helpful to work with our dataframe
# To provide our names for columns header we can use the names parameter and specify the list of elements which has names of headers
df = pd.read_csv("stock_data.csv", header=None, names=['tickers' ,'eps', 'revenue', 'price', 'people'])
print(df)
# ----------------------------------
# To read certain number of rows from a file

# Use the nrows parameter and specify the number of rows of file to read. Useful for reading pieces of large files.
df = pd.read_csv('stock_data.csv', nrows=3)
print(df)
# This limits the number of lines you want to read from csv file
# ----------------------------------
# To clean messy data from file

# Since in our df we have certain cells filled with not available and n.a. values
# To replace with these values use the na_values parameter and give list of values that you want to replace with NaN
df = pd.read_csv('stock_data.csv', na_values=['not available', 'n.a.'])
print(df) 
# This changes the values specified in the list provided to na_values parameter from all places in our dataframe 
# ----------------------------------
# To convert values in certain places only

# We have to pass a dictonary to na_values parameter
df = pd.read_csv('stock_data.csv', na_values={
  'eps': ['not available', 'n.a.'],
  'revenue': ['not available', 'n.a.', -1],
  'people': ['not available', 'n.a.']
})
print(df)
# This can help in data munging
# =================================
# ### Writing Back To CSV File ###

# Use the to_csv method to write our dataframe to csv file
df.to_csv('new1.csv')
# This creates a csv file if file is not created and write with data from df to csv file

# To write csv file without index which is automatically added to our csv file put the index parameter to False
df.to_csv('new2.csv', index=False)

# To write only certain columns use the columns parameter and provide the list of header names that we want
df.to_csv('new3.csv', index=False, columns=['tickers', 'eps'])

# To skip exporting header put header parameter to False
df.to_csv('new4.csv', index=False, columns=['tickers', 'eps'], header=False)
# =================================
# ### Read Excel ###

# To read excel file use the read_excel method
df = pd.read_excel('stock_data.xlsx', 'Sheet1')
print(df)
# ----------------------------------
# Conversion Of Cell Content

# We have to use converters parameter to change certain values in certain columns

# Defining a function by which we will filter our values
def convert_people_cell(cell):
  if cell=='n.a.':
    return 'sam walton'
  return cell

def convert_eps_cell(cell):
  if cell='not avialable':
    return None
  return cell

df = pd.read_excel('stock_data.xlsx', 'Sheet1', converters={
  'people': convert_people_cell,
  'eps': convert_eps_cell
})
# =================================
# ### Writing to excel file ###


# Use the to_excel method to write our dataframe to excel file
pd.to_excel('new1.xlsx', sheet_name='stocks')

# Same as csv file if you don't want to export header and index then put header and index parameter to False for respective effects
pd.to_excel('new1.xlsx', sheet_name='stocks', index=False, header=False)

# To start writing cretain rows and columns
pd.to_excel('new1.xlsx', sheet_name='stocks', startrow=1, startcol=2)
# ----------------------------------
# To write multiple dataframes in one single excel file

# Creating two different dataframes

df_stocks = pd.DataFrame({
    'tickers': ['GOOGL', 'WMT', 'MSFT'],
    'price': [845, 65, 64 ],
    'pe': [30.37, 14.26, 30.97],
    'eps': [27.82, 4.61, 2.12]
})

df_weather =  pd.DataFrame({
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'event': ['Rain', 'Sunny', 'Snow']
})

# Use the ExcelWriter class in Pandas with context manager to write multiple dataframes to one single excel file
with pd.ExcelWriter('stocks_weather.xlsx') as writer:
    df_stocks.to_excel(writer, sheet_name="stocks")
    df_weather.to_excel(writer, sheet_name="weather")
# =================================
# There many properties to read and write like spearater, dilimiter, true_values, false_values, skipinitialspace, skiprows, skipfooter, skip_footer, skip_blank_lines, etc   
