from nose.tools import assert_equal


def algo1(str1='str1', str2='str2'):
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()
    return sorted(str1) == sorted(str2)


def algo2(str1='str1', str2='str2'):
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()

    if len(str1) != len(str2):
        return False

    dict = {}

    for i in str1:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    for i in str2:
        if i in dict:
            dict[i] -= 1
        else:
            return False

    for i in dict:
        if dict[i] != 0:
            return False

    return True


""" 
RUN THIS CELL TO TEST YOUR SOLUTION 
"""


class AnagramTest:
    def test(self, sol):
        assert_equal(sol('go go go', 'gggooo'), True)
        assert_equal(sol('abc', 'cba'), True)
        assert_equal(sol('hi man', 'hi     man'), True)
        assert_equal(sol('aabbcc', 'aabbc'), False)
        assert_equal(sol('123', '1 2'), False)
        print("ALL TEST CASES PASSED")


# Run Tests
t = AnagramTest()
t.test(algo1)
t.test(algo2)
