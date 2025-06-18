# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print(f"{self.name} издаёт звук")
#
# class Dog(Animal):
#     def bark(self):
#         print(f"{self.name} лает. Тяу тяу тяу")
#
# myDog = Dog("Жижик")
# myDog.speak()
# myDog.bark()
#
# class Cat(Animal):
#     def speak(self):
#         print(f"{self.name} мяукает. Мяу мяу")
#
# myCat = Cat("Греча")
# myCat.speak()
#
# class Bird(Animal):
#     def __init__(self, name, can_fly):
#         super().__init__(name)
#         self.can_fly = can_fly
#     def speak(self):
#         super().speak()
#         print(f"{self.name} чирикает. Чирик чирик")
#
# myBird = Bird("Козёл", True)
# print(myBird.can_fly)
# myBird.speak()



# class A:
#     def method(self):
#         print("+++A+++")
#
# class B:
#     pass
#     # def method(self):
#     #     print("+++B+++")
#
# class C(B, A):
#     pass
#
# c = C()
# c.method()
# print(C.__mro__) # Порядок чтения классов



class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        print(f"{self.name} атакует")

class Warrior(Character):
    def __init__(self, name, health, stranght):
        super().__init__(name, health)
        self.stranght = stranght

    def attack(self):
        super().attack()
        print(f"Сила удара {self.stranght}")

class Mage(Character):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.mana = mana

    def cast_spell(self):
        print(f"{self.name}: Чтение заклинания (Затрата маны: {self.mana})")

warrior = Warrior("Ярик", 100, 50)
mage = Mage("Адриана", 50, 200)

warrior.attack()
mage.cast_spell()
