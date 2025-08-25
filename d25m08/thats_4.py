import sqlite3

conn = sqlite3.connect("baza4.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS items(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        item_name TEXT)
    """)

cursor.execute("INSERT INTO items (category, item_name) VALUES ('Vegetable', 'Corn')")
cursor.execute("INSERT INTO items (category, item_name) VALUES ('Fruit', 'Banana')")
cursor.execute("INSERT INTO items (category, item_name) VALUES ('Fruit', 'Apple')")
cursor.execute("INSERT INTO items (category, item_name) VALUES ('Vegetable', 'Potato')")

conn.commit()

cursor.execute("""
    SELECT category, GROUP_CONCAT(item_name, ', ') AS items
    FROM items
    GROUP BY category
""")

arr = cursor.fetchall()
for row in arr:
    print(f"Category: {row[0]}\n"
          f"Elements: {row[1]}\n")