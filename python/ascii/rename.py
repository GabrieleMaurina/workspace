#!/usr/bin/env python

from sys import argv
from os import walk, rename
from os.path import join

def main():
	i = 0
	for root, dirs, files in walk(argv[1]):
		for name in files:
			ext = name.rsplit('.', 1)[-1]
			old = join(root, name)
			new = join(root, f'{i:03d}.{ext}')
			rename(old, new)
			i += 1

if __name__ == '__main__':
	main()
