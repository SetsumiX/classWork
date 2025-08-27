import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
    )
""")

students = [('Anna',), ('Alex',), ('Victoria',), ('Sam',), ('Dima',)]

cursor.executemany("INSERT INTO students (name) VALUES (?)", students)

conn.commit()

cursor.execute("SELECT name FROM students ORDER BY RANDOM() LIMIT 1")
rand_student = cursor.fetchone()[0]

print(rand_student)

cursor.execute("SELECT RANDOM() AS rand_num")
rand_num = cursor.fetchone()[0]
print(rand_num)

conn.close()