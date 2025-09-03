import sqlite3

connect = sqlite3.connect("first.db")
cursor = connect.cursor()

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
    genre TEXT,
    author_id INTEGER,
    FOREIGN KEY(author_id) REFERENCES authors(id)
    )
""")

authors_data = [
    ("Лев Толстой",),
    ("Фёдор Достоевский",),
    ("Антон Чехов",)
]

cursor.executemany("INSERT INTO authors(name) VALUES (?)", authors_data)

books_data = [
    ("Война и мир", "", 1),
    ("Анна Каренина", "", 1),
    ("Приступление и наказание", "", 2),
    ("Чайка", "", 3)
]

cursor.executemany("INSERT INTO books(name, genre, author_id) VALUES (?, ?, ?)", books_data)

print("<<<< Один ко многим >>>>")
cursor.execute("""
    SELECT authors.name, books.name FROM authors
    INNER JOIN books ON authors.id = books.author_id
    ORDER BY authors.name
""")

for aut, boo in cursor.fetchall():
    print(f"Автор: {aut} - книга: {boo}")

connect.close()