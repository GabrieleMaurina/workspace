try:
	from gc import collect

	def gcd(a, b):
		return (b==0 and a) or gcd(b, a%b)	  

	t = int(input())
	for i in range(t):
		n,l=[int(x) for x in input().split()]
		c=[int(x) for x in input().split()]
		p1=gcd(c[0], c[1])
		p2=c[0]//p1
		p=set()
		j=1
		while c[0]==c[j]: j+=1
		if (j%2==1 and c[j]%p2!=0) or (j%2==0 and c[j]%p1!=0): p1=p2
		p.add(p1)
		p2=p1
		for j in range(l):
			c[j]//=p2
			p2=c[j]
			p.add(p2)
		p=sorted(p)
		d={p[j]:chr(j+65) for j in range(26)}
		print("Case #{}: {}".format(i+1, d[p1]), end='')
		for j in c: print(d[j], end='')
		print()
		p=None
		d=None
		collect()
except e:
	pass
