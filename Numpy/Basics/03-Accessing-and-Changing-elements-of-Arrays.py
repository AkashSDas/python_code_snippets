# ###### Accessing and Changing the elements of Arrays ######

# =================================
# Importing numpy module
import numpy as np
# =================================
# Creating 2D Numpy Array
a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])

print(a.shape)
# 2 by 7 array
# =================================
# Just like list here indexing starts from 0 and accessing element is also like list
# =================================
# ### Get a specific element [row, column] ###

print(a[1, 5])
print(a[1, -1])
print(a[-1, -5])
# =================================
# ### Get a specific row ###

# The indexing below select first row and all columns
print(a[0, :])
# =================================
# ### Get a specific column ###

print(a[:, 1])
print(a[:, -1])
# =================================
# ### Getting a little more fancy [startindex:endindex:stepsize] ###

print(a[0, 1:6:2])
print(a[0, 1:-1:2])
# =================================
# ### To change specify element ###

a[1, 5] = 100
print(a)
# =================================
# ### To change entire column ###

a[:, 2] = 99
print(a)
# =================================
# ### To change entire row ###

a[1, :] = 19
print(a)
# =================================
# ### To change specify element ###

a[1, 5] = 77
print(a)
# =================================
# ### A 3D Example ###

b = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
print(b)

# To get 6 from b
print(b[1, 0, 1])

print(b[:, 1, :])
print(b[1, :, :])

# Changing elements
b[:, 1, :] = [[10, 10], [20, 20]]
# It should be in the range of index
print(b)
