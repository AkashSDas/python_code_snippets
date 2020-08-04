# ###### Difference between '==' and 'is' (Equality and Identity) ######

# =================================
# What is the difference between "==" and "is" ?
#     "==" checks for equality, checks if values are equal
#     "is" checks for identity, which means it's going to check if the values are identical in terms of being the same object in memory 
# =================================
l1 = [1,2,3,4,5]
l2 = [1,2,4,5]

if l1 == l2:
  print(True)
else:
  print(False)

# Output is False since they have different values
# =================================
l1 = [1,2,3,4,5]
l2 = [1,2,3,4,5]

if l1 == l2:
  print(True)
else:
  print(False)

# Output is True 
# But values can be considered equal without actually being the same object in memory 
# =================================
# To check that they are same objects in memory there we use is keyword

l1 = [1,2,3,4,5]
l2 = [1,2,3,4,5]

if l1 is l2:
  print(True)
else:
  print(False)

# Output is False since they are different objects in memory
# =================================
l1 = [1,2,3,4,5]
l2 = l1
# Now the l2 will be same list object in memory as our l1

if l1 is l2:
  print(True)
else:
  print(False)

# Output is True since they are same objects in memory
# =================================
# Since list objects are mutable and these are eqaul to same object in memory it means that we change one then it will also means that it will change the other object also

l1 = [1,2,3,4,5]
l2 = l1

l1[0] = 6
# This changes first value f l1 and l2 since they are same objects in memory, the reason they does this is that list are mutable 

print(l1)
print(l2)
# =================================
l1 = [1,2,3,4,5]
l2 = l1

# Printing out the memory address
print(id(l1))
print(id(l2))

# id(l1) is equal to id(l2)
print(id(l1) == id(l2))
# Output is True

# id(l1) == id(l2) --> This is what the is keyword is doing in the background
