from subprocess import Popen, PIPE
from sympy.ntheory import factorint
from sympy.utilities.iterables import multiset_partitions
from itertools import count, cycle
from math import prod
from json import loads

OUT = 'fine.csv'
WORKERS = 'workers.txt'
PATH = '/s/chopin/a/grad/gmaurina/workspace/godel'

def worker(w, i, n):
    print(f'ssh {w} "cd {PATH} ; python3.8 multpart.py {i} {n}"')
    return Popen(f'ssh {w} "cd {PATH} ; python3.8 multpart.py {i} {n}"', shell=True, stdout=PIPE).stdout

def multpart():
    with open(WORKERS, 'r') as workers:
        workers = tuple(w for w in workers.read().split('\n') if w)
    n = len(workers)
    print(workers)
    workers = tuple(worker(w, i, n) for i, w in enumerate(workers, 2))
    for k, w in enumerate(cycle(workers)):
        yield k, loads(w.readline())

def fine():
    f = [1,1]
    for k, mps in multpart():
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
