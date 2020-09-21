#!/usr/bin/env python

from collections import defaultdict as ddict
from itertools import groupby
from operator import itemgetter
from collections import Counter

RDF = '/home/gabriele/Downloads/voti19.rdf'
CSV = '/home/gabriele/Downloads/voti19.csv'

TYPE = '<http://purl.org/dc/elements/1.1/type>'
PARTY = '<http://dati.camera.it/ocd/rif_gruppoParlamentare>'
VOTE = '<http://dati.camera.it/ocd/rif_votazione>'


def read_rdf():
	votes = ddict(lambda : ['']*3)
	with open(RDF, 'r') as f:
		for line in f:
			line = line.split()[:3]
			try:
				line[0] = line[0].rsplit('/',1)[-1][:-1]
			except IndexError: pass
			else:
				if len(line) == 3:
					if line[1] == VOTE:
						votes[line[0]][0] = line[2].rsplit('/',1)[-1][:-1]
					elif line[1] == PARTY:
						votes[line[0]][1] = line[2].rsplit('/',1)[-1][:-1]
					elif line[1] == TYPE:
						votes[line[0]][2] = line[2][1:-1]
	return votes

def save_csv(votes):
	with open(CSV, 'w') as f:
		for v in votes.values():
			f.write(','.join(v) + '\n')

def load_csv():
	with open(CSV, 'r') as f:
		votes = f.read().split('\n')
		votes = [v.split(',') for v in votes if v]
		return votes

def group(votes):
	votes = sorted(votes, key=itemgetter(0))
	groups = {}
	for vote, data in groupby(votes, key=itemgetter(0)):
		groups[vote] = {}
		data = sorted(data, key=itemgetter(1))
		for party, v in groupby(data, key=itemgetter(1)):
			groups[vote][party] = list(d[2] for d in v)
	return groups

def count(groups):
	tot = 0
	tot_different = 0
	for vote, parties in groups.items():
		for party, votes in parties.items():
			if party != '':
				n_votes = len(votes)
				different = n_votes - Counter(votes).most_common(1)[0][1]
				#if n_votes > 100: print(party, n_votes, different, different/n_votes*100)
				tot += n_votes
				tot_different += different
	return tot, tot_different

def main():
	votes = read_rdf()
	save_csv(votes)
	votes = load_csv()
	groups = group(votes)
	t, d = count(groups)
	print(t, d, round(d/t*100, 2))

if __name__ == '__main__':
	main()
