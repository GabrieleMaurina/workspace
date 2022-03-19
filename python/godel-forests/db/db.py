from os.path import getsize

BYTE_ORDER = 'big'

class DB:
    def __init__(self, name, block_size=1000, cache_size=10000000):
        self.name = name
        self.block_size = block_size
        self.cache_size = cache_size
        self.size = getsize(self.name) // self.block_size
        self.cache = [None] * self.cache_size
        open(self.name, 'a').close()
        with open(self.name, 'rb') as data:
            for i in range(min(self.cache_size, self.size)):
                self.cache[i] = int.from_bytes(data.read(self.block_size), BYTE_ORDER)

    def append(self, value):
        with open(self.name, 'ab') as data:
            data.write(value.to_bytes(self.block_size, BYTE_ORDER))
        if self.size < self.cache_size:
            self.cache[self.size] = value
        self.size += 1

    def get(self, key=None):
        if key is None:
            key = self.size-1
        if key < self.cache_size:
            return self.cache[key]
        else:
            with open(self.name, 'rb') as data:
                data.seek(key * self.block_size)
                return int.from_bytes(data.read(self.block_size), BYTE_ORDER)
