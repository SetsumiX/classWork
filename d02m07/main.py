# stack = [] # Стак
# for i in range(5):
#     stack.append(i * 2 + 1)
#
# print(stack)
# stack.pop()
# print(stack)

# from collections import deque
#
# queue = deque() # Куча
#
# queue.append(1)
# queue.append(2)
# queue.append(3)
#
# print(queue)
# print(queue.popleft())
# print(queue.popleft())
#
# print(queue)
#
# arr = []
# arr.append(1)
# arr.append(2)
# arr.append(3)
#
# print(arr.pop(0))

# import heapq
#
# prior = []
# heapq.heappush(prior, (3, "task high priority"))
# heapq.heappush(prior, (2, "task middle priority"))
# heapq.heappush(prior, (1, "task low priority"))
#
# while prior:
#     priority, task = heapq.heappop(prior)
#     print(f"Priority: {priority}, Task: {task}")
#
# class Task:
#     def __init__(self, name, priority):
#         self.name = name
#         self.priority = priority
#
#     def __lt__(self, other):
#         return self.priority < other.priority
#
# task0 = []
#
# heapq.heappush(task0, Task("Wash a cap", 2))
# heapq.heappush(task0, Task("To do project", 1))
# heapq.heappush(task0, Task("Watch a film", 3))
#
# while task0:
#     task1 = heapq.heappop(task0)
#     print(f"Priority {task1.priority}: {task1.name}")
#
# lst = [3, 1, 4, 1, 5, 9]
# heapq.heapify(lst)
# print(lst)
# # parent <= (2 * i + 1) also patent <= (2 * i + 1)
# # i - iterable element from list
#
# def heap_sort(iter_item):
#     h = []
#     for v in iter_item:
#         heapq.heappush(h, v)
#     return [heapq.heappop(h) for i in range(len(h))]
#
# print(heap_sort([5, 8, 4, 1, 2, 1, 5]))
#
# nums = [1, 8, 2, 23, 7, -4, 18, 23, 4, 42, 37, 2]
# print(heapq.nlargest(3, nums))
# print(heapq.nsmallest(3, nums))

# class CharQueue:
#     def __init__(self, size):
#         self.size = size
#         self.queue = []
#
#     def is_empty(self):
#         return len(self.queue) == 0
#
#     def is_full(self):
#         return len(self.queue) == self.size
#
#     def enqueue(self, item):
#         if self.is_full():
#             print("Очередь заполнена")
#             return False
#         self.queue.append(item)
#         return True
#
#     def dequeue(self):
#         if self.is_empty():
#             print("Очередь пуста")
#             return None
#         return self.queue.pop(0)
#
#     def show(self):
#         print(f"Очередь: ", " -> ".join(self.queue) if self.queue else "Пусто")
#
# def char_q_menu():
#     size = int(input("Введите размер очереди >>> "))
#     queue = CharQueue(size)
#
#     while True:
#         action = input(f"^^^Меню очереди^^^\n"
#                        f"1 - Проверить пуста ли очередь\n"
#                        f"2 - Проверка полна ли очередь\n"
#                        f"3 - Добавить символ в очередь\n"
#                        f"4 - Удалить символ из очереди\n"
#                        f"5 - Показать очередь\n"
#                        f"6 - Выход\n"
#                        f"Ответ: ")
#
#         if action == "1":
#             print("Очередь пуста" if queue.is_empty() else "Очередь не пуста")
#         elif action == "2":
#             print("Очередь полна" if queue.is_full() else "Очередь не полна")
#         elif action == "3":
#             char = input("Введите символ для ввода в очередь >>> ")
#             if len(char) == 1:
#                 queue.enqueue(char)
#             else:
#                 print("Ошибка, ожидался один символ")
#         elif action == "4":
#             item = queue.dequeue()
#             if item is not None:
#                 print(f"Удалён символ: {item}")
#         elif action == "5":
#             queue.show()
#         elif action == "6":
#             return False
#         else:
#             print("Нет таких функций, попробуйте ещё раз")
#
# char_q_menu()

class UserSystem:
    def __init__(self):
        self.users = {}

    def add_user(self, login, password):
        if login in self.users:
            print("Пользователь с таким логином уже занят")
            return False
        self.users[login] = password
        print(f"Пользоватьель {login} создан")
        return True

    def remove_user(self, login):
        if login not in self.users:
            print("Ввели ошибку, попробуйте заного")
            return False
        del self.users[login]
        return True

    def find(self, login):
        return login in self.users

    def change_login(self, login, change_on):
        if login not in self.users:
            print("Ввели ошибку, попробуйте заного")
            return False
        if change_on in self.users:
            print("Такой логин уже существует")
            return False
        password = self.users[login]
        del self.users[login]
        self.users[change_on] = password
        print(f"Логин: {login}, успешно изменён на {change_on}")
        return True

    def change_password(self, login, change_on):
        if login not in self.users:
            print("Ввели ошибку, попробуйте заного")
            return False
        self.users[login] = change_on
        print("Пароль успешно заменён")
        return True

    def show_users(self):
        if not self.users:
            print("Пользователей нет в базе данных")
        else:
            print("^^^^^ Пользователи ^^^^^")
            for login, password in self.users.items():
                print(f"Логин: {login}, Пароль: {'*' * len(password)}")

def text(a):
    return input(a)

def user_sys_menu():
    user_sys = UserSystem()

    while True:
        while True:
            action = input(f"^^^Меню пользователей^^^\n"
                           f"1 - Создать аккаунт\n"
                           f"2 - Удалить аккаунт\n"
                           f"3 - Найти аккаунт\n"
                           f"4 - Смена логина\n"
                           f"5 - Смена пароля\n"
                           f"6 - Выход\n"
                           f"Ответ: ")
            match action:
                case "1":
                    login = text("Введите логин >>> ")
                    password = text("Введите пароль >>> ")
                    user_sys.add_user(login, password)
                case "2":
                    login = text("Введите логин аккаунта для удаления >>> ")
                    user_sys.remove_user(login)
                case "3":
                    login = text("Введите логин для нахождения аккаунта >>> ")
                    print("Найден" if user_sys.find(login) else "Не найден")
                case "4":
                    login = text("Введите логин для смены логина аккаунта >>> ")
                    new_login = text("Введите новый логин для замены >>> ")
                    user_sys.change_login(login, new_login)
                case "5":
                    login = text("Введите логин для смены пароля аккаунта >>> ")
                    new_password = text("Введите пароль для замена >>> ")
                    user_sys.change_password(login, new_password)
                case "6":
                    user_sys.show_users()
                case "7":
                    break
                case _:
                    print("Нет такого")

user_sys_menu()