#!/usr/bin/env python

from PIL import Image
from random import randrange as rr
from argparse import ArgumentParser as Parser
from colorthief import ColorThief
from operator import sub

class CT(ColorThief):
	def __init__(self, image):
		self.image = image

class PixelImages:
	def __init__(self, pi, k):
		self.pi = pi
		self.k = min(k, len(pi))

	def __key(self, c):
		def k(p):
			return sum(map(abs,map(sub,p[1],c)))
		return k

	def get_image(self, c):
		i = rr(self.k)
		return self.change_color(sorted(self.pi, key=self.__key(c))[i][0], c)

	def __t(self, a, b):
		return int(a * b / 255)

	def change_color(self, ii, c):
		ci = Image.new('RGB', ii.size)
		cp = ci.load()
		ip = ii.load()
		for x in range(ii.size[0]):
			for y in range(ii.size[1]):
				cp[x,y] = tuple(self.__t(a,b) for a,b in zip(c, ip[x,y]))
		return ci

def generate(ii, pi, k):
	pi = PixelImages(pi,k)

	s = pi.pi[0][0].size[0]
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
	p.add_argument('-k', metavar='<K>', default=10, type=int, help='use K nearest images')
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

def run(i, o, p, r, s, k):
	ii = Image.open(i)
	if r: ii = ii.resize(r)
	pi = list(map(lambda v: (v, CT(v).get_color()) , map(lambda v:fix_pixel_image(Image.open(v),s), p)))
	oi = generate(ii, pi, k)
	oi.save(o)

def main():
	a = parse_args()
	run(a.i, a.o, a.p, a.r, a.s, a.k)

if __name__ == '__main__':
	main()
