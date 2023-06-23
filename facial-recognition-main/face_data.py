import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('/home/hyoseon928/project01/project01.db')
c = conn.cursor()

# Select all rows from the user_data table
c.execute("SELECT * FROM user_data")
rows = c.fetchall()

# Print the retrieved data
for row in rows:
    print("Name:", row[0])
    print("Time:", row[1])
    print("")

# Close the database connection
conn.close()
