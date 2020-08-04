# ###### fargs, *args and **kwargs ######

# =================================
# fargs, *args, **kwargs --> these are conventions used for naming
# =================================
# *args - Take variable arguments in function and returns a tuple

def add(*nums):
    print(nums)
    return sum(nums)

result = add(1,2,3,4)
print(result)
# =================================
# **kwargs - Takes variable arguments as a keyword(key) which has a value and it returns a dictonary

def get_record(**data):
    print(data)

get_record(name='James',age=18,nationality='Australia') # **kwargs converted it to a dictonary
get_record(name='Jane',age=21,nationality='Argentina',course='CS') # dictonary will be ordered in anyway
# =================================
# Example

        #    fargs  *args    **kwarg
def get_data(engine,*queries,**properties):
    print(engine,queries,properties)
    
get_data('google', 'python', 'java', 'flask', 'django', limit= 10, verbose=True)

# Output:
# google ('python', 'java', 'flask', 'django') {'limit': 10, 'verbose': True}
