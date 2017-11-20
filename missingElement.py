from nose.tools import assert_equal

import collections


def finder(a1, a2):
    result = 0

    for i in a1 + a2:
        result ^= i

    return result


def finder2(a1, a2):
    d = collections.defaultdict(int)

    for i in a2:
        d[i] += 1
    for i in a1:
        if d[i] == 0:
            return i
        else:
            d[i] -= 1


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""


class TestFinder:
    def test(self, sol):
        assert_equal(sol([5, 5, 7, 7], [5, 7, 7]), 5)
        assert_equal(sol([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]), 5)
        assert_equal(sol([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1]), 6)

        print('ALL TEST CASES PASSED')


# Run test
t = TestFinder()
t.test(finder)
t.test(finder2)
