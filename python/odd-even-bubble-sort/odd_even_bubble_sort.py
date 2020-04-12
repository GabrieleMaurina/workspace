from operator import lt, gt
from itertools import accumulate
from PIL import Image, ImageDraw
from random import sample

colors = ('red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple', 'black', 'gray', 'white')

def odd_even(l, comparator=lt):

	def gen(old, i):
		res = list(old)
		if i % 2 == 0:
			for e in range(len(old)//2):
				if comparator(res[e * 2 + 1], res[e * 2]):
					res[e * 2], res[e * 2 + 1] = res[e * 2 + 1], res[e * 2]
		else:
			for e in range((len(old)+1)//2-1):
				if comparator(res[e * 2 + 2], res[e * 2 + 1]):
					res[e * 2 + 1], res[e * 2 + 2] =  res[e * 2 + 2], res[e * 2 + 1]
		return res

	return list(accumulate([list(l)]+list(range(len(l))), gen))

def bubble(l, comparator=lt):

	def gen(old, i):
		res = list(old)
		if i % 2 == 0:
			for e in range(min(i, 2 * len(old) - 4 - i)//2 + 1):
				if comparator(res[e * 2 + 1], res[e * 2]):
					res[e * 2], res[e * 2 + 1] = res[e * 2 + 1], res[e * 2]
		else:
			for e in range(min(i, 2 * len(old) - 4 - i)//2 + 1):
				if comparator(res[e * 2 + 2], res[e * 2 + 1]):
					res[e * 2 + 1], res[e * 2 + 2] =  res[e * 2 + 2], res[e * 2 + 1]
		return res

	return list(accumulate([list(l)]+list(range(2 * len(l) - 3)), gen))

def stringify(l):
	return '\n'.join(','.join(map(str, i)) for i in zip(*l))

def stringify_all(l):
	return '\n\n'.join('\n'.join(' | '.join(line) for line in zip(*((','.join(map(str, i)) for i in tm) for tm in (zip(*m) for m in row)))) for row in l)

def compare(l):
	print(stringify_all([[odd_even(l), bubble(l)]]))

def compare_all(l, file=None, w=10):
	print(stringify_all([[odd_even(i), bubble(i)] for i in l]))

def height(l):
	return len(l[0]) if l else 0

def width(l):
	return len(l)

def draw(l, img, w=10, x=0, y=0):
	w2 = w * 2
	n = height(l)
	m = width(l)
	for i in range(n):
		img.line([(x + w + w2 * e, y + w + l[e].index(l[0][i]) * w2) for e in range(m)], colors[l[0][i]], w, 'curve')

def show(l, file=None, w=10):
	w2 = w * 2
	n = height(l)
	m = width(l)
	img = Image.new('RGBA', (w2 * m, w2 * n))
	can = ImageDraw.Draw(img)
	draw(l, can, w)
	if file:
		img.save(file)
	else:
		img.show()

def show_all(l, file=None, w=10):
	w2 = w * 2
	lines = len(l)
	columns = len(max(l, key=len))
	if lines and columns:
		line_sizes = [height(max(line, key=height)) for line in l]
		column_sizes = [width(max(line, key=width)) for line in zip(*l)]
		line_pos = [0] + [i * w2 for i in accumulate(line_sizes)]
		column_pos = [0] + [i * w2 for i in accumulate(column_sizes)]
		img = Image.new('RGBA', (column_pos[-1] + w * (columns - 1), line_pos[-1] + w * (lines - 1)))
		can = ImageDraw.Draw(img)
		for y, line in enumerate(l):
			for x, m in enumerate(line):
				draw(m, can, w, column_pos[x] + w * x, line_pos[y] + w * y)
		if file:
			img.save(file)
		else:
			img.show()

def compare_show(l, file=None, w=10):
	show_all([[odd_even(l), bubble(l)]], file, w)

def compare_show_all(l, file=None, w=10):
	show_all([[odd_even(i), bubble(i)] for i in l], file, w)

def rev(n):
	return list(reversed(range(n)))

def shu(n):
	return sample(list(range(n)), n)

if __name__ == '__main__':
	l=[rev(5), rev(8), shu(4), shu(6), rev(10), shu(10)]
	#compare_all(l)
	#compare_show_all(l)
	show_all([[bubble(i) for i in l],[odd_even(i) for i in l]])
