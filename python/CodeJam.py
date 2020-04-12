FILE = True

if FILE:
	pin = open('input.in', 'r')
	pout = open('output.out', 'w')
else
	import sys
	pin = sys.stdin
	pout = sys.stdout

cases = int(pin.readline())

for i in range(cases):
    pout.write('Case #' + str(i + 1) + ": ")
    
    pout.write('\n')
    
pin.close()
pout.close()