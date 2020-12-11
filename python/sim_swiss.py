from sys import argv
from random import normalvariate as norm

def main():
	N = int(argv[1])
	R = int(argv[2])
	K = float(argv[3])

	p = list([0, v] for v in range(1, N+1))

	print(p)

	for r in range(R):
		for g in range(N//2):
			a = g*2
			b = a+1
			sa = norm(p[a][1], K)
			sb = norm(p[b][1], K)
			if sa == sb:
				p[a][0] += .5
				p[b][0] += .5
			elif sa > sb:
				p[a][0] += 1
			elif sb > sa:
				p[b][0] += 1
		p = sorted(p, reverse=True)
		print(p)

if __name__ == '__main__':
	main()
