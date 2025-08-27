import sqlite3

conn = sqlite3.connect("new_db.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    nickname TEXT UNIQ,
    email TEXT UNIQ
    )
""")

cursor.execute("INSERT INTO users (name, nickname, email) VALUES ('Володя', 'Pro100Volodia', 'vold1985@mail.ru')")
cursor.execute("INSERT INTO users (name, nickname, email) VALUES ('Дарья', 'Sakuradzin', 'DB1223@gmail.com')")
cursor.execute("INSERT INTO users (name, nickname, email) VALUES ('Дима', 'Dims', 'dimon123321@gmail.com')")
cursor.execute("INSERT INTO users (name, nickname, email) VALUES ('NULL', 'NULL', 'coca999@gmail.com')")
conn.commit()

cursor.execute("""
    SELECT
        COALESCE(nickname, name, email, 'nameless') AS display_name
    FROM users
""")

arr = cursor.fetchall()

for row in arr:
    print(f"Name: {row[0]}\n")

conn.close()