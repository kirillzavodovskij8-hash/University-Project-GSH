import sqlite3

db = "data.db"

def conn():
    return sqlite3.connect(db)

def create():
    con = conn()
    cur = con.cursor()
    # name уникален — не будет повторов
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users_bd (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            password INTEGER NOT NULL
        )
    """)
    con.commit()
    con.close()

def add(name, password):
    con = conn()
    cur = con.cursor()
    # проверяем, есть ли уже запись с таким name
    cur.execute("SELECT id FROM users_bd WHERE name = ?", (name,))
    result = cur.fetchone()
    if result is None:
        # вставляем только если записи нет
        cur.execute("INSERT INTO users_bd (name, password) VALUES (?, ?)", (name, password))
        con.commit()
    con.close()

def list_table():
    con = conn()
    cur = con.cursor()
    cur.execute("SELECT * FROM users_bd")
    rows = cur.fetchall()
    for row in rows:
        print(row[1], row[2])
    con.close()

if __name__ == "__main__":
    create()
    add("admin", 111)
    add("admin12", 111)  # не добавится
    list_table()