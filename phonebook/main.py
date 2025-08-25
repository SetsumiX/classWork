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

def main(arg):
    while True:
        t = input(f"Введите действие\n"
                  f"1 - Добавить данные\n"
                  f"2 - Показать все данные\n"
                  f"3 - Поиск данных по параметрам\n"
                  f"4 - Удалить данные\n"
                  f"any - Выход\n"
                  f"Ввод:>>> ")
        match t:
            case "1":
                arg.add_user(**send_data())
            case "2":
                print(f"<<< Номерная книжка >>>")
                arg.show_all_users()
            case "3":
                search_menu(arg)
            case "4":
                _del_menu(arg)
            case _:
                print(">>> Выход <<<")
                break

def send_data():
    return {
        "name": input("Имя >>> ").title(),
        "surname": input("Фамилия >>> ").title(),
        "middlename": input("Отчество(Если есть) >>> ").title(),
        "city": input("Город >>> ").title(),
        "code_city": input("Код области >>> "),
        "phone": input("Номер телефона >>> "),
    }

def search_menu(data):
    search_params = {}
    search_fields = {
        "name": "Имя",
        "surname": "Фамилия",
        "middlename": "Отчество",
        "city": "Город",
        "code_city": "Код области",
        "phone": "Номер телефона",
    }
    for field, descr in search_fields.items():
        value = input(f"Введите {descr} (если известно):>>>").strip()
        if value:
            search_params[field] = value
    if search_params:
        print(f"\nПоиск данных по параметрам {search_params}")
        data.search_user(**search_params)
    else:
        print(f"Параметры не введены для поиска 111")

def _del_menu(data):
    print(">>> Удаление данных пользователя <<<")
    phone = input(f"Введите номер телефона, по которому хотите произвести операцию\n"
                  f"Ввод(без +8): ")
    if phone:
        data._del_user(phone)

if __name__ == "__main__":
    main(PhoneBook())
