# import sys
#
# def func_for_python39():
#     return "Функция для PyCharm 3.9"
#
# def func_for_py312():
#     return "Функция для PyCharm 3.12"
#
# def default():
#     return "Функция для других версий PyCharm"
#
# vers_condition = {
#     (3, 12): func_for_py312,
#     (3, 9): func_for_python39,
# }
#
# version_info = sys.version_info[:2]
# print(version_info, sys.version_info)
#
# select_func = default
#
# for vers, func in vers_condition.items():
#     print(vers)
#     if version_info == vers:
#         select_func = func
#
# print(select_func())



# class Animal:
#     def make_sound(self):
#         print("Some sound animal")
#
# class Dog(Animal):
#     def make_sound(self): # Полиморфизм
#         print("Bark")
#
# class Cat(Animal):
#     def make_sound(self): # Полиморфизм
#         print("Meow")
#
# dog = Dog()
# cat = Cat()
#
# def animal_sound(animal):
#     animal.make_sound()
#
# animal_sound(dog)
# animal_sound(cat)



# class Cat:
#     def make_sound(self):
#         print("Meow")
#
# class Dog:
#     def make_sound(self):
#         print("Bark")
#
# class Cars:
#     def make_sound(self):
#         print("Wroom")
#
# def sound_maker(obj): # Метод утки
#     obj.make_sound()
#
# cat = Cat()
# dog = Dog()
# cars = Cars()
#
# sound_maker(cat)
# sound_maker(dog)
# sound_maker(cars)



# from abc import ABC, abstractmethod
# class SoundMaker(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass
#
# class Dog:
#     def make_sound(self):
#         print("Bark")
#
# class Cat:
#     def make_sound(self):
#         print("Meow")
#
# def sound_maker(obj):
#     if hasattr(obj, "make sound"):
#         obj.make_sound()
#     else:
#         raise TypeError("Object not supports function make_sound")
#
# sound_maker(Dog())
# sound_maker(Cat())



# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#     @abstractmethod # Не даёт распространяться функции, в других классах, или при создании этой функции без наследства
#     def make_sound(self):
#         pass
#     @abstractmethod # И при этом всём, если наследуется класс, функция становится обязательной для написания
#     def move(self):
#         pass
#
# class Dog(Animal):
#
#     def make_sound(self):
#         print("Bark")
#     def move(self):
#         print("Run")
#
# dog = Dog()
# dog.make_sound()



from abc import ABC, abstractmethod
from typing import List

class Character(ABC):
    def __init__(self, name, health): # _name, _health - инкапсуляция
        self._name = name
        self._health = health
        self._level = 1
        Character.total_characters += 1

    total_characters = 0 # Свойство класса

    # =+= Абстракция =+=
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) < 2:
            raise ValueError("Name is too short")
        self._name = value

    @property
    def health(self):
        return self._health

    # =+= Абстракция =+=
    @abstractmethod
    def attack(self):
        pass

    # =+= Полиморфизм =+=
    def take_damage(self, amount):
        self._health -= amount
        print(f"{self._name} получает {amount} ед. урона")

    # =+= Метод класса =+=
    @classmethod
    def get_total_characters(cls):
        return cls.total_characters

    #
    @staticmethod
    def validate_character(name):
        return len(name)

# =+= Наследование =+=

class Warrior(Character):
    def __init__(self, name, health, strength):
        super().__init__(name, health)
        self._strength = strength

    # =+= Полиморфизм =+=
    def attack(self):
        damage = self._strength * 1.5
        print(f"{self._name} нанёс мечём {damage} ед. урона.")
        return int(damage)

    # =+=  =+=
    def shield_block(self):
        print(f"{self._name} заблокировал урон щитом.")
        self._health += 5

class Mage(Character):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self._mana = mana
        self._spells = ["Fireball", "Frostbite", "Thunderbolt"]

    def attack(self):
        if self._mana < 10:
            print("Недостаточно маны.")
            return 0
        self._mana -= 10
        damage = 15 * (self._level * 2)
        print(f"{self._name} наносит {damage} ед. урона, способностью {self._spells[0]}.")
        return damage

    def restore_mana(self, amount):
        self._mana += amount
        print(f"{self._name} восстанавливает {amount} ед. маны.")

class BattleMage(Warrior, Mage):
    def __init__(self, name, health, strength, mana):
        Character.__init__(self, name, health)
        self._strength = strength
        self._mana = mana
        self._spalls = ["Fireball", "Frostbite", "Thunderbolt"]
        self._rage = 0

    def attack(self):
        if self._rage > 50:
            damage = Warrior.attack(self) + Mage.attack(self)
            self._rage = 0
            return damage
        return Warrior.attack(self)

    def empower(self):
        self._rage += 20
        print(f"{self._name} в ярости. Шкала ярости: {self._rage}")

if __name__ == "__main__":
    # Проверка валидации. Статический метод
    print("Валидация имени: ", Character.validate_character("А"))

    abobus_war = Warrior("Абобус", 120, 20)
    juja_mage = Mage("Жужа", 75, 180)
    dagonus_BM = BattleMage("Дагонус", 100, 10, 100)

    # Разные типы для разных интерфейсов
    characters: List[Character] = [abobus_war, juja_mage, dagonus_BM]

    for char in characters:
        print(f"\n{char.name} (Уровень: {char._level}):")
        char.attack()
        if isinstance(char, Mage):
            char.restore_mana(20)
        if isinstance(char, Warrior):
            char.shield_block()
        if isinstance(char, BattleMage):
            char.empower()

    print(f"\nВсего персонажей {Character.get_total_characters()}")