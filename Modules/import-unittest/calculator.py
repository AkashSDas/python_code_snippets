# ###### Calculator code for testing ######

# =================================
# ##### Objectives #####
# - How to write tests
# - How to setup and teardown our test
# - Some practices
# =================================
# Testing will save alot of time, when we write good tests for codes it gives more confidence that our updates and refactoring don't have any unintended consequences or break our code in anyway 
# Example: If we update a function in our project, those update may have actually broken several sections for our code even if that function is itself working 
# A good unit tests will make sure that everything is still working as it should and if it is not then it will show we exactly what is broken
# =================================
# Code for testing 

def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y
    
def divide(x, y):
  if y == 0:
    # Raising an Error 
      raise ValueError("Can not divide by zero!")
  return x / y
# =================================    
# Normally people tend to use print statement to check that their code is working
print(add(2, 3))

# But isn't a good, because testing this isn't easy to automate and if we are testing a lot of functions their is no way we can keep track what is failing and succeding
# =================================
# To add test we have to create test modules
# The name of the test module should start with 'test_' it is a naming convention
