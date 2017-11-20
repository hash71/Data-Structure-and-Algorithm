import timeit


def sum1(n):
    total = n
    for i in range(n):
        total += i
    return total


print(sum1(10))

print(timeit.timeit('sum1(10)', 'from __main__ import sum1', number=3))
