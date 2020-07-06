#!/usr/bin/env python

# Copyright 2020 by Gabriele Maurina, Università degli Studi di Milano.
# All rights reserved.
# This file is released under the "MIT License Agreement".

from sys import argv
from functools import reduce
from operator import mul
from sympy.ntheory import factorint
from sympy.utilities.iterables import multiset_partitions
from multiprocessing import Pool, cpu_count

def multpart(k):
	return k, tuple(mp for mp in tuple(tuple(reduce(mul, prime) for prime in partition) for partition in multiset_partitions(factorint(k, multiple=True))) if k not in mp)

def fine(K, C=1):
	f = [1] * (K+1)
	with Pool(processes=C) as pool:
		for k, mps in pool.imap(multpart, range(2, K+1)):
			f[k] = f[k-1] + sum(reduce(mul, map(lambda v:f[v-1], mp)) for mp in mps)
			yield k, f[k]


def main(K, C=1):
	with open('fine.csv', 'w') as out:
		out.write('K,Fine(K)\n')
		for k, fk in fine(K):
			out.write('{},{}\n'.format(k, fk))
			#print(k)

if __name__ == '__main__':
	main(*(int(v) for v in argv[1:]))