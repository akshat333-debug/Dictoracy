import sqlite3

# Create a new SQLite database (or connect if it exists)
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create a table for users
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    voter_id TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

# Insert a sample user (Voter ID and Email)
c.execute('INSERT INTO users (voter_id, email) VALUES (?, ?)', ('123', 'jayeshpani14@gmail.com'))

# Save (commit) the changes and close the connection
conn.commit()
conn.close()
