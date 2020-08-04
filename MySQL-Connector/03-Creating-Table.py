# ###### Creating Table ######

# =================================
# Importing mysql.connector
import mysql.connector
# =================================
# Creating our connect object
mydb = mysql.connector.connect(host="localhost", user="root", passwd="password", database="testing")

# Creating cursor
my_cursor = mydb.cursor()
# =================================
# ### Creating a table ###

my_cursor.execute("CREATE TABLE employee(name varchar(200), salary int(20))")
# =================================
# ### Seeing tables ###

my_cursor.execute("SHOW TABLES")

for table in my_cursor:
    print(table)
# =================================
# Closing the database connection
mydb.close()
