import sqlite3

db = "data.db"

def conn():
    return sqlite3.connect(db)

def create():
    con = conn()
    cur = con.cursor()
    cur.execute("""CREATE TABLE table (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    pasword INTEGER NOT NULL,""")
    con.commit()
    con.close()

def add(name, pasword):
    con = conn()
    cur = con.cursor()
    cur.execute("INSERT INTO table (name, pasword) VALUES (?, ?)", (name, pasword))
    con.commit()
    con.close()


if __name__ == "__main__":
    create()
    add("admin", 111)