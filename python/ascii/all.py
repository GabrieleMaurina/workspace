#!/usr/bin/env python

from image_art import run
from os import walk
from os.path import join

def main():
	p = [join(r,n) for r, d, f in walk('images') for n in f]

	run('c1.png', 'poster1S.png', p, (100,75), 240)
	run('c1.png', 'poster1L.png', p, (200,150), 120)
	run('c2.png', 'poster2S.png', p, (100,75), 240)
	run('c2.png', 'poster2L.png', p, (200,150), 120)
	run('c3.png', 'poster3S.png', p, (100,75), 240)
	run('c3.png', 'poster3L.png', p, (200,150), 120)

if __name__ == '__main__':
	main()
