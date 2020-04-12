import sys
from sympy.ntheory import factorint

N = int(sys.argv[1])

factors = factorint(N)

print(factors)

R = 1

for f,p in factors.items():
	R *= f**p

print('{} == {} : {}'.format(N, R, N == R))