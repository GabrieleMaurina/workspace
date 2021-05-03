from sys import argv
from random import randrange

N = int(argv[1])

def r():
    return randrange(6)+1

tot = 0
for i in range(N):
    v = 0
    t = 0
    while v != 1:
        v = r()
        if v > 1:
            t += v
    tot += t

print(tot/N)
