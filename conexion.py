import sqlite3 as sql

def dbOpen():
    conn = sql.connect('trabajadoresDB.db')

    return conn
