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
                return f"User: {name} {surname} с номером телефона - {phone}, был добавлен"
            except sqlite3.IntegrityError as e:
                if "phone" in str(e).lower() or "UNIQUE constraint failed" in str(e):
                    print(f"Error. User with this phone already is used ({phone})")
                    return f"Error. User with this phone already is used ({phone})"
                else:
                    print(f"Unknown error. {e}")
                    return f"Unknown error. {e}"

    def show_all_users(self):
        with sqlite3.connect(self.db) as connect:
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM people")
            result = cursor.fetchall()
            if not result:
                print("Book is empty")
                return []
            for row in result:
                print(f"id: {row[0]}\n"
                      f"Имя: {row[1]}\n"
                      f"Фамили: {row[2]}\n"
                      f"Отчество: {row[3]}\n"
                      f"Город: {row[4]}\n"
                      f"Код города: {row[5]}\n"
                      f"Номер телефона: {row[6]}\n")
            return result

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
            return False, "Не введён номер телефона"
        with sqlite3.connect(self.db) as connect:
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM people WHERE phone = ?", [phone])
            result = cursor.fetchone()
            if not result:
                print(f"Данные не найдены по данному => {phone} номеру телефона")
                return False, f"Данные не найдены по данному => {phone} номеру телефона"
            cursor.execute("DELETE FROM people WHERE phone = ?", [phone])
            connect.commit()
            return True, "Удаление произведено успешно"

            # print(f"id: {result[0]}\n"
            #       f"Имя {result[1]}\n"
            #       f"Фамилия {result[2]}\n{result[3]}\n{result[4]}\n{result[5]}\n{result[6]}\n")
            # conf = input(f"Хотите удалить эти данные?\n"
            #              f"Ввод(y/n(any)):").strip()
            # if conf == "y":
            #     cursor.execute("DELETE FROM people WHERE phone = ?", [phone])
            #     print("Удаление произведено успешно")
            # connect.commit()
            # return True

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
        add_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(add_frame, text="Add User")

        ttk.Label(add_frame, text="Name*: ").grid(row=0, column=0, sticky=tkinter.W, pady=5)
        self.name_entry = ttk.Entry(add_frame, width=30)
        self.name_entry.grid(row=0, column=1, pady=5, padx=(10, 0))

        ttk.Label(add_frame, text="Surname*: ").grid(row=2, column=0, sticky=tkinter.W, pady=5)
        self.surname_entry = ttk.Entry(add_frame, width=30)
        self.surname_entry.grid(row=2, column=1, pady=5, padx=(10, 0))

        ttk.Label(add_frame, text="Phone*: ").grid(row=3, column=0, sticky=tkinter.W, pady=5)
        self.phone_entry = ttk.Entry(add_frame, width=30)
        self.phone_entry.grid(row=3, column=1, pady=5, padx=(10, 0))

        ttk.Label(add_frame, text="Middlename: ").grid(row=4, column=0, sticky=tkinter.W, pady=5)
        self.middlename_entry = ttk.Entry(add_frame, width=30)
        self.middlename_entry.grid(row=4, column=1, pady=5, padx=(10, 0))

        ttk.Label(add_frame, text="City: ").grid(row=5, column=0, sticky=tkinter.W, pady=5)
        self.city_entry = ttk.Entry(add_frame, width=30)
        self.city_entry.grid(row=5, column=1, pady=5, padx=(10, 0))

        ttk.Label(add_frame, text="City code: ").grid(row=6, column=0, sticky=tkinter.W, pady=5)
        self.citycode_entry = ttk.Entry(add_frame, width=30)
        self.citycode_entry.grid(row=6, column=1, pady=5, padx=(10, 0))

        add_button = ttk.Button(add_frame, text="Add User", command=self.add_user)
        add_button.grid(row=7, column=0, pady=20)

        self.add_result_text = tkinter.Text(add_frame, height=10, width=60)
        self.add_result_text.grid(row=8, column=0, columnspan=2, pady=10)

        scrollbar = ttk.Scrollbar(add_frame, orient="vertical", command=self.add_result_text.yview)
        scrollbar.grid(row=8, column=2, sticky=(tkinter.W, tkinter.S))
        self.add_result_text.configure(yscrollcommand=scrollbar.set)

    def create_search_tab(self):
        search_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(search_frame, text="Search")

        search_fields = [
            ("name", "Name: "),
            ("surname", "Surname: "),
            ("phone", "Phone: "),
            ("middlename", "Middlename: "),
            ("city", "City: "),
            ("city_code", "City code: ")
        ]
        self.search_entries = {}
        for i, (field, label) in enumerate(search_fields):
            ttk.Label(search_frame, text=label).grid(row=i, column=0, sticky=tkinter.W, pady=2)
            entry = ttk.Entry(search_frame, width=30)
            entry.grid(row=i, column=1, pady=2, padx=(10, 0))
            self.search_entries[field] = entry

        button_frame = ttk.Frame(search_frame)
        button_frame.grid(row=len(search_fields), column=0, columnspan=2, pady=10)

        search_button = ttk.Button(button_frame, text="Поиск", command=self.search_users)
        search_button.pack(side=tkinter.LEFT, padx=5)

        clear_button = ttk.Button(button_frame, text="Очистить", command=self.clear_search)
        clear_button.pack(side=tkinter.LEFT, padx=5)

        columns = ("ID", "Name", "Surname", "Middlename", "City", "City_code", "Phone")
        self.search_tree = ttk.Treeview(search_frame, columns=columns, show="headings", height=15)

        for col in columns:
            self.search_tree.heading(col, text=col)
            self.search_tree.column(col, width=100)
        self.search_tree.grid(row=len(search_fields) + 1, column=0, columnspan=2, pady=10, sticky=(tkinter.W, tkinter.E, tkinter.N, tkinter.S))

        v_scrollbar = ttk.Scrollbar(search_frame, orient="vertical", command=self.search_tree.yview)
        v_scrollbar.grid(row=len(search_fields) + 1, column=2, sticky=(tkinter.N, tkinter.S))
        self.search_tree.configure(yscrollcommand=v_scrollbar.set)

        h_scrollbar = ttk.Scrollbar(search_frame, orient="horizontal", command=self.search_tree.xview)
        h_scrollbar.grid(row=len(search_fields) + 2, column=2, columnspan=2, sticky=(tkinter.W, tkinter.E))
        self.search_tree.configure(xscrollcommand=h_scrollbar.set)

        search_frame.columnconfigure(1, weight=1)
        search_frame.rowconfigure(len(search_fields) + 1, weight=1)

    def create_view_tab(self):
        view_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(view_frame, text="Все пользователи")

        refresh_button = ttk.Button(view_frame, text="Обновить", command=self.load_all_users)
        refresh_button.pack(pady=(0, 10))
        columns = ("ID", "Name", "Surname", "Middlename", "City", "City_code", "Phone")

        self.view_tree = ttk.Treeview(view_frame, columns=columns, show="headings", height=20)
        for col in columns:
            self.view_tree.heading(col, text=col)
            self.view_tree.column(col, width=100)
        self.view_tree.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(view_frame, orient="vertical", command=self.view_tree.yview)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.view_tree.configure(yscrollcommand=scrollbar.set)
        self.load_all_users()
    def create_delete_tab(self):
        delete_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(delete_frame, text="Удалить")

        ttk.Label(delete_frame, text="Введите номер телефона").pack(pady=(0, 10))
        self.delete_phone_entry = ttk.Entry(delete_frame, width=30)
        self.delete_phone_entry.pack(pady=(0, 20))

        delete_button = ttk.Button(delete_frame, text="Удалите пользователя", command=self.delete_user)
        delete_button.pack()

        self.delete_result_text = tkinter.Text(delete_frame, height=15, width=60)
        self.delete_result_text.pack(pady=10)
        scrollbar = ttk.Scrollbar(delete_frame, orient="vertical", command=self.delete_result_text.yview)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.delete_result_text.configure(yscrollcommand=scrollbar.set)


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

    def add_user(self):
        name = self.name_entry.get().strip().title()
        surname = self.surname_entry.get().strip().title()
        middlename = self.middlename_entry.get().strip().title() or None
        phone = self.phone_entry.get().strip()
        city = self.city_entry.get().strip().title() or None
        city_code = self.citycode_entry.get().strip() or None
        if not name or not surname or not phone:
            messagebox.showerror("Ошибка", "Не введены обязательные поля. Имя, Фамилия или Номер телефона.")
            return
        result = self.phonebook.add_user(name, surname, phone, middlename, city, city_code)
        self.add_result_text.insert(tkinter.END, result + "\n")
        self.add_result_text.see(tkinter.END)
        self.name_entry.delete(0, tkinter.END)
        self.surname_entry.delete(0, tkinter.END)
        self.middlename_entry.delete(0, tkinter.END)
        self.phone_entry.delete(0, tkinter.END)
        self.city_entry.delete(0, tkinter.END)
        self.citycode_entry.delete(0, tkinter.END)

        self.load_all_users()

    def search_users(self):
        search_params = {}
        for field, entry in self.search_entries.items():
            value = entry.get().strip()
            if value:
                search_params[field] = value
        if not search_params:
            messagebox.showwarning("Внимание", "Вы не ввели ни одного параметра для поиска")
            return

        result = self.phonebook.search_user(**search_params)

        for item in self.search_tree.get_children():
            self.search_tree.delete(item)

        for row in result:
            self.search_tree.insert("", "end", values=row)
        messagebox.showinfo("Результат поиска", f"Найдено: {len(result)} шт.")

    def delete_user(self):
        phone = self.delete_phone_entry.get().strip()
        if not phone:
            messagebox.showerror("Ошибка", "Пожалуйста введите номер телефона")
            return
        if messagebox.askyesno("Подтвердите удаление", f"Вы точно хотите удалить информацию по этому номеру телефона? - {phone}"):
            success, message = self.phonebook._del_user(phone)
            self.delete_result_text.insert(tkinter.END, message + "\n")
            self.delete_result_text.see(tkinter.END)
            if success:
                self.delete_phone_entry.delete(0, tkinter.END)
                self.load_all_users()

    def clear_search(self):
        for entry in self.search_entries.values():
            entry.delete(0, tkinter.END)
        for item in self.search_tree.get_children():
            self.search_tree.delete(item)

    def load_all_users(self):
        for item in self.view_tree.get_children():
            self.view_tree.delete(item)

        users = self.phonebook.show_all_users()
        for user in users:
            self.view_tree.insert("", "end", values=user)

    def show_version(self):
        messagebox.showinfo("Version", "Phone book Application\nVersion 0.1\nA simple phone book with GUI")

def main():
    root = tkinter.Tk()
    app = PhonebookGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()