import sqlite3

conn = sqlite3.connect("new_db.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    salary REAL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS salary_log(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id INTEGER,
        old_salary REAL,
        new_salary REAL,
        change_date TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

cursor.execute("""
    CREATE TRIGGER IF NOT EXISTS salary_change_trigger
    AFTER UPDATE OF salary ON employees
    FOR EACH ROW
    WHEN OLD.salary != NEW.salary
    BEGIN
        INSERT INTO salary_log (employee_id, old_salary, new_salary)
        VALUES (OLD.id, OLD.salary, NEW.salary);
    END 
""")

cursor.execute("INSERT INTO employees (name, salary) VALUES ('Alex', 40000)")
conn.commit()

cursor.execute("UPDATE employees SET salary = 50000 WHERE name = 'Alex'")
conn.commit()

cursor.execute("SELECT * FROM salary_log")
info = cursor.fetchall()

for row in info:
    print(f"id: {row[0]}\n"
          f"name: {row[1]}\n"
          f"salary\n"
          f"before: {row[2]}\n"
          f"after: {row[3]}\n"
          f"date: {row[4]}\n")

conn.close()