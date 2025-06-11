# stack = []
# def push(a):
#     stack.append(a)
#
# def pop():
#     val = stack[-1]
#     del stack[-1]
#     return val
#
# def pr():
#     print(stack)
#
# push(1)
# push(2)
# push(3)
# pr()
# pop()
# pr()
# pop()
# pr()

# class Stack:
#     def __init__(self):
#         print(f"Инициализация...\n"
#               f"Готово")
#         self.__stack_List = []
#     def push(self, val):
#         self.__stack_List.append(val)
#     def pop(self):
#         val = self.__stack_List[-1]
#         del self.__stack_List[-1]
#         return val
#     def print(self):
#         print(self.__stack_List)
#
# p = Stack()

# print(p.__dict__)
# print(p.__dir__())

# p.push(3)
# for i in range(3): p.push(i + 1)
#
# p1 = Stack()
# p1.push(3)
#
# p.print()
# p1.print()

# class Mth(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__sum = 0
#     def getSum(self):
#         return self.__sum
#     def push(self, val):
#         self.__sum += val
#         Stack.push(self, val)
#     def pop(self):
#         val = Stack.pop(self)
#         self.__sum -= val
#         return val
#     def print(self):
#         return Stack.print(self)
#
# d = Mth()

# for i in range(5):
#     d.push(i + 1)
# print(d.getSum())
# d.print()

# user_name = "Alice"
# user_age = 25
#
# def greeting(a, b):
#     print(f"Hello {a}, we know you {b} years old")
#
# greeting(user_name, user_age)

# class UserFunc:
#     def __init__(self, name, yo):
#         self.name = name
#         self.yo = yo
#
#     def greeting(self):
#         print(f"Hello {self.name}, we know you {self.yo} years old")
#
# alice = UserFunc("Alice", 25)
# bob = UserFunc("Bob", 22)
#
# alice.greeting()
# bob.greeting()
#
# '''В функции для того, чтоб узнать значение по типу name = введёное имя, нужно писать для вывода(return) - "name": "Введёное имя"
# А в классе, можно импользовать Название класса.name'''

# def create_car(brand, model):
#     return {"brand": brand, "model": model}
#
# def create_electric_car(brand, model, battery):
#     car = create_car(brand, model)
#     car["battery"] = battery
#     return car
#
# print(create_electric_car("Tesla", "Plate", 4000))

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
# class ElCar(Car):
#     def __init__(self, brand, model, battery):
#         super().__init__(brand, model)
#         self.battery = battery
#     def print(self):
#         print(f"Марка: {self.brand}, модель: {self.model}, размер батареи: {self.battery}")
#
# tesla_car = ElCar("Tesla", "Modul 3",4000)
#
# tesla_car.print()

# class Animal:
#     def make_sound(self):
#         pass
#
# class Dog(Animal):
#     def make_sound(self):
#         print("Гав")
#
# class Cat(Animal):
#     def make_sound(self):
#         print("Мяу")
#
# def animal_sound(animal: Animal):
#     animal.make_sound()
#
# dog = Dog()
# cat = Cat()
#
# animal_sound(dog)
# animal_sound(cat)

# class Order:
#     def __init__(self, customer, product):
#         self.customer = customer
#         self.product = product
#     def total_price(self):
#         return sum(product.price for product in self.product)
#
# class Products:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# banana = Products("Banana", 1)
# apple = Products("Apple", 0.3)
#
# alice_order = Order("Alice", [banana, apple])
# print(f"All stuff cost: {alice_order.total_price()}$")

class StageShip:
    fuel_type = "Твёрдое топливо"
    def __init__(self, name):
        self.name = name

StageOne = StageShip("Двигатель разгона")
StageTwo = StageShip("Двигатели стабилизации скорости для поддержания орбиты")

print(StageOne.name)
print(StageTwo.name)
print(StageOne.fuel_type)
print(StageTwo.fuel_type)

StageTwo.fuel_type = "Жидкое топливо"
print(StageOne.fuel_type)
print(StageTwo.fuel_type)