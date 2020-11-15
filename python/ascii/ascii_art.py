#!/usr/bin/env python

from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageChops
from argparse import ArgumentParser as Parser
from string import ascii_letters as letters, digits, punctuation
from glob import iglob

def nearest(d, v):
	return d[min(d.keys(), key=lambda k:abs(v-k))]

def generate_table(size, font, chars):
	larger = int(size * 1.1)
	white = Image.new('1', (larger,larger), 1)
	d = {}
	for font in iglob(font):
		font = ImageFont.truetype(font,larger)
		for char in reversed(chars):
			im = Image.new('1', (larger,larger), 1)
			ImageDraw.Draw(im).text((0,0), 'W', font=font)
			im = im.crop(ImageChops.difference(white,im).getbbox())
			im.show()
			exit(0)
			key = sum(im.getdata())
			print(key)
			d[key] = im
	d = {i * size * size / (len(d.keys())-1): d[k] for i, k in enumerate(sorted(d.keys()))}
	return [nearest(d, v) for v in range(size*size + 1)]

def generate_art(reference, resize, size, table):
	reference = Image.open(reference)
	if resize: reference = reference.resize(resize)
	reference = reference.convert('L')
	reference = ImageEnhance.Contrast(reference).enhance(1)
	
	result = Image.new('1', tuple(v * size for v in reference.size), 1)
	p = reference.load()
	for x in range(reference.size[0]):
		for y in range(reference.size[1]):
			v = p[x,y]*size*size//255
			w, h = table[v].size
			px = int(x*size + (size-w)/2)
			py = int(y*size + (size-w)/2)
			result.paste(table[v], (px,py))
	return result

def run(in_im, out_im, resize, size, font):
	chars = letters + digits + punctuation
	table = generate_table(size, font, chars)
	result = generate_art(in_im, resize, size, table)
	result.save(out_im)

def parse_args():
	p = Parser(description='Generate ascii art.')
	p.add_argument('-i', metavar='<input>', default='input.png', help='input image')
	p.add_argument('-o', metavar='<output>', default='output.png', help='output image')
	p.add_argument('-r', metavar='<resize>', default=None, type=int, nargs=2, help='resize <px> x <px>')
	p.add_argument('-s', metavar='<size>', default=10, type=int, help='size of 1 char')
	p.add_argument('-f', metavar='<font>', default='fonts/*.ttf', help='font')
	return p.parse_args()

def main():
	args = parse_args()
	run(args.i, args.o, args.r, args.s, args.f)

if __name__ == '__main__':
	main()
