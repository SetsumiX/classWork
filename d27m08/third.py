import sqlite3

conn = sqlite3.connect("new_db.db")
cursor = conn.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS sales (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     product TEXT,
#     quantity INTEGER,
#     price REAL
#     )
# """)
#
# products_data = [
#     ('phone', 1, 500),
#     ('notebook', 2, 1000),
#     ('phone', 3, 350),
#     ('pad', 2, 380),
#     ]
#
# cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", products_data)
#
# conn.commit()

cursor.execute("""
    WITH products_total AS (
        SELECT
            product,
            SUM(quantity * price) AS total_revenue
        FROM sales
        GROUP BY product
        )
        SELECT
            product,
            total_revenue,
            ROUND(total_revenue * 100.0 / SUM(total_revenue) OVER(), 2) AS percentage
        FROM products_total
        ORDER BY total_revenue DESC
    """)

arr = cursor.fetchall()

print(f"Products info: ")
print(f"Product   | revenue | percent")
print("-" * 30)
for row in arr:
    print(f"{row[0]:9} | {row[1]:7} | {row[2]:6}%")

conn.close()