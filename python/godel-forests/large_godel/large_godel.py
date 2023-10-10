from functools import reduce
from operator import mul
from sympy.ntheory import factorint
from sympy.utilities.iterables import multiset_partitions
from multiprocessing import Pool, cpu_count

def multpart(k):
	return k, tuple(mp for mp in tuple(tuple(reduce(mul, prime) for prime in partition) for partition in multiset_partitions(factorint(k, multiple=True))) if k not in mp)

def main():
	with Pool(processes=C) as pool:
		for k, mps in pool.imap(multpart, range(2, K+1)):
			f[k] = f[k-1] + sum(reduce(mul, map(lambda v:f[v-1], mp)) for mp in mps)

if __name__ == '__main__':
	main()
