class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items)-1
        return self.items[last]

    def size(self):
        return len(self.items)

stack = Stack()
for c in "Позавчера":
    stack.push(c)

reverse = ""

for i in range(len(stack.items)):
    reverse += stack.pop()

list1 = [1, 2, 3, 4, 5]
list2 = []

stack1 = Stack()
for c in list1:
    stack1.push(c)

for i in range(len(stack1.items)):
    list2.append(stack1.pop())
    
print(reverse)
print(list2)
