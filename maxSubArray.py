from nose.tools import assert_equal


def max_sub_array(arr):
    max_till_previous_index = max_so_far = arr[0]
    start_index_arr = [0]
    end_index = 0

    for current_index in range(1, len(arr)):

        max_including_current_index = max_till_previous_index + arr[current_index]

        if max_including_current_index > arr[current_index]:
            max_till_previous_index = max_including_current_index
        else:
            max_till_previous_index = arr[current_index]
            start_index_arr.append(current_index)

        if max_till_previous_index > max_so_far:
            max_so_far = max_till_previous_index
            end_index = current_index
            start_index = start_index_arr[-1]

    print('start {} end {} max {}'.format(start_index, end_index, max_so_far))
    return max_so_far


class LargeContTest(object):
    def test(self, sol):
        assert_equal(sol([1, 2, -1, 3, 4, -1]), 9)
        assert_equal(sol([1, 2, -1, 3, 4, 10, 10, -10, -1]), 29)
        assert_equal(sol([-1, 1]), 1)
        print('ALL TEST CASES PASSED')


# Run Test
t = LargeContTest()
t.test(max_sub_array)
