import sqlite3

conn = sqlite3.connect('database.db')
conn.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    account_type TEXT NOT NULL
);
''')
conn.commit()

def add_user(username, email, password, phone_number, account_type='Employee'):
    conn.execute('''
    INSERT INTO users (username, email, password, phone_number, account_type)
    VALUES (?, ?, ?, ?, ?)
    ''', (username, email, password, phone_number, account_type))
    conn.commit()

def get_user(username):
    cursor = conn.execute('''
    SELECT * FROM users WHERE username = ?
    ''', (username,))
    return cursor.fetchone()

def delete_user(username):
    conn.execute('''
    DELETE FROM users WHERE username = ?
    ''', (username,))
    conn.commit()