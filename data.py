import sqlite3

db_name = "data_base.db"

def conn():
    return sqlite3.connect(db_name)


def create():
    con = conn()
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    pasword INTEGER,)
    """)
    con.commit()
    con.close()
def list_table():
    con = conn()
    cur = con.cursor()
    cur.execute("SELECT * FROM table")
    a = cur.fetchall()
    for row in a:
        print(row[1], row[2])
    con.commit()
    con.close()

def add(name, password):
    con = conn()
    cur = con.cursor()
    cur.execute("INSERT INTO users (name, password) VALUES (?, ?)", (name, password))
    con.commit()
    con.close()

create()
add("admin", 111)
list_table()