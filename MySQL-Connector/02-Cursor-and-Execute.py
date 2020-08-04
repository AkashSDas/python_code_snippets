# ###### Cursor and Execute ######

# =================================
# Importing mysql.connector
import mysql.connector
# =================================
# Creating our connect object
mydb = mysql.connector.connect(host="localhost", user="root", passwd="password")
# =================================
# ### cursor ###

# Creating a cursor
my_cursor = mydb.cursor()
# =================================
# ### Creating a database ###

my_cursor.execute("CREATE DATABASE testing")
# =================================
# ### Seeing all databases ###

my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
    print(db)
# =================================
# Closing the database connection
mydb.close()
