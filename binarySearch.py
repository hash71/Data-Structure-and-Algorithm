def binary_search(arr, elm):  # iterative
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = int((left + right) / 2)

        if elm == arr[mid]:
            return True

        if elm > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return False


def rec_bin_search(arr, elm):  # recursive
    if not arr:
        return False
    left = 0
    right = len(arr) - 1

    mid = int((left + right) / 2)

    if elm == arr[mid]:
        return True
    if elm < arr[mid]:
        return rec_bin_search(arr[:mid], elm)
    else:
        return rec_bin_search(arr[mid + 1:], elm)


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = []
# binary_search(arr, 4)
print(binary_search(arr, 2.2))
print(rec_bin_search(arr, 2.2))
