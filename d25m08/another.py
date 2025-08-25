import sqlite3

conn = sqlite3.connect("baza_another.db")

cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS events(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        event_name TEXT NOT NULL,
        event_date TEXT)
    """)

cursor.execute("INSERT INTO events (event_name, event_date) VALUES ('Meeting', '2024-04-05')")

conn.commit()

cursor.execute("SELECT DATE('now')")
today = cursor.fetchone()[0]
print(f"Today {today}")

cursor.execute("SELECT event_name, strftime('%Y', event_date) FROM events")
arr = cursor.fetchall()
for row in arr:
    print(f"Event {row[0]}, Year: {row[1]}")