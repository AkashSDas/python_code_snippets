# ###### Introduction to mysql-connector ######

# =================================
# To install the package do --> pip3 install mysql-connector-python
# =================================
# Importing mysql.connector
import mysql.connector
# =================================
# ### connect ###

# Creating our connect object
mydb = mysql.connector.connect(host="localhost", user="root", passwd="password")
print(mydb)

if mydb:
    print("Connection Successfull")
else:
    print("Connection Unsuccessfull")
# =================================
# ### close  ###

# Closing the database connection
mydb.close()

# Note: Always close the database that we are connected to
# Alternative this is using a context-manager which is more prefered for managing resources
