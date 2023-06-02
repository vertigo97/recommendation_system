import streamlit as st
import sqlite3
import bcrypt

# Create a connection to the SQLite database
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create a table to store user information if it doesn't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        email TEXT,
        password_hash TEXT
    )
''')
conn.commit()

def signup_user(username, email, password):
    # Check if the username already exists
    c.execute('SELECT * FROM users WHERE username = ?', (username,))
    if c.fetchone():
        return False

    # Generate a password hash
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # Insert the new user into the database
    c.execute('INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)', (username, email, password_hash))
    conn.commit()
    return True

def main():
    st.title("User Sign Up")

    # Username input
    username = st.text_input("Enter username")

    # Email input
    email = st.text_input("Enter email")

    # Password input
    password = st.text_input("Enter password", type="password")

    # Sign Up button
    if st.button("Sign Up"):
        if signup_user(username, email, password):
            st.success("Sign up successful!")
        else:
            st.error("Username already exists")

if __name__ == "__main__":
    main()
