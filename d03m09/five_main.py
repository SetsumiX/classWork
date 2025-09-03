import sqlite3

connect = sqlite3.connect("second.db")
cursor = connect.cursor()

cursor.execute("PRAGMA foreign_key=ON")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS authors(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQ NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    author_id INTEGER,
    FOREIGN KEY(author_id) REFERENCES authors(id) ON DELETE CASCADE
    )
""")

authors_data = [
    ("Лев Толстой",),
    ("Фёдор Достоевский",),
    ("Антоан де Сант-Экзюпери",)
]

cursor.executemany("INSERT INTO authors(name) VALUES (?)", authors_data)

books_data = [
    ("Война и мир", 1),
    ("Анна Каренина", 1),
    ("Приступление и наказание", 2),
    ("Маленький принц", 3)
]

cursor.executemany("INSERT OR IGNORE INTO books(name, author_id) VALUES (?, ?)", books_data)

print("<<<< Один ко многим >>>>")
cursor.execute("""
    SELECT books.name, authors.name FROM books
    JOIN authors ON books.author_id = authors.id
""")

for row in cursor.fetchall():
    print(f"{row}")

ath = "Фёдор Достоевский"
cursor.execute("""
    SELECT books.name
    FROM books
    JOIN authors ON books.author_id = authors.id
    WHERE authors.name = ?
""", (ath,))

for row in cursor.fetchall():
    print(row)

cursor.execute("""
    DELETE FROM authors
    WHERE name = "Лев Толстой"
""")

print("Удаление...")
cursor.execute("""
    SELECT books.name, authors.name
    FROM books
    JOIN authors ON books.author_id = authors.id
    WHERE authors.name = ?
""", (ath,))
for row in cursor.fetchall():
    print(row)

connect.close()