# ###### Mathematical Operations using Numpy ######

# =================================
# Importing numpy module
import numpy as np
# =================================
# ### Basic Mathematical Operations ###

# Creating a an array
a = np.array([1,2,3,4])

# These effects will be on every element in the array
print(a + 2)
print(a - 3)
print(a * 10)
print(a / 3)
print(a ** 2)

a += 2
print(a)

# Performing mathematical operations between arrays
b = np.array([1,0,1,0])
print(a + b)
# =================================
# ### sin method ###

a = np.sin(a)
print(a)
# =================================
# ### cos method ###

a = np.cos(a)
print(a)
# =================================
# So we can use mathematical functions like:
# - Trignometric Functions
# - Hyperbolic Functions
# - Rounding
# - Sums, Products, Differences
# - Exponents and Logarithms
# - Other special functions
#   > i0(x) --> Modified Bessel function of the first kind, order 0
#   > sinc(x) -->	Return the sinc function
# - Floating point routines
# - Rational routine
# - Arithmetic Operations
# - Handling complex numbers
