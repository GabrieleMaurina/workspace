from sympy.ntheory import factorint
from sympy.utilities.iterables import multiset_partitions
from itertools import count
from math import prod

OUT = 'fine.csv'

def multpart(k):
    return tuple(mp for mp in tuple(tuple(prod(prime) for prime in partition) for partition in multiset_partitions(factorint(k, multiple=True))) if k not in mp)

def fine():
    f = [1,1]
    for k in count(start=2):
        mps = multpart(k)
        f.append(f[k-1] + sum(prod(map(lambda v:f[v-1], mp)) for mp in mps))
        yield k, f[k]

def main():
    with open(OUT, 'w') as out:
        out.write('K,Fine(K)\n')
    for k, fk in fine():
        with open(OUT, 'a') as out:
            out.write(f'{k},{fk}\n')

if __name__ == '__main__':
    main()
