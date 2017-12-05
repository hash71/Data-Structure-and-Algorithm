# for n elements there are n-1 pairs
# for 1st pass we check(whether to swap which takes O(1) time) n-1 pairs and get 1st largest element
# for 2nd pass we check(whether to swap which takes O(1) time) remaining n-2 pairs and get 2nd largest element
# for 3rd pass we check(whether to swap which takes O(1) time) remaining n-3 pairs and get 3rd largest element
#
# in this way we need to do 1 to n-1 total (n-1)n/2 pass [ O(n^2) ]
#
# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html


def bubble_sort(arr):
    last_unsorted = len(arr) - 1
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(last_unsorted):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
        last_unsorted -= 1


def bubble_sort1(arr):
    sorted_flag = False
    for i in range(1, len(arr)):
        if sorted_flag:
            break
        sorted_flag = True
        for j in range(len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sorted_flag = False


x = [4, 3, 2, 1]
bubble_sort1(x)
print(x)
