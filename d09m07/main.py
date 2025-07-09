# def create_node(value, next_node=None):
#     return {"value": value, "next": next_node}
#
# def append(head, value):
#     new_node = create_node(value)
#     if not head:
#         return new_node
#     current = head
#     while current["next"]:
#         current = current["next"]
#
#     current["next"] = new_node
#     return head
#
# def check_list(head):
#     current = head
#     while current:
#         print(current["value"], end=" -> ")
#         current = current["next"]
#     print("None")
#
# def prepend(head, value):
#     return create_node(value, head)
#
# def insert_after(head, older_value, new_value):
#     current = head
#     while current:
#         if current["value"] == older_value:
#             new_node = create_node(new_value, current["next"])
#             current["next"] = new_node
#             return head
#         current = current["next"]
#     print(f"{older_value} не найден")
#     return head
#
# def clear(head):
#     return None
#
# def replace(head, old_value, new_value):
#     current = head
#     while current:
#         if current["value"] == old_value:
#             current["value"] = new_value
#             return head
#         current = current["next"]
#         print(f"{old_value} не найден")
#
# def contains(head, value):
#     current = head
#     while current:
#         if current["value"] == value:
#             return True
#         current = current["next"]
#     print(f"{value} не найдено")
#     return False
#
#
# head = append(None, 12)
# head = append(head, 3)
# head = append(head, 1)
# check_list(head)
# head = prepend(head, 0)
# head = insert_after(head, 0, 42)
# head = replace(head, 42, 5)
# print(contains(head, 3))
# check_list(head)
# head = clear(head)
# check_list(head)
import json
import time


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#         self.prev = None
#
# class DoubleLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def is_empty(self):
#         return self.head is None
#
#     def append(self, value):
#         new_node = Node(value)
#         if self.is_empty():
#             self.head = self.tail = new_node
#         else:
#             new_node.prev = self.tail
#             self.tail.next = new_node
#             self.tail = new_node
#
#     def check_list(self):
#         current = self.head
#         while current:
#             print(current.value, end=" <--> ")
#             current = current.next
#         print("None")
#
#     def rev_check_list(self):
#         current = self.tail
#         while current:
#             print(current.value, end=" <--> ")
#             current = current.prev
#         print("None")
#
#     def remove(self, value):
#         if self.is_empty():
#             return False
#         current = self.head
#         while current:
#             if current.value == value:
#                 if current.prev:
#                     current.prev.next = current.next
#                 else:
#                     self.head = current.next
#                 if current.next:
#                     current.next.prev = current.prev
#                 else:
#                     self.tail = current.prev
#                 return True
#             current = current.next
#         return False
#
#     def contains(self, value):
#         current = self.head
#         while current:
#             if current.value == value:
#                 return True
#             current = current.next
#         return False
#
#     def replace(self, old_value, new_value):
#         current = self.head
#         while current:
#             if current.value == old_value:
#                 current.value = new_value
#                 return True
#             current = current.next
#         return False
#
# dll = DoubleLinkedList()
#
# for i in range(10):
#     dll.append((i+1)*10)
#
# dll.check_list()



# d = {}
#
# keys = ["имя", "возраст", "хобби", "пол", "страна"]
# for key in keys:
#     d[key] = input(f"Введите {key} >>> ")
#
# print(d)

# import pickle, json
# class Airplane:
#     def __init__(self, model, capacity, max_speed, current_fuel):
#         self.model = model
#         self.capacity = capacity
#         self.max_speed = max_speed
#         self.current_fuel = current_fuel
#
#     def __str__(self):
#         return f"Модель самолёта: {self.model}\nИмеет мест: {self.capacity}\nМаксимальная скорость: {self.max_speed}\nТекущее топливо: {self.current_fuel}"
#
#     def pack(self, filename):
#         with open(filename, "wb") as file:
#             pickle.dump(self, file)
#
#     @classmethod
#     def unpack(cls, filename):
#         with open(filename, "rb") as file:
#             return pickle.load(file)
#
#     def pack_json(self, filename):
#         with open(filename, "w") as file:
#             json.dump(self.__dict__, file)
#
#     @classmethod
#     def unpack_json(cls, filename):
#         with open(filename, "r") as file:
#             data = json.load(file)
#             airplane = cls.__new__(cls)
#             airplane.__dict__.update(data)
#             return airplane
#
# ar = Airplane("як", 1, 1700, 350)
# print(ar)
#
# ar.pack("my_yak.txt")
# p = ar.unpack("my_yak.txt")
# print(p)
#
# ar.pack_json("my_yak.json")
# j = ar.unpack_json("my_yak.json")
# print(j)



import pickle, json
class Clock:
    def __init__(self, hours, minutes, seconds):
        if not (0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59):
            raise ValueError("Введено странное время")
        self.hours = hours
        self.minuets = minutes
        self.seconds = seconds

    def __str__(self):
        return f"Час/Минуты/Секунды: {self.hours:02d}/{self.minuets:02d}/{self.seconds:02d}"

    def tick(self):
        self.seconds += 1
        if self.seconds >= 60:
            self.seconds = 0
            self.minuets += 1
        if self.minuets >= 60:
            self.minuets = 0
            self.hours += 1
        if self.hours >= 24:
            self.hours = 0

    def pack_pickle(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    def pack_json(self, filename):
        with open(filename, "w") as file:
            data = {
                "hours": self.hours,
                "minutes": self.minuets,
                "seconds": self.seconds
            }
            json.dump(data, file)

    @classmethod
    def unpack_pickle(cls, filename):
        with open(filename, "r") as file:
            data = ...

    def unpack_json(self, filename):
        with open(filename, "r") as file:
            data = json.load(file)
            self.hours = data["hours"]
            self.minuets = data["minutes"]
            self.seconds = data["seconds"]


time_cur = Clock(13, 58, 58)

time_cur.pack_pickle("errortime.txt")
time_cur.pack_json("errortime.json")

for i in range(120):
    # time.sleep(1)
    time_cur.tick()

print(time_cur)
time_cur.unpack_json("errortime.json")
print(time_cur)