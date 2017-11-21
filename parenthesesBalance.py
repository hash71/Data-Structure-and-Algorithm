from nose.tools import assert_equal


def balance_check(s):
    if len(s) % 2 == 1:  # check if len is even or odd
        return False
    if not s:  # check if empty
        return False

    opening = '({['
    matches = [('(', ')'), ('[', ']'), ('{', '}')]
    stack = []

    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:  # if the first one is a closing bracket then stack is empty
                return False
            last_paren = stack.pop()
            if (last_paren, paren) not in matches:
                return False

    return len(stack) == 0


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""


class TestBalanceCheck(object):
    def test(self, sol):
        assert_equal(sol('[](){([[[]]])}('), False)
        assert_equal(sol('[{{{(())}}}]((()))'), True)
        assert_equal(sol('[[[]])]'), False)
        print('ALL TEST CASES PASSED')


# Run Tests

t = TestBalanceCheck()
t.test(balance_check)
