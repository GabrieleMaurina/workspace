from random import random as r
from sys import argv

def pi(depth = 100):
	if depth <= 0: return 0
	def p(): return (r()-.5)**2
	circle = 0
	for i in range(depth):
		if p()+p() <= 0.25: circle += 1
	return circle/depth*4

if __name__ == '__main__':
	n = int(argv[1]) if len(argv) > 1 else 100
	print('PI approximated with ' + str(n) + ' points is: ' + str(pi(n)))
