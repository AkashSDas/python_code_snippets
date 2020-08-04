# ###### Merger DataFrames ######

# Merge DataFrame or named Series objects with a database-style join.
# =================================
# Importing pandas module
import pandas as pd
# =================================
# ### To join two dataframes into one on the basis of city names ###

df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
})
print(df1)

df2 = pd.DataFrame({
    "city": ["chicago","new york","orlando"],
    "humidity": [65,68,75],
})
print(df2)

df3 = pd.merge(df1, df2, on='city')
# Here in "on" parameter we pass in column on which you want to perform merge
print(df3)

# Here it is seeing the city names and matching humdity and temperature into those city, so it not just matching any value but value that belongs to city names are matched to those city names

# It is same as JOINS in DataBase
# =================================
# ### Suppose we have some cities whose values are not given ###

df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando","baltimore"],
    "temperature": [21,14,35,32],
})

df2 = pd.DataFrame({
    "city": ["chicago","new york","sans fransico"],
    "humidity": [65,68,71],
})

df3 = pd.merge(df1, df2, on='city')

print(df3)

# Here whatever was common between those two dataframes were merged
# Here it did INTERSECTION from SET THEORY
# It is same as INNER JOIN in DataBase
# =================================
# ### To choose how we want to do the intersection we use the "how" parameter ###

# ---------------------------------
# OUTER JOIN ---> DataBase
# UNION ---> Set Theory

df3 = pd.merge(df1, df2, on='city', how='outer')
print(df3)
# ---------------------------------
# INNER JOIN is default

df3 = pd.merge(df1, df2, on='city', how='inner')
print(df3)
# ---------------------------------
# LEFT JOIN

df3 = pd.merge(df1, df2, on='city', how='left')
print(df3)
# ---------------------------------
# RIGHT JOIN

# Here left/right is decided by the order in which you have given df's

df3 = pd.merge(df1, df2, on='city', how='right')
print(df3)
# ---------------------------------
# To know that the data came is from right/left we can use indicator flag, it set to False by default

df3 = pd.merge(df1, df2, on='city', how='outer', indicator=True)
print(df3)
# =================================
# ### Suffixes ###

df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando", "baltimore"],
    "temperature": [21,14,35,38],
    "humidity": [65,68,71, 75]
})

df2 = pd.DataFrame({
    "city": ["chicago","new york","san diego"],
    "temperature": [21,14,35],
    "humidity": [65,68,71]
})

# In "on" parameter we give the column name in which we want to perform the merge
df3 = pd.merge(df1, df2, on='city')

print(df3)
# Here both the dataframes have temperature and humdity when we join both we will see that it will automatically appends _x and _y because humidity and temperature columns were repeated between the two dataframes so to distinguish them it automatically appends these suffixes
# ---------------------------------
# To have your own suffixes use the suffixes parameter and passed in a tuple of values which have the names we want

df3 = pd.merge(df1, df2, on='city', suffixes=('_left','_right'))
print(df3)
