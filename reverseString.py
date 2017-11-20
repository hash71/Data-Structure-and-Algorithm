from nose.tools import assert_equal


def reverse_string(s):
    delimiters = [' ']
    word_array = []
    single_word = ''

    for i in s:
        if i not in delimiters:
            single_word += i
        else:
            if len(single_word):
                word_array.append(single_word)
            single_word = ''
    if len(single_word):
        word_array.append(single_word)

    result = word_array[-1]
    for i in range(2, len(word_array) + 1):
        result += ' ' + word_array[-i]
    return result


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""


class ReversalTest(object):
    def test(self, sol):
        assert_equal(sol('    space before'), 'before space')
        assert_equal(sol('space after     '), 'after space')
        assert_equal(sol('   Hello John    how are you   '), 'you are how John Hello')
        assert_equal(sol('1'), '1')
        print("ALL TEST CASES PASSED")


# Run and test
t = ReversalTest()
t.test(reverse_string)
