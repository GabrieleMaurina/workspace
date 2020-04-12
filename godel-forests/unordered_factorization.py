from sympy.ntheory import factorint
from sympy.utilities.iterables import multiset_partitions
from functools import reduce
from operator import mul

print(factorint(12, multiple=True))
#[2, 2, 3]

print(list(multiset_partitions(factorint(12, multiple=True))))
#[[[2, 2, 3]], [[2, 2], [3]], [[2, 3], [2]], [[2], [2], [3]]]

print([[reduce(mul, primes) for primes in partition] for partition in multiset_partitions(factorint(12, multiple=True))])
#[[12], [4, 3], [6, 2], [2, 2, 3]]
