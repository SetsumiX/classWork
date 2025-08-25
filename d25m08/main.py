import sqlite3

conn = sqlite3.connect("baza.db")

cursor = conn.cursor()
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS products(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         price REAL)
#     """)
#
# cursor.execute("INSERT INTO products (name, price) VALUES ('Apple', 1.2)")
# cursor.execute("INSERT INTO products (name, price) VALUES ('Banana', 1.0)")
# cursor.execute("INSERT INTO products (name, price) VALUES ('Orange', 1.3)")
#
# conn.commit()

cursor.execute("SELECT COUNT(*) FROM products")
count = cursor.fetchone()[0]
print(f"Всего продуктов: {count}")

cursor.execute("SELECT SUM(price) FROM products")
total = cursor.fetchone()[0]
print(f"Общая цена продуктов: {total}")

cursor.execute("SELECT AVG(price) FROM products")
avg_price = cursor.fetchone()[0]
print(f"Средняя цена всех продуктов: {avg_price:2f}")

cursor.execute("SELECT MAX(price) FROM products")
max_price = cursor.fetchone()[0]
print(f"Максимальная цена продукта: {max_price}")

cursor.execute("SELECT MIN(price) FROM products")
min_price = cursor.fetchone()[0]
print(f"Минимальная цена продукта: {min_price}")

cursor.execute("SELECT name, UPPER(name), LENGTH(name) FROM products")
ar = cursor.fetchall()
for row in ar:
    print(f"\nOriginal: {row[0]}\n"
          f"Upper: {row[1]}\n"
          f"Length: {row[2]}\n")

cursor.execute("""
    SELECT name, price,
        CASE
            WHEN price < 1 THEN 'Cheap'
            WHEN price BETWEEN 1 AND 1.3 THEN 'Middle'
            ELSE 'Expansive'
        END AS price_category
    FROM products
""")

arr = cursor.fetchall()
for row in arr:
    print(f"Name: {row[0]}\n"
          f"Price: {row[1]}\n"
          f"Price category: {row[2]}\n")

conn.close()