from sys import argv

with open(argv[1], 'r') as f:
	print('opened')
	res = f.readlines()
	print('read')
	print(res[-10:])