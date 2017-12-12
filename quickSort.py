def quick_sort(arr, begin, end):
    if begin < end:
        pivot = partition_array(arr, begin, end)
        quick_sort(arr, begin, pivot - 1)
        quick_sort(arr, pivot + 1, end)


def partition_array(arr, begin, end):
    pivot = begin
    left = begin
    right = end

    while True:
        while arr[pivot] <= arr[right] and pivot != right:
            right -= 1
        if right == pivot:
            break
        else:
            arr[pivot], arr[right] = arr[right], arr[pivot]
            pivot = right

        while arr[pivot] >= arr[left] and pivot != left:
            left += 1
        if left == pivot:
            break
        else:
            arr[pivot], arr[left] = arr[left], arr[pivot]
            pivot = left
    return pivot


x = [1, 2, 1]

quick_sort(x, 0, len(x) - 1)
print(x)
