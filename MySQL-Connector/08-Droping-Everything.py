# ###### Droping Everything ######

# =================================
# Importing mysql.connector
import mysql.connector
# =================================
# Creating our connect object
mydb = mysql.connector.connect(host="localhost", user="root", passwd="password", database="testing")

# Creating cursor
my_cursor = mydb.cursor()
# =================================
# Deleting the table

delete_table_query = "DROP TABLE employee"
my_cursor.execute(delete_table_query)
mydb.commit()
# =================================
# Deleting the database

delete_database_query = "DROP DATABASE testing"
my_cursor.execute(delete_database_query)
mydb.commit()
# =================================
# Closing the database connection
mydb.close()
