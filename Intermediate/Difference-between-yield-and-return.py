# ###### Difference between yield and return ######

# =================================
# ### Using the yield keyword ###

def countdown():
    i=5
    while i > 0:
        yield i
        i -= 1
        
print(list(countdown ()))

# Output is [5,4,3,2,1]
# =================================
# ### Using the return keyword ###

def countdown():
    i=5
    while i > 0:
        return i
        i -= 1
        
print(countdown ())

# Output is 5
# =================================
### General difference between return and yield is that return terminates the execution while yield doesn't ###
