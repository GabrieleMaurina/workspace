from inspect import getsource, getsourcelines
from os import fork
from time import sleep
from multiprocessing import Process as p

def a():
	print('asdf')
	exec('{}a()'.format(getsource(a)))

def b():
	pid = fork()
	if not pid:
		print('asdf')
		sleep(5)
		print('asdf')

def c():
	def f():
		print('qwer')
		sleep(5)
		print('qwer')
	p(target=f, daemon=True).start()
c()
