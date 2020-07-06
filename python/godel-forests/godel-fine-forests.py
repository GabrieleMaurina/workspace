#!/usr/bin/env python3

from argparse import ArgumentParser as arg_par
from itertools import product
from functools import reduce
from operator import mul

sympy_optimization = False
factorint = None
multiset_partitions = None

def factors(N):
	if sympy_optimization: return get_factors(N)
	else: return find_factors(N)

def get_factors(N):
	return [l for l in [[reduce(mul, prime) for prime in partition] for partition in multiset_partitions(factorint(N, multiple=True))] if N not in l]

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

def counter(K, verbose=False):
	with open('count.txt', 'w') as out:
		out.write('K,Fine(K)\n')
		for i, v in enumerate(count_fine(K)):
			out.write(str(i + 2) + ',' + str(v) + '\n')
			if verbose: print(i + 2)

def generate_fine(K):
	g = [[[]]] * (K + 1)
	if K >= 2:
		g[2] = [[[]]]
		yield g[2]
	for i in range(3, K + 1):
		g[i] = [[j] for j in g[i-1]]
		for p in factors(i):
			p = [g[n-1] for n in p]
			for c in product(*p):
				g[i].append(list(c))
		yield g[i]

def printer(K, verbose=False):
	with open('print.txt', 'w') as out:
		for i, v in enumerate(generate_fine(K)):
			out.write('{}\n\n'.format(i+2))
			for f in v:
				for t in f:
					out.write(str(t) + '\n')
				out.write('\n')
			if verbose: print(i + 2)
id = 0
def draw(graph, t):
	global id
	name = str(id)
	for n in t:
		id += 1
		graph.edge(name, str(id))
		draw(graph, n)

def drawer(K, format='svg', verbose=False):
	from graphviz import Graph as G
	global id
	id = 0
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

def parse_args():
	parser = arg_par(prog= 'python godel-fine-forests.py', description='Count or draw the non-isomorphic k-element Godel algebras.')
	parser.add_argument('K', type=int, help='compute forests up to K')
	parser.add_argument('-v', '--verbose', action='store_true', help='increase output verbosity')
	parser.add_argument('-c', '--count', action='store_true', help='count the forests and saves csv "count.txt"')
	parser.add_argument('-p', '--print', action='store_true', help='print the forests as list rapresentation into "print.txt"')
	parser.add_argument('-d', '--draw', metavar='format', default='', nargs='?', help='draw the forests onto image "draw.svg" (requires GraphViz)')
	parser.add_argument('-s', '--sympy', action='store_true', help='use sympy optimization (requires Sympy)')
	args = parser.parse_args()
	if args.draw == None: args.draw = 'svg'
	elif args.draw == '': args.draw = None
	if not args.count and not args.print and args.draw == None:
		parser.error('Specify at least one action between count, print or draw.')
	return args

def import_sympy():
	global factorint, multiset_partitions, sympy_optimization
	from sympy.ntheory import factorint
	from sympy.utilities.iterables import multiset_partitions
	sympy_optimization = True

def main():
	args = parse_args()
	if args.sympy: import_sympy()
	if args.count: counter(args.K, args.verbose)
	if args.print: printer(args.K, args.verbose)
	if args.draw: drawer(args.K, args.draw, args.verbose)

if __name__ == "__main__":
	main()
