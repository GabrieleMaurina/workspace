from sys import argv

def doors_count(n):
	d = [1]*n
	for i in range(2, n+1):
		for j in range(2, n+1):
			if j%i == 0: d[j-1] += 1
	return d

def doors_state(n):
	d = [True]*n
	for i in range(2, n+1):
		for j in range(1, n+1):
			if j%i == 0: d[j-1] = not d[j-1]
	return d

if __name__ == '__main__':
	n = int(argv[1]) if len(argv)>1 else 100
	print('n = ' + str(n))
	print(' '.join(str(i) for i in doors_count(n)))
	print(' '.join(str(i) for i in doors_state(n)))
