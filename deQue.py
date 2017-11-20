class Deque:
    def __init__(self):
        self.elements = []

    def size(self):
        return len(self.elements)

    def is_empty(self):
        return self.elements == []

    def push_front(self, element):
        self.elements.append(element)

    def push_rear(self, element):
        self.elements.insert(0, element)

    def pop_front(self):
        if not self.elements:
            return "Deque is empty"
        self.elements.pop()

    def pop_rear(self):
        if not self.elements:
            return "Deque is empty"
        self.elements.pop(0)
