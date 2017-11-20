import sys


def tst(n):
    lst = []
    for i in range(n):
        print('length {} size {}'.format(len(lst), sys.getsizeof(lst)))
        lst.append(i)


tst(100)
