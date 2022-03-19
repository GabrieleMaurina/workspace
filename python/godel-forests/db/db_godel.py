from sympy.ntheory import factorint
from sympy.utilities.iterables import multiset_partitions
from itertools import count
from math import prod
from db import DB

def multpart(k):
    return tuple(mp for mp in tuple(tuple(prod(prime) for prime in partition) for partition in multiset_partitions(factorint(k, multiple=True))) if k not in mp)

def main():
    f = DB('fine.db')
    while f.size < 2:
        f.append(1)
    for k in count(start=f.size):
        f.append(f.get(k-1) + sum(prod(map(lambda v:f.get(v-1), mp)) for mp in multpart(k)))

if __name__ == '__main__':
    main()
