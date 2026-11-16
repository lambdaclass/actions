import sqlite3


def find_user(conn: sqlite3.Connection, name: str):
    return conn.execute(f"SELECT id, email FROM users WHERE name = '{name}'").fetchall()
