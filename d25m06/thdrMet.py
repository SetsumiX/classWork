class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} goda"

    def __repr__(self):
        return f"{self.name}, {self.age}"

p = Person("Аня", 300)
print(p)
print(repr(p))

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__init__(cls)
        return cls._instance

a = Singleton()
b = Singleton()
print(a is b)

class TempFile:
    def __init__(self, filename):
        self.filename = filename

    def __del__(self):
        import os
        if os.path.exists(self.filename):
            os.remove(self.filename)

t = TempFile("err.txt")
del t

class Book:
    def __init__(self, title, author, amount):
        self.title = title
        self.author = author
        self.amount = amount

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.amount < other.amount

    def __le__(self, other):
        return self.amount <= other.amount

    def __gt__(self, other):
        return self.amount > other.amount

    def __ge__(self, other):
        return self.amount >= other.amount

b1 = Book("1984", "Oliver", 300)
b2 = Book("1984", "Oliver", 250)
print(b1 == b2) # Простая проверка равенства(функции __eq__) без его написания
print(b1 != b2) # Простая проверка неравенства(функции __ne__) без его написания

# __lt__, __gt__, __le__, __ge__ - равенства(меньше чем, больше чем, меньше или равно, больше или равно)
print(b1 < b2)
print(b1 > b2)

class Vector:
    def __init__(self, x, y, items):
        self.x = x
        self.y = y
        self.items = items

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Vector(self.x / other.x, self.y / other.y)

    def __abs__(self):
        return abs(self.x)

    def __len__(self):
        return len(self.items)

v1 = Vector(2, 4, [])
v2 = Vector(1, 3, [2, 3])
v3 = v1 + v2
print(v3.x, v3.y)
