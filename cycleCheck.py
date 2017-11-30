from nose.tools import assert_equal


class Node:
    def __init__(self, data):
        self.data = data
        self.nextnode = None


def find_start_of_cycle(start, node_of_collision):
    slow = start
    fast = node_of_collision

    while slow != fast:
        slow = slow.nextnode
        fast = fast.nextnode
    print(slow.data)


def cycle_check(node):
    slow = node
    fast = node
    start = node

    while fast != None and fast.nextnode != None:
        slow = slow.nextnode
        fast = fast.nextnode.nextnode

        if slow == fast:
            find_start_of_cycle(start, fast)
            return True

    return False


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""

# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = b

#############

print(cycle_check(a))
