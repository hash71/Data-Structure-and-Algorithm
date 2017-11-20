import ctypes


class DynamicArray:
    def __init__(self):
        self.n = 0
        self.capacity = 1  # default capacity 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, k):
        if not 0 <= k < self.n:
            return IndexError('out of bound error')
        return self.A[k]

    def append(self, elm):
        if self.n == self.capacity:
            self.capacity *= 2
            B = self.make_array(self.capacity)

            for i in range(self.n):
                B[i] = self.A[i]
            self.A = B

        self.A[self.n] = elm
        self.n += 1

    def make_array(self, capacity):  # returns raw array of given capacity
        return (capacity * ctypes.py_object)()


a = DynamicArray()

a.append(1)
a.append(2)
a.append(3)

print(a[6])
print(a[0])
