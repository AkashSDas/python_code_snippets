# ###### Statistics using Numpy ######

# =================================
# Importing numpy module
import numpy as np
# =================================
# Creating an array
stats = np.array([[1,2,3], [4,5,6]])
# =================================
# ### To find min and max element in the entire matrix ###

a = np.min(stats)
print(a)

a = np.max(stats)
print(a)
# =================================
# ### To find min and max element of all rows or columns ###

# 1.For rows
a = np.min(stats, axis=1)
print(a)
a = np.max(stats, axis=1)
print(a)

# 2. For column
a = np.min(stats, axis=0)
# It will give the first full first row since those are min's
print(a)
a = np.max(stats, axis=0)
# It will give the second full first row since those are max's
print(a)
# =================================
# ### To find sum elements of all rows or columns ###

# Sum of column elements
a = np.sum(stats, axis=0)
print(a)

# Sum of row elements
a = np.sum(stats, axis=1)
print(a)
