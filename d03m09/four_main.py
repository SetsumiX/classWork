import sqlite3

connect = sqlite3.connect("first.db")
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS employee(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    position TEXT,
    manager_id INTEGER,
    FOREIGN KEY (manager_id) REFERENCES employee(id)
    )
""")

emp_data = [
    ("Иван Иванов", "менеджер", None),
    ("Пётр Петров", "разраб", 1),
    ("Ирина Иринова", "графика", 2)
]

cursor.executemany("""
    INSERT INTO employee(name, position, manager_id)
    VALUES (?, ?, ?)
""", emp_data)

print("<<<< Самосвязь >>>>")

cursor.execute("""
    SELECT e.name AS employee, e.position, m.name AS manager, m.position AS manager_position
    FROM employee e
    Left JOIN employee m ON e.manager_id = m.id
    ORDER BY e.id
""")

for name, pos, manager, manag_pos in cursor.fetchall():
    print(f"{name} ({pos}) >>> {manager} ({manag_pos})")

connect.close()