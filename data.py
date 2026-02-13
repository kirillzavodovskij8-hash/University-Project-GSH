import sqlite3

db_name = "base"

def conn():
    return sqlite3.connect(db_name)
    

def create():
    con = conn()
    cur = con.cursor()
    cur.execute(((
        """CREATE TABLE IF NOT EXISTS table
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        pasword INTEGER,
        """
    )))

def list_table():
    con = conn()
    cur = con.cursor()
    cur.execute("SELECT * FROM table")
    a = cur.fetchall()
    for name, password in a:
        print(name, password)
    con.close()
