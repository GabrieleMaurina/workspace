import sys
import itertools
from time import time

def factors(N):
	if sympy_optimization:
		return get_factors(N)
	else:
		return find_factors(N)

def get_factors(N):
	from sympy.ntheory import factorint
	from sympy.utilities.iterables import multiset_partitions
	from functools import reduce
	from operator import mul

	return [l for l in [[reduce(mul, primes) for primes in partition] for partition in multiset_partitions(factorint(N, multiple=True))] if N not in l]

def find_factors(N, numbers=[], min=2, max=-1):
	if N == 1:
		yield numbers
	else:
		if max == -1:
			max=N
		for i in range(min, max):
			if N % i == 0:
				numbers.append(i)
				for res in find_factors(N // i, numbers, i, max):
					yield res
				del numbers[-1]

def count_fine(K):
	f = [1] * (K + 1)
	for i in range(2, K + 1):
		f[i] = f[i - 1]
		for p in factors(i):
			c = 1
			for n in p:
				c *= f[n-1]
			f[i] += c
		yield f[i]

def counter(K):
	out = open('count.txt', 'w')
	out.write('K Fine(K)\n\n')
	for i, v in enumerate(count_fine(K)):
		out.write(str(i + 2) + ' ' + str(v) + '\n')
		if verbose: print(i + 2)
	out.close()

def generate_fine(K):
	g = [[[]]] * (K + 1)
	if K >= 2:
		g[2] = [[[]]]
		yield g[2]
	for i in range(3, K + 1):
		g[i] = [[j] for j in g[i-1]]
		for p in factors(i):
			p = [g[n-1] for n in p]
			for c in itertools.product(*p):
				g[i].append(list(c))
		yield g[i]

def printer(K):
	out = open('print.txt', 'w')
	for i, v in enumerate(generate_fine(K)):
		out.write('{}\n\n'.format(i+2))
		for f in v:
			for t in f:
				out.write(str(t) + '\n')
			out.write('\n')
		if verbose: print(i + 2)
	out.close()

id = 0
def draw(graph, t):
	global id
	name = str(id)
	for n in t:
		id += 1
		graph.edge(name, str(id))
		draw(graph, n)

def drawer(K):
	global id
	from graphviz import Graph as G
	index = sys.argv.index('-d')
	format = None
	if index + 2 < len(sys.argv) and not sys.argv[index + 1].startswith('-'):
		format = sys.argv[index + 1].replace('"', '').replace("'", '')
	for i, v in enumerate(generate_fine(K)):
		if i + 2 == K:
			graph = G(str(K), filename='draw', format=format if format else 'svg')
			graph.attr('node', shape='point')
			for j,f in enumerate(v):
				forest = G(name='cluster'+str(j))
				for t in f:
					id += 1
					forest.node(str(id))
					draw(forest, t)
				graph.subgraph(forest)
			graph.render()
		if verbose: print(i + 2)

if __name__ == "__main__":
	verbose = '-v' in sys.argv
	sympy_optimization = '-s' in sys.argv
	help = '***Godel fine forests***\nCount or draw the non-isomorphic k-element Godel algebras.\n\nUsage:\n\tpython3 godel-fine-forests.py [options] K\n\nOptions:\n\t-c\t\tcount\n\t-d [format]\tdraw (requires graphviz installation)\n\t-h\t\thelp\n\t-p\t\tprint\n\t-s\t\tsympy optimization (requires sympy installation)\n\t-v\t\tverbose'
	if '-h' in sys.argv or len(sys.argv) < 2:
		print(help)
	try:
		if verbose: t_start = time()
		if '-c' in sys.argv:
			counter(int(sys.argv[-1]))
		if '-p' in sys.argv:
			printer(int(sys.argv[-1]))
		if '-d' in sys.argv:
			drawer(int(sys.argv[-1]))
		if verbose:
			t_end = time()
			print('Time: {}s.'.format(t_end - t_start))
	except:
		print(help)
