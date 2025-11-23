import sqlite3

# Connect to database (creates if doesn't exist)
conn = sqlite3.connect('database and sqlAlchemy/site.db')

# Create cursor
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
''')

# Insert data
# cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", 
#                ('John Doe', 'john@example.com'))

# Commit and close
conn.commit()
conn.close()