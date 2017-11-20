from nose.tools import assert_equal


def pair_sum(arr, n):
    seen = set()
    output = set()

    for i in arr:
        target = n - i

        if target in seen:
            output.add((min(i, target), max(i, target)))
        else:
            seen.add(i)

    return len(output)


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""


class TestPair:
    def test(self, sol):
        assert_equal(sol([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10), 6)
        assert_equal(sol([1, 2, 3, 1], 3), 1)
        assert_equal(sol([1, 3, 2, 2], 4), 2)
        print('ALL TEST CASES PASSED')


# Run tests
t = TestPair()
t.test(pair_sum)
