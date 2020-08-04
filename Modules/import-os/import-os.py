# ###### import os ######

# =================================
# Importing os module
import os
# =================================
# ### getcwd() ###

# It is used to get the current directory that we are in
print(os.getcwd()) 

# getcwd --> get current working directory
# =================================
# ### chdir() ###

# It is used to change directory
os.chdir('') 
# inside the '' give the directory to which you want to go

print(os.getcwd())
# Current working directory changes to one given inside the ''
# =================================
# ### listdir() ###

# It is used to list directory
print(os.listdir())

# Gives files and folders in the current working directory
# We can alse pass a path to listdir() but by default it will list the file in current directory
# =================================
# ### Creating directories ###

# There are two methods
# 1. mkdir()
# 2. mkdirs()

# ---------------------------------
os.mkdir('OS-Demo')
os.makedirs('OS-Demo') 
# makedirs will make directory that is few level deep and mkdir won't do that
# ---------------------------------
# This is will give an error because the top level i.e. OS-Demo doesn't exist
os.mkdir('OS-Demo/Sub-Dir-1)
# ---------------------------------
# Using makedirs will create the top level for us 
os.makedirs('OS-Demo/Sub-Dir-1') # using this is prefered even while making top level's
# ---------------------------------
print(os.listdir())
# =================================
# ### Deleting directories ###

# rmdir - remove directory                  
# ---------------------------------         
os.rmdir('OS-Demo/Sub-Dir-1') 
# Using rmdir is preferd so that we can delete the exact file that we want to delete
# ---------------------------------
# This will remove parent directories also         
os.removedirs('OS-Demo/Sub-Dir-1')
# ---------------------------------
print(os.listdir())
# =================================
# ### Renaming directories ###
         
os.rename('original_file_name', 'new_file_name')
# =================================
# ### stat() ###

# To look some information about file we can use stat method
         
# It gives info about 'file_name'
print(os.stat('file_name'))

# st_size attribut gives size of file
print(os.stat('file_name').st_size) 

# st_mtime attribut gives time of last modification
print(os.stat('file name').st_mtime)
# This gives time such that humans cannot read

# To convert it to human readable time format
from datetime import datetime

mod_time = os.stat('file name').st_mtime
print(datetime.fromtimestamp(mod_time))
# =================================
# ### walk() ###
         
# To see entire directory tree and files within desktop
os.walk() 
# This is a generator that yield's a tuple of three values as it is walking through directory tree, for each directory it see's it yield (directory path, directory within that path, files within that path)
# ---------------------------------
# Since it yields three value tuple that's why are able to use this syntax
for dirpath, dirnames, filenames in os.walk('path_of_directory'):
    print("current path: ", dirpath)
    print("directries: ", dirnames)
    print("files: ", filenames)
    print()
# ---------------------------------    
# For current directory
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print("current path: ", dirpath)
    print("directries: ", dirnames)
    print("files: ", filenames)
    print()    
# =================================
# ### environ ###         
         
# It will print out all the enviroment variable
print(os.environ) 

# Access home directory location by grabbing the home enviroment variable
print(os.environ.get('HOME'))
# This gives location of user home directory
# =================================
# ### join() ###         
         
# combine os.environ.get('HOME') and 'test.txt'
         
# One way is to just concatenate them
file_path = os.environ.get('HOME') + 'test.txt'
print(file_path) 
# It is not a good method because it tends to mistakes
# ---------------------------------
# So we will be using join method from os.path module
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)
# =================================
# ### Other useful methods ###

# ---------------------------------         
# basename()
print(os.path.basename('/tmp/test.txt')) 
# It gives file name of anypath we are working on and it doesn't have to be real path
# ---------------------------------
# dirname()
print(os.path.dirname('/tmp/test.txt')) 
# It gives directory name
# ---------------------------------
# split()
# If we want the dirname and basename both
print(os.path.split('/tmp/test.txt'))
# ---------------------------------
# exists
# To check if a path exist
print(os.path.exists('/tmp/test.txt'))
# ---------------------------------
# If file get saves without extension and you to check if something is directory or file

# To check directory it will return (True/False)
print(os.path.isdir('/tmp/test.txt'))  

# To check file it will return (True/False)
print(os.path.isfile('/tmp/test.txt')) 
# ---------------------------------
# splitext
# split the file route and extension
print(os.path.splitext('/tmp/test.txt'))
