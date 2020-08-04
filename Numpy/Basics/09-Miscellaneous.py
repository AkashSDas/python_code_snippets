# ###### Miscellaneous ######

# =================================
# Importing numpy module
import numpy as np
# =================================
# ### Load Data From File ###

# ---------------------------------
filedata = np.genfromtxt('data.txt', delimiter=',')
print(filedata)

# Numbers will aoutomatically be casted to float type
# ---------------------------------
# To get data in specific type 

filedata = np.genfromtxt('data.txt', delimiter=',')
filedata = filedata.astype('int32')
print(filedata)

# Doing just this --> filedata.astype('int32') won't make it to int type, it will make a copy of int type but our filedata will be of type float only, therefore we to do it like this --> filedata = filedata.astype('int32')
# =================================
# ### Boolean Masking and Advance Indexing ###

# ---------------------------------
# To know where in filedata values are greater than 50 
print(filedata > 50)
# It returns boolean True for values > 50 and Flase for values < 50

print(filedata <= 50)
# ---------------------------------
# We can index filedata to find where it is greater than 50
print(filedata[filedata > 50])
# We only get values
# ---------------------------------
# ### any ###

# To get any value greater than 50 in columns
print(np.any(filedata > 50, axis=0))
# ---------------------------------
# ### all ###

# To get all value greater than 50 in columns
print(np.all(filedata > 50, axis=0))

# To get all value greater than 50 in rows
print(np.all(filedata > 50, axis=1))
# ---------------------------------
# To get values greater than 50 and less than 100

result = ((filedata > 50) & (filedata < 100))
print(result)
# ---------------------------------
# For negation and also we can do this like this --> () using one more pair of parenthese

result = ((~(filedata > 50) & (filedata < 100)))
print(result)
