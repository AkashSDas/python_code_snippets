# ###### Reshape DataFrame using melt ######

# Similary to pivot method, melt method is also used to transform/reshape data
# =================================
# Importing pandas module
import pandas as pd
# =================================
# Getting the data

df = pd.read_csv('weather.csv')
print(df)
# =================================
# ### melt ###

df1 = pd.melt(df, id_vars=["day"])
print(df1)

# id_vars - Thing which we want in our x-axis, the column we want to keep intact or column we want to transform
# =================================
# ### To filter data ###

# Normal way
print(df1[df1["variable"]=="berlin"])

# Using the melt method
# If we have big data to filter them down we would do it like this

# var_name - Name to use for the ‘variable’ column. If None it uses frame.columns.name or ‘variable’.
df2 = pd.melt(df, id_vars=["day"], var_name='city')
print(df2)

# value_name - Name to use for the ‘value’ column.
df3 = pd.melt(df, id_vars=["day"], var_name='city', value_name='temperature')
print(df3)
