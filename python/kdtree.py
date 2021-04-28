import numpy as np
from scipy.spatial import cKDTree
from rtree.index import Index
from sys import argv
from time import time as t

N = int(argv[1])
K = int(argv[2])

points = np.random.random_sample(size=(N,2))
queries = np.random.random_sample(size=(K,2))

def test(f,m):
	t1 = t()
	f()
	print(m,t()-t1)

def ckd():
	global qtree
	for i in range(N):
		qtree = cKDTree(points[:i+1])

def qckd():
	for p in queries:
		qtree.query(p)

rtree = Index()
def rt():
	for i,(x,y) in enumerate(points):
		rtree.insert(i,(x,y,x,y))

d = 0.1
def qrt():
	for x,y in queries:
		list(rtree.intersection((x-d,y-d,x+d,y+d)))

def qnv():	
	for x1,y1 in queries:
		min(max(abs(x1-x2),abs(y1-y2)) for x2,y2 in points)

test(ckd,'ckdtree')
test(qckd,'ckdtree query')
test(rt,'rtree')
test(qrt,'rtree query')
test(qnv,'naive query')
