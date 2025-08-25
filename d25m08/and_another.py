import sqlite3

conn = sqlite3.connect("baza_another.db")
cursor = conn.cursor()

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS sales(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         product TEXT NOT NULL,
#         amount REAL)
#     """)
#
# cursor.execute("INSERT INTO sales (product, amount) VALUES ('A', 100)")
# cursor.execute("INSERT INTO sales (product, amount) VALUES ('B', 150)")
# cursor.execute("INSERT INTO sales (product, amount) VALUES ('A', 200)")
#
# conn.commit()

cursor.execute("""
    SELECT product, amount,
        ROW_NUMBER() OVER (ORDER BY product DESC) AS row_num
    FROM sales
""")

arr = cursor.fetchall()
for row in arr:
    print(f"Product: {row[0]}\n"
          f"Amount: {row[1]}\n"
          f"Number row: {row[2]}\n")