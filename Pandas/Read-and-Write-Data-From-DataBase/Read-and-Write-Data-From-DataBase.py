# ###### Read and Write Data From DataBase ######

# =================================
# ### Objectives ###
# Read database records into Pandas dataframe and write it back
#   1. pd.read_sql_table
#   2. pd.read_sql_query
#   3. df.to_sql
#   4. pd.read_sql (which is just wrapper for first two methods)
# =================================
# Importing modules
import pandas as pd
import sqlalchemy
# =================================
# This can be used to interface with any other database just the sample string will change when we use different database, so things are documented on pandas document
# =================================
engine = sqlalchemy.create_engine('mysql+pysql://root:@localhost:3306/application')
# =================================
# ### read_sql_table ###

# To read table
df = pd.read_sql_table('customers', engine)
print(df)

# To read specific columns use the columns parameter and pass in a list which contains column names that we want to see
df = pd.read_sql_table('customers', engine, columns=['name'])
print(df)
# =================================
# ### read_sql_query ###

# Task is to join two tables with sql

# To read the same data into Pandas dataframe
query = """
SELECT customers.name, customers.phone_number, orders.name, oreders.amount
FROM customers INNER JOIN orders
ON customers.id = orders.customer_id
"""

df = pd.read_sql_query(query, engine)
print(df)

# It will execute the query internally, engine and the result will load into df
# =================================
# If we have lot of records to read we can use chunksize, if we use that then we will be able to load a huge amount of data into patches, it has other arguments such as parse_dates, index_col
# =================================
# ### Writing data from dataframe to sql ###

df = pd.read_csv('customers.csv')
print(df)

# To rename column names
df.rename(columns={
  'Customer Name': 'name',
  'Customer Phone': 'phone_number'
}, inplace=True)
print(df)

# ### to_sql ###

df.to_sql(
  name='customers', # name of the sql table
  con=engine, # connection
  index=False,
  if_exists='append'
)

# if_exists has values 'fail', 'replace' and 'append'
# fail - if table exists, do nothing
# replace - if table exists, drop it, recreate it, and insert data
# append - if table exists, insert data. Create if does not exist

# This will write all the records in sql database

# df.read_sql()
# =================================
# ### read_sql ###

# We can do similar things as read_sql_table and req_sql_query

df.read_sql('customers', engine)
df.read_sql(query, engine)

# When we provide first argument as table name it will internally perform read_sql_table
# When we provide first argument as query it will internally perform read_sql_query
