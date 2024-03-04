# Import module
import sqlite3

# Connecting to sqlite
conn = sqlite3.connect('gfg.db')

# Creating a cursor object using
# the cursor() method
cursor = conn.cursor()

# Updating
cursor.execute('''UPDATE emp SET lname = "Jyoti" WHERE fname="Rishabh";''')

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()
