import sqlite3
import tkinter
from tkinter import ttk, messagebox, simpledialog

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
                      f"Имя: {row[1]}\n"
                      f"Фамили: {row[2]}\n"
                      f"Отчество: {row[3]}\n"
                      f"Город: {row[4]}\n"
                      f"Код города: {row[5]}\n"
                      f"Номер телефона: {row[6]}\n")

    def search_user(self, **kwargs):
        if not kwargs:
            print(f"Нет параметров для поиска 222")
            return []
        conditions = []
        values = []

        for key, value in kwargs.items():
            if key in ["name", "surname", "middlename", "city", "code_city", "phone"]:
                conditions.append(f"{key} LIKE ?")
                values.append(f"%{value}%")
        if not conditions:
            print("Нет параметров для поиска 333")
            return []
        query = "SELECT * FROM people WHERE " + "AND ".join(conditions)
        with sqlite3.connect(self.db) as connect:
            cursor = connect.cursor()
            cursor.execute(query, values)
            result = cursor.fetchall()

            if result:
                print(f"Найдено {len(result)} по запросу:")
                for row in result:
                    print(f"id: {row[0]}\n"
                          f"ФИО: {row[1]} {row[2]} {row[3]}\n"
                          f"Город с его кодом: {row[4]} {row[5]}\n"
                          f"Номер телефона: {row[6]}\n")
            else:
                print("Ничего не найдено")
            return result

    def _del_user(self, phone):
        if not phone:
            print("Не введён телефон")
            return False
        with sqlite3.connect(self.db) as connect:
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM people WHERE phone = ?", [phone])
            result = cursor.fetchone()
            if not result:
                print(f"Данные не найдены по данному => {phone} номеру телефона")
                return False
            print(f"id: {result[0]}\n"
                  f"Имя {result[1]}\n"
                  f"Фамилия {result[2]}\n{result[3]}\n{result[4]}\n{result[5]}\n{result[6]}\n")
            conf = input(f"Хотите удалить эти данные?\n"
                         f"Ввод(y/n(any)):").strip()
            if conf == "y":
                cursor.execute("DELETE FROM people WHERE phone = ?", [phone])
                print("Удаление произведено успешно")
            connect.commit()
            return True

class PhonebookGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Phonebook")
        self.root.geometry("1300x800")
        self.phonebook = PhoneBook()
        self.create_widgets()
        self.create_menu()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tkinter.W, tkinter.E, tkinter.N, tkinter.S))
        title_label = ttk.Label(main_frame, text="Phonebook", font=("Times New Roman", 20, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        self.notebook = ttk.Notebook(main_frame)
        self.notebook.grid(row=1, column=0, columnspan=2, sticky=(tkinter.W, tkinter.E, tkinter.N, tkinter.S))

        self.create_add_tab()
        self.create_search_tab()
        self.create_view_tab()
        self.create_delete_tab()
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)

    def create_add_tab(self):
        ...

    def create_search_tab(self):
        ...

    def create_view_tab(self):
        ...

    def create_delete_tab(self):
        ...


    def create_menu(self):
        menubar = tkinter.Menu(self.root)
        self.root.config(menu = menubar)

        file_menu = tkinter.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label="Refresh all", command=self.load_all_users)
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=self.root.quit)

        help_menu = tkinter.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        file_menu.add_command(label="Version", command=self.show_version)

    def load_all_users(self):
        ...

    def show_version(self):
        messagebox.showinfo("Version", "Phone book Application\nVersion 0.1\nA simple phone book with GUI")

def main():
    root = tkinter.Tk()
    app = PhonebookGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()