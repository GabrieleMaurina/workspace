#!/usr/bin/env python

from os import walk
from os.path import join, relpath
from filecmp import cmp

PATH1 = '/home/gabriele/workspace/dext'
PATH2 = '/home/gabriele/workspace/babelRTS'

EXT = '.py'

def diff(p1, p2):
	def files(p):
		for root, dirs, files in walk(p):
			for name in files:
				if name.endswith(EXT):
					yield relpath(join(root, name), p)
	f1 = set(files(p1))
	f2 = set(files(p2))
	c = f1 & f2
	f1o = f1 - f2
	f2o = f2 - f1
	return len(f1o) + len(f2o) + sum(not cmp(join(p1, f), join(p2, f))for f in c)

print(diff(PATH1, PATH2))
