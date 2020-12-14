import sys
import math
from functools import lru_cache
from time import time


# aks primality test
def expand_x_1(n):
# This version uses a generator and thus less computations
	c =1
	for i in range(n//2+1):
		c = c*(n-i)//(i+1)
		yield c

def aks(p):
	if p==2:
		return 1

	for i in expand_x_1(p):
		if i % p:
# we stop without computing all possible solutions
			return 0
	return 1
#and  aks primality test

def lastindex(lt, val):
	return len(lt) - lt[::-1].index(val) - 1

@lru_cache(maxsize=None)
def f(k):
	if k<=3:
		return 1
	else:
		return F(k-1)

def divisorGen(n):
	large_divisors = []
	for i in range(2, int(math.sqrt(n) + 1)):
		if n % i == 0:
			yield i
			if i*i != n:
				large_divisors.append(n // i)
	for divisor in reversed(large_divisors):
		yield divisor

def fact(k, min_divisor=2):
	if aks(k) == 1:
		yield [k]
	#for divisor in range(min_divisor, k+1):
	for divisor in list(divisorGen(k)):
		for product in fact(k // divisor, divisor):
			yield product + [divisor]

def g(k): #k is composite
	# fact(k) insieme di fattorizzazioni buone
	factk= list(fact2(k))
	#	print k,factk
	b=0
	for seq in factk:
		a=1
		for n in seq:
		#	print "a:", a, "n:",n
			a = a*f(n)
		b=b+a
		#print seq,b
	return b

def F(k): #F(k)= f(k) + pr(k)*g(k)
	if aks(k)==1:
		return f(k)
	else:
		return g(k) + f(k)


def products(n, min_divisor=2):
	"""Generate expressions of n as a product of ints >= min_divisor."""
	if n == 1:
		yield []
	for divisor in range(min_divisor, n+1):
		if n % divisor == 0:
			for product in products(n // divisor, divisor):
				yield product + [divisor]

def fact2(k):
	fact=list(products(k))
	el=[k]
	fact.remove(el)
	return fact

t_start = time()

start = int( sys.argv[1] )
end = int( sys.argv[2] )
i=start
outfile = open("./fine.txt","w")
outfile.write("k \t | Fine(k) \n")
outfile.write("---------------- \n")
while i<=end:
	outfile.write(str(i)+"\t |"+str(F(i))+"\n")
	print(i)
	i=i+1
outfile.close()

t_end = time()

print(t_end - t_start)
