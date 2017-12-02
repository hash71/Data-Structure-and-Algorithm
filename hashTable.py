class Hashtable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * size
        self.data = [None] * size

    def hashfunction(self, key):
        return key % self.size

    def rehash(self, oldhash):
        return (oldhash + 1) % self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key)  # hashvalues are indexes like 0,1,2 for two list slot & data

        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        elif self.slots[hashvalue] == key:
            self.data[hashvalue] = data
        else:
            nextslot = self.rehash(hashvalue)  # simple the next slot

            while self.slots[nextslot] != None or self.slots[nextslot] != key:
                nextslot = self.rehash(nextslot)

            if self.slots[nextslot] == None:
                self.slots[nextslot] = key
                self.data[nextslot] = data
            else:
                self.data[nextslot] = data

    def get(self, key):
        startslot = self.hashfunction(key)
        position = startslot
        found = False
        stop = False
        data = None

        while self.slots[position] != None and not found and not stop:

            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(key)

                if position == startslot:
                    stop = True

        return data

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        self.put(key, value)


h = Hashtable(5)
h[1] = 'one'
h[2] = 'two'
h[3] = 'three'
x = h[1]
print(h.get(1))
h[1] = 'new_one'
print(h[1])
print(h[4])
