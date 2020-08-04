# ###### Initializing Different Types of Arrays ######

# =================================
# Importing numpy module
import numpy as np
# =================================
# ### All 0's matrix ###

# It takes shape as argument

a = np.zeros(5)
# 1D matrix with 5 columns
print(a)

a = np.zeros((2,3))
print(a)

a = np.zeros((2,3,4,3))
print(a)
# =================================
# ### All 1's matrix ###

a = np.ones((4,2,2))
print(a)

# We can also specify data types
a = np.ones((4,2,2), dtype='int32')
print(a)
# =================================
# ### Any other number ###

a = np.full((2,2), 99)
print(a)
# =================================
# ### Any other number (full_like) ###

# Here the shape is given of any other array

b = np.full_like(a, 11)
# Here the shape is taken of array a
print(b)

# We can also do this with full method
b = np.full(a.shape, 11)
print(b)
# =================================
# ### To initialize an array of random numbers ###

# To get random number between 0(inclusive) and 1(exclusive)
a = np.random.rand(4, 2)
print(a)

# To pass in shape 
a = np.random.random_sample(a.shape)
print(a)

# To get integer values
a = np.random.randint(7)
print(7)
# If we don't specify starting value it will start at 0 and if we didn't specify shape it will give one number

# Use size for giving shape
a = np.random.randint(7, size=(3,3))
print(a)
# =================================
# ### The identity matrix ###

a = np.identity(5)
print(a)
# =================================
# ### repeat ###

a = np.array([1,2,3])
r1 = np.repeat(a, 3, axis=0)
print(r1)

a = np.array([[1,2,3]])
r1 = np.repeat(a, 3, axis=0)
print(r1)

a = np.array([[1,2,3], [4,5,6]])
r1 = np.repeat(a, 3, axis=0)
print(r1)
r1 = np.repeat(a, 3, axis=1)
print(r1)
# =================================
# axis=0 --> repeat along column
# axis=1 --> repeat along row
# =================================
# Example:

a = np.ones((5,5), dtype='int16')
b = np.zeros((3,3), dtype='int16')
b[1,1] = 9
a[1:-1, 1:-1] = b
print(a)
# =================================
# NOTE: Be careful when copying arrays!!!
# Arrays are immutable
# =================================
a = np.array([1,2,3])
b = a
b[0] = 100
print(b)
print(a)
# =================================
# ### To safely copy we have to use copy method ###

a = np.array([1,2,3])
b = a.copy()
b[0] = 100
print(b)
print(a)
