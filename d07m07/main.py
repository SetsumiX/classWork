# class FixedStack:
#     def __init__(self, size):
#         self.size = size
#         self.stack = []
#
#     def is_full(self):
#         return len(self.stack) == self.size
#
#     def is_empty(self):
#         return len(self.stack) == 0
#
#     def push(self, item):
#         if self.is_full():
#             print("Стек полон")
#             return False
#         else:
#             self.stack.append(item)
#             print(f"В стек добавлен элемент: {item}")
#             return True
#
#     def pop(self):
#         if self.is_empty():
#             print("Вытаскивать нечего")
#             return None
#         return self.stack.pop()
#
#     def count(self):
#         return len(self.stack)
#
#     def clear(self):
#         self.stack.clear()
#         print("Стек очищен")
#
#     def check_first_el(self):
#         if self.is_empty():
#             print("Проверять нечего")
#             return None
#         return self.stack[-1]
#
#     def display(self):
#         if self.is_empty():
#             print("Элементов нет")
#             return None
#         else:
#             print("Стек (верх -> низ): ", self.stack[::-1])
#
# a = FixedStack(5)
#
# a.push(1)
# a.display()
# a.push(3)
# a.push(4)
# a.push(5)
# a.push(2)
# a.display()
# a.push(6)
# a.pop()
# a.display()
# print(a.check_first_el())
# a.clear()
# print(a.is_empty())



# def create_node(value, next_node = None):
#     return {"value": value, "next": next_node}
#
# def t_list(head):
#     current = head
#     while current is not None:
#         print(current["value"], end = " -> ")
#         current = current["next"]
#     print("None")
#
# node3 = create_node(3)
# node2 = create_node(2, node3)
# node1 = create_node(1, node2)
#
# t_list(node1)



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, after_value, new_value):
        current = self.head
        while current:
            if current.value == after_value:
                new_node = Node(new_value)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Значение {after_value} не найдено")

    def clear(self):
        self.head = None

    def replace(self, old_value, new_value):
        current = self.head
        while current:
            if current.value == old_value:
                current.value = new_value
                return
            current = current.next
        print(f"Значение {old_value} не найдено")

    def contains(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def count(self):
        current = self.head
        temp = []
        while current:
            if current is not None:
                temp.append(current.value)
                current = current.next
        return len(temp)

    def delete(self, value):
        if not self.head:
            return

        if self.head.value == value:
            self.head = self.head.next

        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

b = LinkedList()
b.print_list()
b.append(1)
b.append(2)
b.print_list()
b.prepend(0)
b.print_list()
b.insert_after(1, 42)
b.print_list()
b.replace(42, 3)
b.print_list()
print(b.contains(3))
print(b.count())
b.delete(1)
print(b.count())