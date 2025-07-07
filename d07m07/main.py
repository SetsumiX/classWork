class FixedStack:
    def __init__(self, size):
        self.size = size
        self.stack = []

    def is_full(self):
        return len(self.stack) == self.size

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        if self.is_full():
            print("Стек полон")
            return False
        else:
            self.stack.append(item)
            print(f"В стек добавлен элемент: {item}")
            return True

    def pop(self):
        if self.is_empty():
            print("Вытаскивать нечего")
            return None
        return self.stack.pop()

    def count(self):
        return len(self.stack)

    def clear(self):
        self.stack.clear()
        print("Стек очищен")

    def check_first_el(self):
        if self.is_empty():
            print("Проверять нечего")
            return None
        return self.stack[-1]

    def display(self):
        if self.is_empty():
            print("Элементов нет")
            return None
        else:
            print("Стек (верх -> низ): ", self.stack[::-1])

a = FixedStack(5)

a.push(1)
a.display()
a.push(3)
a.push(4)
a.push(5)
a.push(2)
a.display()
a.push(6)
a.pop()
a.display()
print(a.check_first_el())
a.clear()
print(a.is_empty())

