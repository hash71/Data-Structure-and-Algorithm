def shell_sort(arr):
    n = len(arr)
    sublist_count = int(n / 2)

    # number of sublist == gap
    while sublist_count:

        for i in range(sublist_count):  # for each sublist
            insertion_sort(arr, i, sublist_count)
        sublist_count = int(sublist_count / 2)


def insertion_sort(arr, start, gap):
    for i in range(start + gap, len(arr), gap):
        position = i
        value = arr[position]

        while position >= gap and arr[position - gap] > value:
            arr[position] = arr[position - gap]
            position = position - gap
        arr[position] = value


x = [5, 4, 3, 2, 1, 77, 9, 8]
shell_sort(x)
print(x)
