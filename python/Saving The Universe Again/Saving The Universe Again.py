import sys

pin = sys.stdin
pout = sys.stdout

#pin = open('input.in', 'r')
#pout = open('output.out', 'w')

def dmg(l):
	t = 0
	s = 1
	for a in l:
		if a == 'S':
			t += s
		else:
			s *= 2
	return t

cases = int(pin.readline())

for i in range(cases):
	pout.write('Case #' + str(i + 1) + ": ")
	
	D, P = pin.readline().split()
	D = int(D)
	d = dmg(P)
	c = [i for i,a in enumerate(P) if a == 'C']
	N = len(P)
	t = 0
	
	for j in range(len(c) - 1, -1, -1):
		while d > D and c[j] < N + j - len(c):
			c[j] += 1
			t += 1
			d -= 2 ** j
	
	if d > D:
		pout.write('IMPOSSIBLE')
	else:
		pout.write(str(t))
	
	pout.write('\n')
	
pin.close()
pout.close()