import sqlite3

connect = sqlite3.connect("first.db")
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS student_courses(
    student_id INTEGER,
    course_id INTEGER,
    enrollment_data TEXT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
    )
""")

st_dt = [
    ("Иван Иванов",),
    ("Пётр Петров",),
    ("Ирина Иринова",)
]

crs_dt = [
    ("Математика",),
    ("Физика",),
    ("Астрономия",)
]
cursor.executemany("INSERT INTO students (name) VALUES (?)", st_dt)

cursor.executemany("INSERT INTO courses (title) VALUES (?)", crs_dt)

st_cr_data = [
    (1, 1, "2024-01-15"),
    (1, 2, "2024-01-15"),
    (2, 2, "2024-01-20"),
    (2, 3, "2024-01-20"),
    (3, 1, "2024-01-03"),
    (3, 3, "2024-01-03")
]

cursor.executemany("INSERT INTO student_courses (student_id, course_id, enrollment_data) VALUES (?, ?, ?)", st_cr_data)

print("<<<< Многие ко многим >>>>")

cursor.execute("""
    SELECT students.name, courses.title, student_courses.enrollment_data
    FROM students
    INNER JOIN student_courses ON students.id = student_courses.student_id
    INNER JOIN courses ON courses.id = student_courses.course_id
    ORDER BY students.name
""")

for name, course, data in cursor.fetchall():
    print(f"{name}: {course}\n"
          f"Дата поступления: {data}\n")

connect.close()