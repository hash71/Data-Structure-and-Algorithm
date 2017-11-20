from nose.tools import assert_equal


def compress(s):
    l = len(s)
    result = ''
    if l == 0:
        return ''
    if l == 1:
        return s + '1'

    cnt = 1
    i = 1

    while i < l:
        if s[i] == s[i - 1]:
            cnt += 1
        else:
            result += s[i - 1] + str(cnt)
            cnt = 1
        i += 1

    result += s[i - 1] + str(cnt)
    return result


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""


class TestCompress(object):
    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print('ALL TEST CASES PASSED')

    # Run Tests


t = TestCompress()
t.test(compress)
