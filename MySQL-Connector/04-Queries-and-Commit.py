# ###### Queries and Commit ######

# =================================
# Importing mysql.connector
import mysql.connector
# =================================
# Creating our connect object
mydb = mysql.connector.connect(host="localhost", user="root", passwd="password", database="testing")

# Creating cursor
my_cursor = mydb.cursor()
# =================================
query = "INSERT INTO employee(name, salary) VALUES(%s, %s)"
values = [("babu rao", 10000), ("raju", 20000), ("shyam", 30000), ]

# Since execute method will single value but since we are using a tuple we have to use executemany method
my_cursor.executemany(query, values)
# =================================
# ### commit ###

# Commiting our changes
mydb.commit()
# =================================
# Closing the database connection
mydb.close()
