# ###### Linear Algebra using Numpy ######

# =================================
# Importing numpy module
import numpy as np
# =================================
# ### Multiplying two matrices ###

# Note: Number of columns of first matrix should be equal to number of rows of second matrix then only martrices can be multiplyed

a = np.ones((2,3))
b = np.full((3,2), 2)

# Doing a*b this won't work since these are of different sizes

# To multipy arrays we have to use the matmul method
c = np.matmul(a,b)
print(c)
# =================================
# ### Determinant of matrices ###

# To find the determinant of matrices we use the linalg.det method
a = np.identity(3)
b = np.linalg.det(a)
print(b)
# =================================
# We can do operation on matrices like:
#   - Matrix and vector products
#   - Decompositions
#   - Matrix eigenvalues
#   - Norms and other numbers
#   - Solving equations and inverting matrices
#   - Exceptions
#   - Linear algebra on several matrices at once
