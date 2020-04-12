from functools import *

print(sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0]))

def smallest(k):
	delta = reduce(lambda x, y: x*y, [x for x in range(2, k + 1) if all(x%i != 0 for i in range(2, x))])
	n = delta
	while any(n % i != 0 for i in range(2, k + 1)): n += delta
	return n

print(smallest(100))

def smallest_fast(k):
	f = {}
	for i in range(2, k + 1):
		for key in f:
			c = 0
			while i % key == 0:
				i /= key
				c += 1
			f[key] = max(f[key], c)
		if i != 1:
			f[i] = 1
	return reduce(lambda x, y: x * y, map(lambda f: f[0]**f[1], f.items()))

print(smallest_fast(100))

print(sum(map(lambda x: int(x), str(2**1000))))

def fib(n):
	x, y = 1, 1
	while y < 10 ** n: x, y = y, x + y
	return y

print(fib(1000))