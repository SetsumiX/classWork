class Book:
    def __init__(self):
        self.addresses = []

    def add_address(self, name, secName, city, phone, cityCode, thirName=None):
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
        for k, info in enumerate(self.addresses):
            if secname.lower() in info["фамилия"].lower():
                print(f"id: {info['id']}\n"
                      f"Имя: {info['имя']}\n"
                      f"Фамилия: {info['фамилия']}\n"
                      f"Отчество: {info['отчество']}\n"
                      f"Город: {info['город']}\n"
                      f"Телефон: {info['телефон']}\n"
                      f"Областной код: {info['областной код']}\n")

    def find_address_thirname(self, thirname):
        for k, info in enumerate(self.addresses):
            if thirname.lower() in info["отчество"].lower():
                print(f"id: {info['id']}\n"
                      f"Имя: {info['имя']}\n"
                      f"Фамилия: {info['фамилия']}\n"
                      f"Отчество: {info['отчество']}\n"
                      f"Город: {info['город']}\n"
                      f"Телефон: {info['телефон']}\n"
                      f"Областной код: {info['областной код']}\n")

    def find_address_city(self, city):
        for k, info in enumerate(self.addresses):
            if city.lower() in info["город"].lower():
                print(f"id: {info['id']}\n"
                      f"Имя: {info['имя']}\n"
                      f"Фамилия: {info['фамилия']}\n"
                      f"Отчество: {info['отчество']}\n"
                      f"Город: {info['город']}\n"
                      f"Телефон: {info['телефон']}\n"
                      f"Областной код: {info['областной код']}\n")

    def find_address_telephone(self, telephone):
        for k, info in enumerate(self.addresses):
            if telephone.lower() in info["телефон"].lower():
                print(f"id: {info['id']}\n"
                      f"Имя: {info['имя']}\n"
                      f"Фамилия: {info['фамилия']}\n"
                      f"Отчество: {info['отчество']}\n"
                      f"Город: {info['город']}\n"
                      f"Телефон: {info['телефон']}\n"
                      f"Областной код: {info['областной код']}\n")

    def find_address_citycode(self, citycode):
        for k, info in enumerate(self.addresses):
            if citycode.lower() in info["областной код"].lower():
                print(f"id: {info['id']}\n"
                      f"Имя: {info['имя']}\n"
                      f"Фамилия: {info['фамилия']}\n"
                      f"Отчество: {info['отчество']}\n"
                      f"Город: {info['город']}\n"
                      f"Телефон: {info['телефон']}\n"
                      f"Областной код: {info['областной код']}\n")

data = Book()

while True:
    action_1 = input(f"Выберите вариант взаимодействия с базой данных:\n"
                   f"1 - Добавить контакт\n"
                   f"2 - Показать всех\n"
                   f"3 - Найти контакт\n"
                   f">>> ")

    match action_1:
        case "1":
            data.add_address(input("Имя: "),
                             input("Фамилия: "),
                             input("Отчество (Если есть): "),
                             input("Город: "),
                             input("Номер телефона: "),
                             input("Код области: "))

        case "2":
            data.show_all()

        case "3":
            while True:
                action_2 = input(f"Найти контакт по:\n"
                                 f"1 - Имени\n"
                                 f"2 - Фамилии\n"
                                 f"3 - Отчеству\n"
                                 f"4 - Городу\n"
                                 f"5 - Телефону\n"
                                 f"6 - Области\n"
                                 f">>> ")
                match action_2:
                    case "1":
                        data.find_address_name(input(">>> "))
                        break
                    case "2":
                        data.find_address_secname(input(">>> "))
                        break
                    case "3":
                        data.find_address_thirname(input(">>> "))
                        break
                    case "4":
                        data.find_address_city(input(">>> "))
                        break
                    case "5":
                        data.find_address_telephone(input(">>> "))
                        break
                    case "6":
                        data.find_address_citycode(input(">>> "))
                        break
                    case _:
                        print("Попробуйте ещё раз")

        case _:
            print("Попробуйте ещё раз")