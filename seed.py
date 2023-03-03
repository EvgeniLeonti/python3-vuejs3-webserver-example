import sqlite3

# Open a connection to the database
conn = sqlite3.connect('database.db')

# Create the table if it does not exist
conn.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name TEXT, value INTEGER)''')

# Seed the table with example data
example_data = [('Alice', 25), ('Bob', 30), ('Charlie', 35), ('Dave', 40), ('Eve', 45), ('Frank', 50),
                ('Grace', 55), ('Henry', 60), ('Ivy', 65), ('John', 70), ('Kate', 75), ('Leo', 80),
                ('Mary', 85), ('Nancy', 90), ('Oscar', 95), ('Peggy', 100), ('Quincy', 105), ('Rachel', 110),
                ('Steve', 115), ('Tina', 120)]

for data in example_data:
    conn.execute("INSERT INTO users (name, value) VALUES (?, ?)", data)

# Commit the transaction
conn.commit()

# Close the connection
conn.close()
