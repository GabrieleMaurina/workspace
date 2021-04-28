from multiprocessing import Pool, cpu_count
from math import sqrt
from random import random as rand
from sys import argv
from time import time as t

def r():
	return rand()-0.5

def time(f, n):
	it = t()
	res = f(n)
	return t()-it, res

def pi(n):
	t = 0
	for i in range(n):
		if r()**2+r()**2 <= 0.25:
			t += 1
	return t/n/0.25

def ppi_single(n):
	t = 0
	for i in range(n):
		if r()**2+r()**2 <= 0.25:
			t += 1
	return t

def ppi(n):
	cpus = cpu_count()
	data = [n//cpus]*cpus
	with Pool() as p:
		t = p.map(ppi_single,data)
	return sum(t)/n/0.25

def loop(s):
	d = 1/s
	d2 = d/2
	for i in range(s):
		yield (-0.5 + d2 + i*d)**2

def loop2(s):
	for x2 in loop(s):
		for y2 in loop(s):
			yield x2,y2

def square_pi(n):
	t = 0
	s = int(sqrt(n))
	for x2, y2 in loop2(s):
		if x2+y2 <= 0.25:
			t += 1
	return t/s/s/0.25

def fsquare_pi(n):
	t = 0
	s = int(sqrt(n))
	d = 1/s
	b = -0.5+d/2
	for x in range(s):
		for y in range(s):
			if (b+x*d)**2 + (b+y*d)**2 <= 0.25:
				t += 1
	return t/s/s/0.25

def main():
	n = int(argv[1])
	t1, p1 = time(pi,n)
	t2, p2 = time(ppi,n)
	t3, p3 = time(square_pi,n)
	t4, p4 = time(fsquare_pi,n)
	print(f'{t1:.2f} {t2:2.2f} {t3:.2f} {t4:.2f} -  {p1} {p2} {p3} {p4}')

if __name__ == '__main__':
	main()
