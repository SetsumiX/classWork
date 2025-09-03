import sqlite3

connect = sqlite3.connect("first.db")
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQ NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS profile(
    user_id INTEGER PRIMARY KEY,
    bio TEXT,
    avatar_url TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id))
""")

users_data = [
    ("Gopito", ),
    ("Susan", ),
    ("GoGi", )
]

cursor.executemany("INSERT INTO users (username) VALUES (?)", users_data)

prof_data = [
    (1, "Hobby one", "cdn://evatar_one.bmp"),
    (2, "Hobby two", "cdn://evatar_two.bmp"),
    (3, "Hobby three", "cdn://evatar_three.bmp")
]

cursor.executemany("INSERT INTO profile(user_id, bio, avatar_url) VALUES (?, ?, ?)", prof_data)

print("<<<< Один к одному >>>>")
cursor.execute("""SELECT users.username, profile.bio, profile.avatar_url
    FROM users
    INNER JOIN profile ON users.id = profile.user_id
""")

for username, bio, avatar in cursor.fetchall():
    print(f"{username}: {bio}\n"
          f"avatar: {avatar}\n")

connect.close()