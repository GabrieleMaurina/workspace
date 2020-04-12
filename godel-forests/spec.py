#!python

#from sets import Set
import primefac
import sys
import itertools
import math

# aks primality test
def expand_x_1(n): 
# This version uses a generator and thus less computations
    c =1
    for i in range(n/2+1):
        c = c*(n-i)/(i+1)
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

def f(k):
	if k<=3:
		return 1
	else:
		return F(k-1)

def divisorGen(n):
    large_divisors = []
    for i in xrange(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

def fact(k, min_divisor=2):
    	if aks(k) == 1:
        	yield [k]
	    #for divisor in range(min_divisor, k+1):
	for divisor in list(divisorGen(k)):
		for product in fact(k / divisor, divisor):
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

start = int( sys.argv[1] )
end = int( sys.argv[2] )
i=start
outfile = open("./fine.txt","w")
outfile.write("k \t | Fine(k) \n")
outfile.write("---------------- \n")
while i<=end:
	outfile.write(str(i)+"\t |"+str(F(i))+"\n")
	i=i+1

outfile.close()


'''
def fact(k):
	fact= list()
	#definire partizioni come lista di list
	factors = list( primefac.primefac(k) )  #if factors=[2, 2, 2, 3] 
	mult =  primefac.factorint(k) 		#then mult={2: 3, 3: 1}
	fact.append(factors)
	lfactors=len(factors)-1
	li=2
	levels=list()
	levels.append(factors)
	tuples=list()
	tuples.append(factors)
	c=0
	print factors
	while li<=lfactors:
		print set( itertools.combinations(factors,li))
		print list( itertools.combinations(factors,li))
		print set( itertools.combinations_with_replacement(factors,li))
		print list( itertools.combinations_with_replacement(factors,li))


		li=li+1
	print fact	

		for t in tuples:
			if c>0:
				k=max(t)
			print t,k
			tupapp=list()
			for n in set(t):
				l=list()	
				l.append(n)
				l.append(k/n)
				tupapp.append(l)
		levels.append(tupapp)
		tuples=tupapp	
		c=1
		level_i=level_i+1
		
	print levels
	return fact
'''	#	m=mult[factors[i]]
	#	li= lastindex(factors,factors[i])
	#	print primefac.listprod(fact)
	#	for n in set(factors):
	#	fact= set( itertools.combinations(factors,l))


