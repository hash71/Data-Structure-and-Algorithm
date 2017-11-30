from nose.tools import assert_equal


class Node:
    def __init__(self, value):
        self.value = value
        self.nextnode = None


def nth_to_last_node(n, head):
    left_pointer = head
    right_pointer = head
    for i in range(n):
        if not right_pointer.nextnode:
            raise LookupError('Error: n is larger than the linked list.')
        right_pointer = right_pointer.nextnode

    while right_pointer:
        right_pointer = right_pointer.nextnode
        left_pointer = left_pointer.nextnode

    return left_pointer


"""
RUN THIS CELL TO TEST YOUR SOLUTION AGAINST A TEST CASE

PLEASE NOTE THIS IS JUST ONE CASE
"""

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e


####

class TestNLast(object):
    def test(self, sol):
        assert_equal(sol(2, a), d)
        print('ALL TEST CASES PASSED')


# Run tests
t = TestNLast()
t.test(nth_to_last_node)
