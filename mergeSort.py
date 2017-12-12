def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return
    mid = int(n / 2)
    left_list = arr[:mid]
    right_list = arr[mid:]
    merge_sort(left_list)
    merge_sort(right_list)

    i, j, k = 0, 0, 0

    while i < len(left_list) and j < len(right_list):

        if left_list[i] < right_list[j]:
            arr[k] = left_list[i]
            i += 1
        else:
            arr[k] = right_list[j]
            j += 1
        k += 1

    while i < len(left_list):
        arr[k] = left_list[i]
        i += 1
        k += 1

    while j < len(right_list):
        arr[k] = right_list[j]
        j += 1
        k += 1


x = [3, 2, 1, 5, 0]
merge_sort(x)
print(x)
