import sqlite3

class PhoneBook:
    def __init__(self, db="phonebook.db"):
        self.db = db
        self.create_table()

    def create_table(self):
        with sqlite3.connect(self.db) as connect:
            cursor = connect.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS people(
                    _id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    surname TEXT NOT NULL,
                    middlename TEXT,
                    city TEXT,
                    code_city,
                    phone TEXT UNIQ)
            """)
            connect.commit()

    def add_user(self, name, surname, phone, middlename=None, city=None, code_city=None):
        with sqlite3.connect(self.db) as connect:
            try:
                cursor = connect.cursor()
                new_user = (name, surname, middlename, city, code_city, phone)
                cursor.execute("""INSERT INTO people (name, surname, middlename, city, code_city, phone)
                                VALUES (?,?,?,?,?,?)""", new_user)
                print(f"Данные нового человека были добавлены:\n"
                      f"{name}\n"
                      f"{surname}\n"
                      f"{middlename}\n"
                      f"{city}\n"
                      f"{code_city}\n"
                      f"{phone}\n")
            except sqlite3.IntegrityError as e:
                if "phone" in str(e).lower() or "UNIQUE constraint failed" in str(e):
                    print(f"Error. User with this phone already is used ({phone})")
                else:
                    print(f"Unknown error. {e}")

    def show_all_users(self):
        with sqlite3.connect(self.db) as connect:
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM people")
            result = cursor.fetchall()
            if not result:
                print("Book is empty")
                return None
            for row in result:
                print(f"id: {row[0]}\n"
                      f"Name: {row[1]}\n"
                      f"Surname: {row[2]}\n"
                      f"Middle name: {row[3]}\n"
                      f"City: {row[4]}\n"
                      f"Code of city: {row[5]}\n"
                      f"Phone: {row[6]}\n")

if __name__ == "__main__":
    phonebook = PhoneBook()

    phonebook.show_all_users()
    phonebook.add_user("Валд", "Бачков", "9922243345", "Вэнымонымовыч", "Вожешкий", "431")
    phonebook.show_all_users()