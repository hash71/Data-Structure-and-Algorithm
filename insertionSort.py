def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        elm = arr[i]
        marker = i

        while marker and arr[marker - 1] > elm:
            arr[marker] = arr[marker - 1]
            marker -= 1
        arr[marker] = elm


x = [3, 2, 1, 5]
insertion_sort(x)
print(x)
