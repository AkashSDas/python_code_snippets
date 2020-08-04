# ###### Basics Of Numpy ######

# =================================
# Importing numpy module
import numpy as np
# =================================
# ### Initializing an Array ###

a = np.array([1,2,3])
print(a)

# 2D array
b = np.array([[1,2,3], [4,5,6]])
print(b)
# =================================
# ### Indexing a NumPy Array ###

a = np.array([1,2,3,4,5,6,7,8,9])

idx = a[1]
print(idx)

# To get index of multiple values
i = a[[2,5,8]]
print(i)
# =================================
# ### Get Dimension of our array ###

print(a.ndim)
print(b.ndim)
# =================================
# ### Get Shape  ###

# shape attribute gives number of rows and columns
print(a.shape)
print(b.shape)
# =================================
# ### Get Type ###

# To know how much memory our compiler has taken we use the dtype(data type) attribute
print(a.dtype)
print(b.dtype)
# =================================
# ### To spcify what type we want to store in an array ###

c = np.array([1,2,3], dtype='int16')
print(c.dtype)
# =================================
# ### Get Size in of our array in bytes ###

print(a.itemsize)
print(b.itemsize)
print(c.itemsize)
# =================================
# ### To get total number of elements in the array ###

print(a.size)
print(b.size)
print(c.size)
# =================================
# ### Get total size ###

print(a.size * a.itemsize)

# Which is same as ==> nbytes(number of bytes)
print(a.nbytes)
# =================================
# ### For floats ###

f = np.array([0.1, 9.8, 3.14])

print(f)
print(f.dtype)
print(f.itemsize)
print(f.size)
print(f.nbytes)
# =================================
# ### For being more efficient ###

f = np.array([0.1, 9.8, 3.14], dtype='int8')
# To fit the data in tiny space as possible
