
import streamlit as st
import psycopg2

def connect_db():
    return psycopg2.connect(
        host="db",
        dbname="mydatabase",
        user="myuser",
        password="mypassword",
        port=5432
    )

st.title("Streamlit + PostgreSQL Example")

try:
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users;")
    rows = cursor.fetchall()
    for row in rows:
        st.write(row)
    cursor.close()
    conn.close()
except Exception as e:
    st.error(f"Error: {e}")

