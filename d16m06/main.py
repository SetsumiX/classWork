# class Example:
#     __money = 0
#     def __init__(self, name):
#         self.name = name
#         self.age = 18
#
#     def pp(self):
#         return self.name
#
#     def set_age(self, value):
#         self.age = value
#
#     def get_age(self):
#         return self.age
#     @staticmethod
#
#     def get_money():
#         return Example.__money
#
# p = Example("Nik")
#
# print(p.pp(), Example.get_money())
#
# print(p.get_age())
# p.set_age(22)
# print(p.get_age())

# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance
#     @property
#     def balance(self):
#         return self.__balance
#
#     @balance.setter
#     def balance(self, value):
#         if value >= 0:
#             self.__balance = value
#         else:
#             raise ValueError("!Баланс не может быть отрицательным!")
#
# account = BankAccount(100)
# print(account.balance) # Getter, так как смотрим баланс
#
# account.balance = 200 # Setter, так как меняем значение
# print(account.balance)

# class ShipStages:
#     fuel_type = "жидкое топливо"
#
#     @staticmethod
#     def check_fuel(cls_fuel, extra_date):
#         print(f"Вид топлива: {cls_fuel}\n"
#               f"Доп. данные: {extra_date}")
#
# ShipStages.check_fuel(ShipStages.fuel_type, "Проверка топлива")

# class ShipStages:
#     def __init__(self, name_stage_1):
#         self.name_stage_1 = name_stage_1
#
#     @staticmethod
#     def print_name(instance):
#         print(f"Вид топлива: {instance.name}") # Не понял как это должно работать
#
# stage1 = ShipStages("Взлётная")
# ShipStages.print_name(stage)

# class BankAccount:
#     currency = "USD"
#
#     def __init__(self, balance):
#         self.balance = balance
#
#     @staticmethod
#     def transfer(cls_currency, account_from, account_to, amount):
#         print(f"Валюта: {cls_currency}")
#         print(f"Перевод: {amount} {cls_currency}")
#         account_from.balance -= amount
#         account_to.balance += amount
#
# account1 = BankAccount(1000)
# account2 = BankAccount(2000)
#
# BankAccount.transfer(BankAccount.currency, account2, account1, 365)
# print(account1.balance)
# print(account2.balance)

# class ShipStage:
#     total_rockets = 0
#
#     def __init__(self, name):
#         self.name = name
#         ShipStage.total_rockets += 1
#
#     @staticmethod
#
#     def get_total(cls):
#         return cls.total_rockets
#
# stage = ShipStage("Взлёт")
# print(ShipStage.get_total(ShipStage))

