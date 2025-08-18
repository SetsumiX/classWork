class Book:
    def __init__(self):
        self.addresses = []

    def add_address(self, name, secName, thirName, city, phone, cityCode):
        num_id = len(self.addresses) + 1
        data = {
            "id": num_id,
            "имя": name,
            "фамилия": secName,
            "отчество": thirName,
            "город": city,
            "телефон": phone,
            "областной код": cityCode
        }
        self.addresses.append(data)

    def show_all(self):
        print(self.addresses)
        return self.addresses

    def find_address_name(self, name):
        for k, info in enumerate(self.addresses):
            if name.lower() in info["имя"].lower():
                print(f"id: {info['id']}\n"
                      f"Имя: {info['имя']}\n"
                      f"Фамилия: {info['фамилия']}\n"
                      f"Отчество: {info['отчество']}\n"
                      f"Город: {info['город']}\n"
                      f"Телефон: {info['телефон']}\n"
                      f"Областной код: {info['областной код']}\n")

    def find_address_secname(self, secname):
        ...

    def find_address_thirname(self, thirname):
        ...

    def find_address_city(self, city):
        ...

    def find_address_telephone(self, telephone):
        ...

    def find_address_citycode(self, citycode):
        ...

data = Book()

data.add_address("Vladislav", "Butkov", "Veniaminovich", "Volzhkiy", "9921489555", "34")
data.add_address("Иван", "Иванов", "Иванович", "Volzhkiy", "99229434553", "34")


data.show_all()

data.find_address_name("vla")
data.find_address_name("ив")

action = input(f"Выберите вариант взаимодействия с базой данных:\n"
               f"1 - ...\n"
               f"2 - ...\n"
               f"3 - ...\n"
               f">>> ")

match action:
    case "1":
        data.add_address(input())

    case "2":
        data.find_address_name(input())

    case "3":
        data.show_all()