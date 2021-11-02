with open('nameAddress.txt','r') as f, open('name.txt','a') as g:
	f = f.read().split('\n')
	for line in f:
		g.write(line.split(' ')[0])
