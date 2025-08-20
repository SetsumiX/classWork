import sqlite3

# conn = sqlite3.connect("example.db")
#
# cursor = conn.cursor()
#
# cursor.execute(
#     '''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         age INTEGER)
#     ''')
#
# conn.commit()
# conn.close()



# INTEGER - целочилсенное
# REAL - числа с плавающей точкой
# NUMERIC - общий тип, между целыми и дробными
# BOOLEAM - true false, только будет 1 или 0
# TEXT - обычное хранение строк(при написании даты, формат таков: гггг/мм/дд)
# CHAR(10) - текстовое хранение с огранечением по символам
# VARCHAR(255) - 255 максимальное огранечение символов, всё тот же char
# BLOB - бинарное значение(хранение картинок)
# PRIMARY KEY - первичный ключ, индификатор(id), который не может повторяться
# AUTOINCREMENT - автоматическое увеличение значения
# NOT NULL - поле становится обязательным для заполнения
# UNIQUE - уникальное значение, которое не может повторяться
# DEFAULT "value" - при создании пользователя/поля, автоматически заполняется, если не происходит какого либо заполнения
# CHECK (age > 18) - проверка каких либо значений, при заполнении
# FOREIGN KEY - не понял



# conn = sqlite3.connect("new_test.db")
# cursor = conn.cursor()
# cursor.execute(
#     '''
#     CREATE TABLE IF NOT EXISTS employee(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         first_name TEXT NOT NULL,
#         lust_name TEXT NOT NULL,
#         salary REAL,
#         age INTEGER DEFAULT 18,
#         email TEXT UNIQUE,
#         photo BLOB,
#         hire_data TEXT,
#         CHECK (age>=16),
#         emp_code CHAR(6) UNIQUE NOT NULL)
#     '''
# )
#
# conn.commit()
# conn.close()



# conn = sqlite3.connect("example.db")
# cursor = conn.cursor()
# cursor.execute("""
#     INSERT INTO users (name, age) VALUES ("Ivan", 25)
# """)
#
# users_data = [
#     ("Dima", 30),
#     ("Karina", 23),
#     ("Yulia", 19)
# ]
#
# cursor.executemany("""
#     INSERT INTO users (name, age) VALUES (?, ?)
# """, users_data)
#
# conn.commit()
# conn.close()



# conn = sqlite3.connect("example.db")
# cursor = conn.cursor()
# cursor.execute("""
#     SELECT * FROM users
# """) # * - берёт все данные

# all_users = cursor.fetchall()
# print("All users", all_users)
# one_user = cursor.fetchone()
# print("The first user", one_user)

# cursor.execute("SELECT name, age FROM users")
# usrs = cursor.fetchone()
# print(usrs)

# cursor.execute("SELECT * FROM users WHERE age > 25")
# old_usrs = cursor.fetchall()
# print(old_usrs)

# cursor.execute("SELECT * FROM users ORDER BY age DESC") # ORDER BY - сортировка по, DESC - порядок убывания. Если по возростанию, не пишем DESC
# usrs = cursor.fetchall()
# print(usrs)

# cursor.execute("SELECT * FROM users LIMIT 2") # LIMIT - выводить только определённое количество, начиная с первого
# usrs = cursor.fetchall()
# print(usrs)

# conn.close()



# conn = sqlite3.connect("example.db")
# cursor = conn.cursor()
# cursor.execute("""
#     UPDATE users SET age = 30 WHERE id = 1
# """)

# conn.commit()
#
# cursor.execute("SELECT * FROM users LIMIT 2")
# usrs = cursor.fetchall()
# print(usrs)

# cursor.execute("""
#     UPDATE users SET name = ?, age = ? WHERE id = 1
# """, ("Alex", 24))
#
# conn.commit()
#
# cursor.execute("SELECT * FROM users LIMIT 2")
# usrs = cursor.fetchall()
# print(usrs)

# cursor.execute("""
#     UPDATE users SET age = age + 1 WHERE age < 20
# """)
#
# conn.commit()
#
# cursor.execute("SELECT * FROM users")
# usrs = cursor.fetchall()
# print(usrs)

# conn.close()



# conn = sqlite3.connect("example.db")
# cursor = conn.cursor()
#
# data = [(9,), (12,)]
# # cursor.execute("DELETE FROM users WHERE id = 4")
# # cursor.execute("DELETE FROM users WHERE age >= 30")
# cursor.executemany("DELETE FROM users WHERE id = ?", data)
#
# conn.commit()
#
# cursor.execute("SELECT * FROM users")
# usrs = cursor.fetchall()
# print(usrs)
#
# conn.close()



conn = sqlite3.connect("example.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS users") # DROP TABLE - удаляет всю таблицу данных

conn.commit()
conn.close()