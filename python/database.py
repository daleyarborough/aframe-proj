import csv, sqlite3 as sq3

# Establish connection to csv file used to create database
conn = sq3.connect('my_db.db')

# Cursor is created in order to call the execute method and run sql commands
cur = conn.cursor()

# Create Table
cur.execute('''DROP TABLE IF EXISTS airbnb''')
cur.execute('''CREATE TABLE airbnb
            (
            name text, 
            price text, 
            city text
            )''')

# In Order to Save, Commit Changes
conn.commit()

print("Table airbnb has been created")