# ###### Error Handling ######

# =================================
# When we get an error there is a tracback which is useful for developers but it of no use to the user 
# try/except block is useful so that when we get an error it is not visible to the users
# =================================
# ### try-except block ###

try:
  f = open('textfile.txt')
  # The file name is incorrect
  # This is FileNotFoundError
except Exception:
  print('Sorry. This file does not exist')
# =================================
# Here the Exception is very general it is catching all the errors other than FileNotFoundError

try:
  f = open('text_file.txt')
  # The file name is correct
  # But bad variable assingment
  var = bad_var
except Exception:
  print('Sorry. This file does not exist')
  
# Now also we get the same message even if the error this time is different 
# The opening of file was successful but not the assingment of variable
# We have to be more specific 
# =================================
# ### Specifying the Exception ###

# Being more specific to catch more general exception

try:
  f = open('text_file.txt')
  var = bad_var
except FileNotFoundError:
  print('Sorry. This file does not exist')
except Exception:
  print("Sorry. Something went wrong")

# When you are handling more exception be sure that the specific execption be on top and more general ones be at the bottom of try/except block
# =================================
# ### Exception as e ###

# To print out the excetion that it threw

try:
  f = open('text_file.txt')
  var = bad_var
except FileNotFoundError as e:
  print(e)
except Exception as e:
  print(e)

# Here instead of variable "e" we can use other name, but it is a naming convention 
# =================================
# ### else clause ###

# else block, it runs code that needs to be executed if the try clause doesn't raise an exception 

try:
  f = open('test_file.txt')
  # Correct file name
except FileNotFoundError as e:
  print(e)
except Exception as e:
  print(e)
else:
  print(f.read())
  f.close()
# ---------------------------------
# We can also specify error like this

try:
  f = open('test_file.txt')
  # Correct file name
  print(f.read())
  f.close()
except FileNotFoundError as e:
  print(e)
except Exception as e:
  print(e)

# But we want to be more specific on what we are trying to catch
# The try block might catch some error but we were not trying to catch
# So it is better to put it in else clause or apart from try block altogether
# =================================
# ### finally clause ###

# The else clause run only when we don't throw an exception but the finally clause runs no matter what happens, whether the code is successful or we throw an exception
# This is useful for making sure that you release certain resources regardless of what happens in try and except

# Example: Suppose your working with database or something like that then this would be an area where you could close down the database at this step 
# ---------------------------------
try:
  f = open('test_file.txt')
  # Correct file name
except FileNotFoundError as e:
  print(e)
except Exception as e:
  print(e)
else:
  print(f.read())
  f.close()
finally:
  print('Executing Finally....')
# ---------------------------------
try:
  f = open('testfile.txt')
  # Wrong file name
except FileNotFoundError as e:
  print(e)
except Exception as e:
  print(e)
else:
  print(f.read())
  f.close()
finally:
  print('Executing Finally....')
# =================================
# ### We can raise exceptions on our own ###

# It doen't need to be something that Python would have caught on its own 
# Use the "raise" keyword to raise an exception

try:
  f = open('currupt_file.txt')
  # Nothing wrong with the file or its name

  # Raising Exception
  if f.name == 'currupt_file.txt':
    raise Exception
except FileNotFoundError as e:
  print(e)
except Exception:
  print('Error!')
else:
  print(f.read())
  f.close()
finally:
  print('Executing Finally....')
