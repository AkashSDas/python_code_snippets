# ###### Stack and Unstack ######

# =================================
# To take one of the column level and transposed it into row level can be done by stacking
# We might also want to take metric from our column level and transpose it into a row level all of this can be achieved using stacking
# =================================
# Importing pandas module
import pandas as pd
# =================================
# Getting the data from excel file

df = pd.read_excel('stocks.xlsx', header=[0,1])
# Remember to supply header argument, those are levels of header, level 1 and level 2
# =================================
# ### Stack ###

print(df.stack())

# To take the first level 
print(df.stack(level=0))

# If we have any na values we have to pass dropna=True
print(df.stack(level=1, dropna=True))
# =================================
# ### Unstack ###

# We can unstack to reverse the transformation
df_stacked = df.stack()
df_stacked.unstack()

# We can do this with n-level of columns

df.stack()
# It will by default stack the inner most level and transpose it
