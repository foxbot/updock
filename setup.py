import sqlite3

db = sqlite3.connect('data.db')
db.execute('''
    CREATE TABLE IF NOT EXISTS files (
        id integer PRIMARY KEY,
        name text UNIQUE NOT NULL,
        type text NOT NULL,
        data blob
    );
''')
db.commit()

print('ok')
