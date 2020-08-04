# ### Objectives ###
# 1. lambda
# 2. map
# 3. filter
# 4. reduce

# =================================
# ### lambda ###

# lambda do not use def and return statments, these are implicit
# ---------------------------------
z = lambda x: x*2
print(z(2))
# ---------------------------------
z = lambda x,y: x+y
print(z(2,3))
# ---------------------------------
z = lambda x,y,w: x+y+w
print(z(2,3,4))
# ---------------------------------
z = lambda x,y: x if x>y else y
print(z(1,2))
print(z(4,2))
# =================================
# ### map ###

# map applies same function to each item in a sequence and returns a map object. 
# map function takes a function and a sequence as an argument

n = [1,2,3,4]

z = map(lambda x: x**2,n)
print(z)

# Casting map object to a list
print(list(z))
# =================================
# ### filter ###

# filter filter's items out of the sequence and return's a filter object
# filter function takes a function and a sequence as an argument

n = (4,3,2,1)

z = filter(lambda x: x>2,n)
print(z)

# Casting filter object to a tuple
print(tuple(z))
# =================================
# ### reduce ###

# To use reduce function we have to import it from functools libary
from functools import reduce

# reduce applies same operation to items of a sequence and uses result of operation as first parameter for next operation and then returns a item not a sequence

n = [4,3,2,1]
        
print(reduce(lambda x,y: x*y,n))

# reduce will do the same work as multiply function will do
def multiply(sequence):  
        product = sequence[0]
        for i in range(1, len(sequence)):
                product *= sequence[i]
    return product

result = multiply([4,3,2,1])
print(result)
