# ###### Reorganizing Arrays ######

# =================================
# Importing numpy module
import numpy as np
# =================================
# ### reshape ##

before = np.array([[1,2,3,4], [5,6,7,8]])
print(before)

# To change the shape of array we use the reshape method
after = before.reshape((8,1))
print(after)

after = before.reshape((2,2,2))
print(after)

# You can pass any value of shape as along it can contain same number of elements in our case it is 8 (8*1, 2*2*2)
# =================================
# ### Vertically Stacking Vectors ###

# ---------------------------------
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

result = np.vstack([v1,v2])
print(result)

# We can also do 
result = np.vstack([v1,v2,v1,v2])
print(result)
# ---------------------------------
# We cannot do something like this where sizes mismatch

try:
  v1 = np.array([1,2,3,4,5])
  v2 = np.array([5,6,7,8])
  result = np.vstack((v1,v2))
  print(result)
except Exception as e:
  print(e)
# ---------------------------------
# We can alse do this with using this --> () without using this --> []

v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

result = np.vstack((v1,v2))
print(result)
result = np.vstack((v1,v2,v1,v2))
print(result)
# =================================
# ### Horizontal Stacking Vectors ###

h1 = np.ones((2,4))
h2 = np.zeros((2,2))

result = np.hstack((h1,h2))
print(result)
