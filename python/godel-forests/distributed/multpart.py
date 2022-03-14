from sys import argv
from sympy.ntheory import factorint
from sympy.utilities.iterables import multiset_partitions
from multiprocessing import Pool
from itertools import count
from math import prod
from json import dumps

def multpart(k):
    return dumps(tuple(mp for mp in tuple(tuple(prod(prime) for prime in partition) for partition in multiset_partitions(factorint(k, multiple=True))) if k not in mp))

def main():
    i, n = (int(v) for v in argv[1:3])
    with Pool(4) as pool:
        for res in pool.imap(multpart, count(i, n)):
            print(res)

if __name__ == '__main__':
    main()