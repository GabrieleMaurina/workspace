#!/usr/bin/env python

from PIL import Image
from webcolors import name_to_rgb as ntrgb
from sys import argv


def t0(a, b):
	return int(a * b / 255)

def t1(a, b):
	return min(a, b)

def t2(a, b):
	return int(a + (255 - a) * b / 255)

ts = (t0, t1, t2)

def change_color(im, co, t):
	new = Image.new('RGB', im.size)
	np = new.load()
	op = im.load()
	for x in range(im.size[0]):
		for y in range(im.size[1]):
			np[x,y] = tuple(t(a,b) for a,b in zip(co, op[x,y]))
	return new

def main():
	im = Image.open(argv[1])
	im = change_color(im, ntrgb(argv[3]), ts[int(argv[4])])
	im.save(argv[2])
	im.show()

if __name__ == '__main__':
	main()
