stack = []
def push(a):
    stack.append(a)

def pop():
    val = stack[-1]
    del stack[-1]
    return val

def pr():
    print(stack)

push(1)
push(2)
push(3)
pr()
pop()
pr()
pop()
pr()

class Stack:
    def __init__(self):
        print(f"Инициализация...\n"
              f"Готово")
        self.__stack_List = []
    def push(self, val):
        self.__stack_List.append(val)
    def pop(self):
        val = self.__stack_List[-1]
        del self.__stack_List[-1]
        return val
    def print(self):
        print(self.__stack_List)

p = Stack()

# print(p.__dict__)
# print(p.__dir__())

p.push(3)
for i in range(3): p.push(i + 1)

p1 = Stack()
p1.push(3)

p.print()
p1.print()