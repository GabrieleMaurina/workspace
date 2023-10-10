from os.path import getsize, isfile

class Godel:
    def __init__(self):
        self.data_file = 'godel.data'
        self.index_file = 'godel.index'
        self.index_size = 6
        self.cache = [None] * self.cache_size
        self.cache_size = 1000
        self.last = None
        self.last_index_size = None
        self.size = 0
        self.load_data()
    
    def load_data(self):
        if not isfile(self.data_file) or not isfile(self.index_file):
            with open(self.data_file, 'w'): pass
            with open(self.index_file, 'w'): pass
        with open(self.index_file, 'rb') as idx:
            for i in range(self.cache_size):
                p = idx.read(self.index_size)
                self.cache[i] = 
    
    def append(self, v):
        if self.size < self.cache_size - 1:
            self.cache[self.size] = v
        
        index_bytes = self.last_index_size.to_bytes(self.index_size, 'big', signed=False)
        with open(self.index_file, 'ab') as idx:
            idx.write(index_bytes)
        value_bytes = v.to_bytes('big', signed=False)
        with open(self.data_file, 'ab') as data:
            data.write(value_bytes)
        
        self.last_index_size += len(value_bytes)
        self.size += 1
        self.last = v
    
    def get(self, k):
        if self > 0:
            if k < self.size:
                if k < self.cache_size:
                    return self.cache[k]
                elif k == self.size - 1:
                    return self.last
                else:
                    with open(self.index_file, 'rb') as idx:
                        idx.seek(self.index_size*k)
                        start = int.from_bytes(idx.read(self.index_size), 'big', signed=False)
                        end = int.from_bytes(idx.read(self.index_size), 'big', signed=False)
                    with open(self.data_file, 'rb') as data:
                        data.seek(start)
                        return int.from_bytes(data.read(end - start), 'big', signed=False)
            else:
                raise ValueError('K not computed yet.')
        else:
            raise ValueError('K cannot be negative.')

    def get_last(self):
        return self.last