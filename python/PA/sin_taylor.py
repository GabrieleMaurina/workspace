from math import factorial, sin
sin_taylor = lambda x, n=1, d=1: x**(d*2-1)/factorial(d*2-1) - (sin_taylor(x, n, d+1) if d < n else 0)

if __name__ == '__main__':
	print(sin_taylor(1, 30), sin(1))
