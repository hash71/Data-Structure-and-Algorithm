def selection_sort(arr):
    n = len(arr)
    for i in range(0, n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


x = [5, 4, 3, 2, 1]
selection_sort(x)
print(x)
