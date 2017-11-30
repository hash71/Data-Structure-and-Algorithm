class Node:
    def __init__(self, data):
        self.value = data
        self.nextnode = None


def reverse(head):
    current = head

    prev = None

    while current:
        nxt = current.nextnode

        current.nextnode = prev
        prev = current
        current = nxt

    return prev


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d

reverse(a)
print(d.nextnode.value)
print(c.nextnode.value)
print(b.nextnode.value)
