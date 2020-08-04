# ######  Difference between  str() and repr()  ######

# =================================
a = [1,2,3,4]
b = 'simple string'

print(str(a))
print(repr(a))

print(str(b))
print(repr(b))

# Not much difference between them yet 
# =================================
# The goal of __repr__ is to be unambiguous(a python command)
# The goal of __str__ is to be readable

# Real Difference
try:
    import datetime
    import pytz
    
    a = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
    
    b = str(a)
    
    print('str(a): {}'.format(str(a)))
    print('str(b): {}'.format(str(b)))
    
    print()
    
    print('repr(a): {}'.format(repr(a)))
    print('repr(b): {}'.format(repr(b)))
    
    print()
except ModuleNotFoundError:
    print("Module 'pytz' is not installed here")
# =================================    
# __repr__ is for developers to find mistakes while debugging while __str__ is userfriendly
# =================================
# str returns a more a readable 
str(x)

# repr returns a more of a python command
repr(x)
