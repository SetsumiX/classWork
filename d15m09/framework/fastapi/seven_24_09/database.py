import sqlite3
from typing import List, Optional
class Database:
    def __init__(self, db_path: str = "todo.db"):
        self.db_path = db_path
        self.init_db()

    def get_connect(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_db(self):
        conn = self.get_connect()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQ NOT NULL,
            password TEXT NOT NULL,
            dateReg TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS todos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            task TEXT NOT NULL,
            complete BOOLEAN DEFAULT FALSE,
            dateCreate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """)
        conn.commit()
        conn.close()

    def get_user_todos(self, user_id: int) -> List[dict]:
        conn = self.get_connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, task, complete, dateCreate FROM todos WHERE user_id = ?", (user_id,))
        res = cursor.fetchall()
        conn.close()
        return [dict(row) for row in res]

    def authenticate_user(self, username:str, password:str) -> Optional[int]:
        conn = self.get_connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
        result = cursor.fetchone()
        conn.close()
        return result["id"] if result else None

    def create_user(self, username:str, password:str) -> Optional[int]:
        try:
            conn = self.get_connect()
            cursor = conn.cursor()

            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))

            user_id = cursor.lastrowid

            conn.commit()
            conn.close()

            return user_id

        except sqlite3.IntegrityError:
            return None

    def add_todo(self, user_id: int, task: str) -> bool:
        try:
            conn = self.get_connect()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO todos (user_id, task) VALUES (?, ?)", (user_id, task))
            conn.commit()
            conn.close()
            return True
        except:
            return False

    def del_todo(self, user_id: int, todo_id: int) -> bool:
        conn = self.get_connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM todos WHERE id = ? and user_id = ?", (todo_id, user_id))
        conn.commit()
        conn.close()
        return cursor.rowcount > 0

    def toggle_todo(self, user_id: int, todo_id: int) -> bool:
        conn = self.get_connect()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE todos SET complete = NOT complete WHERE id = ? AND user_id = ?",
            (todo_id, user_id))
        conn.commit()
        conn.close()
        return cursor.rowcount > 0