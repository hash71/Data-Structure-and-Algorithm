class Queue:
    def __init__(self):
        self.elements = []

    def size(self):
        return len(self.elements)

    def is_empty(self):
        return self.elements == []

    def enqueue(self, item):
        self.elements.insert(0, item)

    def dequeue(self):
        if self.elements == []:
            return 'Queue is empty'
        return self.elements.pop()



