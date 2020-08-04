# ###### import array ######

# =================================
# ### Primitive Array ###
# =================================
# ### Methods of creating an array ###

# ---------------------------------
# 1. First way of creating an array

import array
  
a = array.array("i", [1,2,3,4,5,6])
print(a)

# 'i' = typecode, telling what type of datatype my array will hold 
# ---------------------------------
# 2. Second way of creating an array

import array as arr

a = arr.array("i", [1,2,3,4,5,6])
print(a)
# ---------------------------------
# 3. Third way of creating an array

from array import *

a = array("i", [1,2,3,4,5,6]) # here array is our constructor
print(a)
# =================================
# ### Accessing elements of array ###

import array as arr

a = arr.array('i', [1, 2, 3, 4, 5])

print(a[1])
print(a[-1])
# =================================   
# Note: Array are Mutable
# =================================      
# ### Length of Array ###

a = arr.array('i', [1, 2, 3, 4, 5])
length = len(a)
print(length)
# =================================   
# ### We can add elements in Array by append(), extend() and insert() methods ###

a.append(6)    
a.extend([11, 22, 33])
a.insert(0, 7)
print(a)
# =================================   
# ### We can remove elements of Array by remove() and pop() methods ###

x = a.remove(7) # remove() method doesn't return any value
print(a)
print(x)

x = a.pop()
print(a)
print(x)

x = a.pop(5)
print(a)
print(x)
# =================================   
# ### Array Concatenation ###

# Note: Both array should be of same datatype

b = arr.array('i', [1,2,3,4])
c = arr.array('i', [5,6,7,8])
d = arr.array('i')
d = b + c
print(d)
# =================================   
# ### Slicing an Array ###

a = arr.array('i', [1, 2, 3, 4, 5, 6, 7])
print(a[0:5])

a = arr.array('i', [1, 2, 3, 4, 5])
for index, element in enumerate(a[0:-2]):
    print("{} {}".format(index, element))
print(a[::-1]) # [::-1] it does't reverse my array it prints an reverse copy of my array, this method is not prrefered since it exhauste the memory
# =================================   
# ### Looping through an Array ###

a = arr.array('i', [1, 2, 3, 4, 5, 6, 7])

for i in a:
    print(i)
    
print()    
    
counter = 0    
while counter < len(a):
    print(a[counter])
    counter += 1
