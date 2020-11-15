#!/usr/bin/env python

from PIL import Image
from random import randrange as rr
from argparse import ArgumentParser as Parser

class PixelImages:
	def __init__(self, pi):
		self.pi = pi
		self.l = len(pi)

	def get_image(self, c):
		i = rr(self.l)
		return self.change_color(self.pi[i], c)

	def t(self, a, b):
		return int(a * b / 255)

	def change_color(self, ii, c):
		ci = Image.new('RGB', ii.size)
		cp = ci.load()
		ip = ii.load()
		for x in range(ii.size[0]):
			for y in range(ii.size[1]):
				cp[x,y] = tuple(self.t(a,b) for a,b in zip(c, ip[x,y]))
		return ci

def generate(ii, pi):
	pi = PixelImages(pi)

	s = pi.pi[0].size[0]
	w, h = ii.size
	tot = w * h
	count = 0
	
	oi = Image.new('RGB', (w*s, h*s))
	data = ii.load()
	
	for x in range(w):
		for y in range(h):
			oi.paste(pi.get_image(data[x,y]), (x*s, y*s))
			count += 1
			print('{:.2f}%'.format(count/tot*100))
	return oi

def parse_args():
	p = Parser(description='Generate image art.')
	p.add_argument('-i', metavar='<input>', required=True, help='input image')
	p.add_argument('-o', metavar='<output>', required=True, help='output image')
	p.add_argument('-p', metavar='<image>', required=True, nargs='+', help='images to use as pixels')
	p.add_argument('-r', metavar='<size>', default=None, type=int, nargs=2, help='resize input image width, height')
	p.add_argument('-s', metavar='<size>', default=20, type=int, help='width of 1 pixel image')
	return p.parse_args()

def crop_square(i):
	w, h = i.size
	s = min(w,h)
	l = (w - s) // 2
	u = (h - s) // 2
	r = (w + s) // 2
	d = (h + s) // 2
	return i.crop((l,u,r,d))

def fix_pixel_image(i, s):
	return crop_square(i).resize((s,s))

def run(i, o, p, r, s):
	ii = Image.open(i)
	if r: ii = ii.resize(r)
	pi = [fix_pixel_image(Image.open(v),s) for v in p]
	oi = generate(ii, pi)
	oi.save(o)

def main():
	a = parse_args()
	run(a.i, a.o, a.p, a.r, a.s)

if __name__ == '__main__':
	main()
