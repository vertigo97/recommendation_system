import streamlit as st
import sqlite3
import bcrypt

# Create a connection to the SQLite database
conn = sqlite3.connect('users.db')
c = conn.cursor()

def login_user(username, password):
    c.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = c.fetchone()
    if user:
        password_hash = user[3]
        if bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8')):
            return True
    return False

def main():
    st.title("User Login")

    # Username input
    username = st.text_input("Enter username")

    # Password input
    password = st.text_input("Enter password", type="password")

    # Login button
    if st.button("Log In"):
        if login_user(username, password):
            st.success("Logged in successfully!")
            if st.session_state.login_success:
                st.markdown(f"[Click here to access the app](http://localhost:8501/)")
        else:
            st.error("Invalid username or password")
            st.session_state.login_success = False

if __name__ == "__main__":
    st.session_state.login_success = True
    main()
