class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return "Stack is Empty"
        self.items.pop()

    def peek(self):
        if not self.items:
            return "Stack is Empty"
        return self.items[-1]

    def size(self):
        return len(self.items)