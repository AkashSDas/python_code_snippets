# ###### File Objects - Reading and Writing to Files ######

# =================================
# ### Bad Way ###

# ---------------------------------
# To open file use the open method

f = open('test.txt', 'r')

# If we don't specify what we want to do(read['r'],write['w'],append['a']) it will by default open file for reading

# If there is no file with filename give then it will create a new file with that filename
# ---------------------------------
# To know the filename use the name attribute
print(f.name)
# ---------------------------------
# To know to mode with which file is opened use the mode attribute
print(f.mode)
# ---------------------------------
# We have to explicitly close the file when we are done using it since it was opened

# To close the file use the close method
f.close()
# =================================
# This is not a good way
# More prefered way of working with files is using a context manager
# Since in above method when we are opening the file then we have to explicitly close the file too. If we don't close the file then we can end with leaks that cause us to run over the maximum allowed file descriptors on your system and your applications could throw an error so we have to remember to close the file.
# =================================
# ### Using a Context Manager ###

with open('test.txt') as f:
    # To read the content of the file use the read method
    f_contents = f.read()
    print(f_contents)
# ---------------------------------
# If we have extremely large files and we want to read but don't want to load all of the contents of the file into memory
# So there are other methods of reading files other than the read method
# ---------------------------------
# ### .readlines() - This will give us list of elements each elements containg each line with new line character at the end ###

with open('test.txt') as f:
    f_contents = f.readlines()
    print(f_contents)
# ---------------------------------
# ### .readline() - It reads one line character at a time ###

with open('test.txt') as f:
    f_contents = f.readline()
    print(f_contents, end="")
    # end="" --> To avoid new lines
# ---------------------------------    
with open('test.txt') as f:
   for line in f:
     print(line, end="")
# It will print each line in the file object        
# ---------------------------------
# To have more control of what you want to read

with open('test.txt') as f:
   f_contents = f.read(100)
   # 100 lines
   print(f_contents, end="")
   # It will pickup from there where the above one left
   f_contents = f.read(100)
   print(f_contents, end="")
   # Once we reach to the end of file then the read method will just return empty string
# ---------------------------------
# If the file specified is a huge file and we don't know how many lines are there in it then we would prefer reading chunks of it

size_to_read = 10

with open('test.txt') as f:
   f_contents = f.read(size_to_read)
   while len(f_contents) > 0:
     print(f_contents, end="|")
     f_contents = f.read(size_to_read)
     # The above line is to advance the loop otherwise we will be in an infinite loop
     # So when the file ends it will return an empty string and the condition will not be meet we will come out of the loop
# ---------------------------------
# ### .tell() - It returns a value of much we have read or On which position we are in the file ###

with open('test.txt') as f:
    print(f.tell())
# ---------------------------------
# ### .seek() - We can manipulate our position using seek method ### 

with open('test.txt') as f:
    f.seek(0)
# ========================================
# Once we open the file and when we leave the block the file will be closed on its own also if there is some error then the file will be automatically closed
# ========================================
# ### Writing To A File ###

# ---------------------------------
# If the file test.txt does not exist then 'w' mode will create a file with that name, if it exists then it will overwrite its content, so be careful and use 'a' mode i.e. append mode
# ---------------------------------
# ### .write() - Use the write method to write to a file ###

with open('test.txt', 'w') as f:
    f.write('Test')
    # It will pick where the first one left
    f.write('Test')
# ---------------------------------
with open('test.txt', 'w') as f:
    # We can also use seek
    f.write('Test')
    f.seek(0)
    f.write('Test')
    # Second Test will overwrite the first one
# ---------------------------------
with open('test.txt', 'w') as f:
    # But seek method doesn't overwrite everything
    f.write('Test')
    f.seek(0)
    f.write('R')
    # Here the R overwrote only T
# ========================================
# Combining Both Read and Write

# This is basically copying context of one file to the other file
with open('test.txt', 'r') as rf:
  with open('text_copy.txt', 'w') as wf:
    for line in rf:
      wf.write(line)
# ========================================
# To work with images we have to use binary(b)

# Copying image
with open('image.jpg', 'rb') as rf:
  with open('image_copy.jpg', 'wb') as wf:
    for line in rf:
      wf.write(line)
# ========================================
# Since some time you want more control over exactly what you are reading and writing

with open('image.jpg', 'rb') as rf:
  with open('image_copy.jpg', 'wb') as wf:
    chunk_size = 4096
    rf_chunk = rf.read(chunk_size)
    while len(rf_chunk) > 0:
      wf.write(rf_chunk)
      # To keep this from being an infinte loop we have to add the below line
      rf_chunk = rf.read(chunk_size)
