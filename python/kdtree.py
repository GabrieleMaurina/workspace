import numpy as np
from scipy.spatial import cKDTree
from rtree.index import Index
from sys import argv
from time import time as t

N = int(argv[1])
K = int(argv[2])

points = np.random.random_sample(size=(N,2))
queries = np.random.random_sample(size=(K,2))

t1 = t()
for i in range(N):
	qtree = cKDTree(points[:i+1])
print(t()-t1)

t1 = t()
for p in queries:
	qtree.query(p)
print(t()-t1)

rtree = Index()
d = 0.01

t1 = t()
for i,(x,y) in enumerate(points):
	rtree.insert(i,(x-d,y+d,x+d,y+d))
print(t()-t1)

t1 = t()
for x,y in queries:
	list(rtree.intersection((x-d,y-d,x+d,y+d)))
print(t()-t1)
